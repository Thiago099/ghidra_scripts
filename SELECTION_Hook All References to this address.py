#@author 
#@category _NEW_
#@keybinding ctrl alt h
#@menupath 
#@toolbar 
from ghidra.app.script import GhidraScript

from  _common import versions, AddressLibrary

scriptName = "Hook All References to this function"


class MyScript(GhidraScript):
	def run(self):
		library = AddressLibrary(askChoice(scriptName, "Please Select The Game Version:", versions, versions[0]))


		refs = currentProgram.referenceManager.getReferencesTo(currentAddress)

		if not refs.hasNext():
			instruction = getInstructionAt(currentAddress)
			ref_address = instruction.getOperandReferences(0)[0].getToAddress()
			refs = currentProgram.referenceManager.getReferencesTo(ref_address)
			

		for ref in refs:
			address = ref.getFromAddress()
			func = getFunctionContaining(address)

			if func is not None:
				entryPoint = func.getEntryPoint()
				offset = address.subtract(entryPoint)
				library.PrintAddress(entryPoint, offset)
			else:
				print("address " + str(address) + " is not on a function")


script = MyScript()
script.run()


