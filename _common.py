


import os
import json

script_dir = os.path.dirname(os.path.realpath(__file__))


with open(script_dir+'/data/offsets.json') as f:
    data = json.load(f)


versions = list(data.keys())


def MemoryToAddressLibrary(version, input):
    if(input not in data[version]["skyrim-to-address"]):
        print("address "+input+" not found on address library")
        return 0
    return data[version]["skyrim-to-address"][input]

def AddressLibraryToMemory(version, input):
    if(str(input) not in data[version]["address-to-skyrim"]):
        print("address "+str(input)+" not found on address library")
        return 0
    raw_address = int(data[version]["address-to-skyrim"][str(input)],16)
    offset = 0x140000000
    return hex(offset+raw_address)

class AddressLibrary:
    def __init__(self, version):
        self.version = version
    def PrintAddress(self, entryPoint, offset):
        print(str(MemoryToAddressLibrary(self.version,"0x"+str(entryPoint)[2:].lstrip('0')))+" "+hex(offset).rstrip('L'))
    def GetMemory(self, address):
        return AddressLibraryToMemory(self.version, address).rstrip('L')


