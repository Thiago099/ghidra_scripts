
#TODO write a description for this script
#@author 
#@category _NEW_
#@keybinding
#@menupath 
#@toolbar 
from ghidra.app.script import GhidraScript
from ghidra.util.task import ConsoleTaskMonitor
from ghidra.program.model.symbol import ReferenceManager

from  _common import versions, AddressLibraryDisplay

class ExampleScript(GhidraScript):
    def run(self):
        return askChoice("Game Version", "Please Select The Game Version:", versions, versions[0])

script = ExampleScript()
lib = AddressLibraryDisplay(script.run())

refs = currentProgram.referenceManager.getReferencesTo(currentAddress)

for ref in refs:
	address = ref.getFromAddress()
	func = getFunctionContaining(address)
	if func is not None:
		entryPoint = func.getEntryPoint()
		offset = address.subtract(entryPoint)
		lib.PrintAddress(entryPoint, offset)
