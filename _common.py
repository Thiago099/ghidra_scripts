


import os
import json

import re


script_dir = os.path.dirname(os.path.realpath(__file__))


with open(script_dir+'/data/offsets.json') as f:
    offsets = json.load(f)

with open(script_dir+'/data/definition.json') as f:
    definition = json.load(f)

with open(script_dir+'/data/addresses_match.json') as f:
    address_match = json.load(f)

versions = list(offsets.keys())

pair = {"ae":"se","se":"ae"}


def MemoryToAddressLibrary(version, input):
    input = "0x"+str(input)[2:].lstrip('0')
    if(input not in offsets[version]["skyrim-to-address"]):
        print("address "+input+" not found on address library")
        return 0
    return offsets[version]["skyrim-to-address"][input]


def MemoryToAddressLibrarySilent(version, input):
    input = "0x"+str(input)[2:].lstrip('0')
    if(input not in offsets[version]["skyrim-to-address"]):
        return "-1"
    return offsets[version]["skyrim-to-address"][input]

def AddressLibraryToMemory(version, input):
    if(str(input) not in offsets[version]["address-to-skyrim"]):
        print("address "+str(input)+" not found on address library")
        return "-1"
    raw_address = int(offsets[version]["address-to-skyrim"][str(input)],16)
    offset = 0x140000000
    return hex(offset+raw_address)

def GetMatchID(game_version, input):
    if(input in address_match[game_version]):
        return address_match[game_version][input]
    print("failed to get the match address for input: "+input)
    return "-1"

def GetAddressData(game_version,version, input):
    if(game_version == "ae"):
        input = GetMatchID("ae", input)
    if(input in definition):
        return definition[input]
    
    return "-1"

def GetAllIds(game_version):
    if(game_version == "ae"):
        input =  [item for item in [GetMatchID("se", item) for item in list(definition.keys())] if item != "-1"]
    else:
        input = list(definition.keys())
    return input

class AddressLibrary:
    def __init__(self, currentProgram):
        metadata = currentProgram.getMetadata()
        for key, value in metadata.items():
            if(key == "PE Property[ProductVersion]"):
                version = re.sub(r'\.[^.]*$', '', value)
                self.version = version
                break
        if(self.version):
            self.game_version = offsets[self.version]["game-version"]
        else:
            print("version is not on the database, you need to generate the files")

    def GetCurrentVersionId(self,target_version, id):
        if(target_version == self.game_version):
            return id
        return GetMatchID(self.game_version, id)
    
    def GetIdForCurrentVersion(self, id):
        return GetMatchID(pair[self.game_version], id)
    
    def getGameVersion(self):
        return self.game_version
    def getExactVersion(self):
        return self.version
    def GetAllIds(self):
        return GetAllIds(self.game_version)
    
    def GetAddressData(self, id):
        return GetAddressData(self.game_version, self.version, id)
    def GetMemoryData(self, address):
        id = str(MemoryToAddressLibrarySilent(self.version, str(address)))
        if id == "-1":
            return "-1"
        return GetAddressData(self.game_version, self.version, id)
    
    def PrintAddress(self, entryPoint, offset):
        print(str(MemoryToAddressLibrary(self.version,entryPoint))+" "+hex(offset).rstrip('L'))

    def GetGameVersion(self):
        return self.game_version.upper()

    def GetMemory(self, address):
        return AddressLibraryToMemory(self.version, address).rstrip('L')
    
    def PrintAddressLibraryIds(self, address):
        id = str(MemoryToAddressLibrarySilent(self.version, str(address)))
        if id == "-1":
            return False
        pair = GetMatchID(self.game_version, id)
        if(str(pair)=="-1"):
            return False

        if(self.game_version == "ae"):
            print("SE: "+str(pair))
            print("AE: "+str(id))
        else:
            print("SE: "+str(id))
            print("AE: "+str(pair))

        return True



