#TODO write a description for this script
#@author 
#@category _NEW_
#@keybinding 
#@menupath 
#@toolbar 


#TODO Add User Code Here


#TODO write a description for this script
#@author 
#@category _NEW_
#@keybinding
#@menupath 
#@toolbar 
from ghidra.app.script import GhidraScript
from ghidra.util.task import ConsoleTaskMonitor
from  _common import versions, AddressLibraryDisplay

class ExampleScript(GhidraScript):
    def run(self):
        return askChoice("Game Version", "Please Select The Game Version:", versions, versions[0])

script = ExampleScript()
lib = AddressLibraryDisplay(script.run())

from ghidra.program.model.symbol import ReferenceManager

func = getFunctionContaining(currentAddress)

if func is not None:
	entryPoint = func.getEntryPoint()
	offset = currentAddress.subtract(entryPoint)
	lib.PrintAddress(entryPoint,offset)
