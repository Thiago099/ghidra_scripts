


import os
import json

script_dir = os.path.dirname(os.path.realpath(__file__))


with open(script_dir+'/data/offsets.json') as f:
    offsets = json.load(f)

with open(script_dir+'/data/known-addresses.json') as f:
    known_addresses = json.load(f)

versions = list(offsets.keys())


def MemoryToAddressLibrary(version, input):
    if(input not in offsets[version]["skyrim-to-address"]):
        print("address "+input+" not found on address library")
        return 0
    return offsets[version]["skyrim-to-address"][input]

def MemoryToAddressLibrarySilent(version, input):
    if(input not in offsets[version]["skyrim-to-address"]):
        return 0
    return offsets[version]["skyrim-to-address"][input]

def AddressLibraryToMemory(version, input):
    if(str(input) not in offsets[version]["address-to-skyrim"]):
        print("address "+str(input)+" not found on address library")
        return "0"
    raw_address = int(offsets[version]["address-to-skyrim"][str(input)],16)
    offset = 0x140000000
    return hex(offset+raw_address)

def GetAddressName(game_version, input):
    return known_addresses[game_version][input]["name"]

def GetAllIDS(game_version):
    return list(known_addresses[game_version].keys())

def GetAddressPair(game_version, input):
    return known_addresses[game_version][input]["pair"]
class AddressLibrary:
    def __init__(self, version):
        self.version = version
        self.game_version = offsets[version]["game-version"]

    def getGameVersion(self):
        return self.game_version
    def getExactVersion(self):
        return self.version
    def GetAllIDS(self):
        return GetAllIDS(self.game_version)
    
    def GetIdName(self, id):
        return GetAddressName(self.game_version, id)
    
    def PrintAddress(self, entryPoint, offset):
        print(str(MemoryToAddressLibrary(self.version,"0x"+str(entryPoint)[2:].lstrip('0')))+" "+hex(offset).rstrip('L'))

    def GetMemory(self, address):
        return AddressLibraryToMemory(self.version, address).rstrip('L')
    
    def PrintAddressLibraryIds(self, address):
        id = str(MemoryToAddressLibrarySilent(self.version,"0x"+str(address)[2:].lstrip('0')))
        if id == "0":
            return False

        pair = GetAddressPair(self.game_version,id)
        if(self.game_version == "ae"):
            print("SE: "+str(pair))
            print("AE: "+str(id))
        else:
            print("SE: "+str(id))
            print("AE: "+str(pair))

        return True



