#@author 
#@category _NEW_
#@keybinding 
#@menupath 
#@toolbar 

from ghidra.app.script import GhidraScript
from ghidra.util.task import ConsoleTaskMonitor
from ghidra.program.model.symbol import ReferenceManager

from  _common import versions, AddressLibrary
scriptName = "Get Address Library ID"
class MyScript(GhidraScript):
	def run(self):
		library = AddressLibrary(askChoice(scriptName, "Please Select The Game Version:", versions, versions[0]))

		if not library.PrintAddressLibraryIds(currentAddress):
			try:
				instruction = getInstructionAt(currentAddress)
				ref_address = instruction.getOperandReferences(0)[0].getToAddress()
				library.PrintAddressLibraryIds(ref_address)
			except:
				print("Failed to get the reference")
				print("This might not be a known function")
				print("Otherwise, if you are in a function, you could try going to the definition of the item")

script = MyScript()
script.run()

