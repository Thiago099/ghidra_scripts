


import os
import json

script_dir = os.path.dirname(os.path.realpath(__file__))


with open(script_dir+'/offsets.json') as f:
    data = json.load(f)


versions = list(data.keys())


def MemoryToAddressLibrary(version, input):
    return data[version][input]

class AddressLibraryDisplay:
    def __init__(self, version):
        self.version = version
    def PrintAddress(self, entryPoint, offset):
	    print(str(MemoryToAddressLibrary(self.version,"0x"+str(entryPoint)[2:].lstrip('0')))+" "+hex(offset).rstrip('L'))


