#@author 
#@category _NEW_
#@keybinding ctrl alt h
#@menupath 
#@toolbar 
from ghidra.app.script import GhidraScript
from ghidra.util.task import ConsoleTaskMonitor
from ghidra.program.model.symbol import ReferenceManager

from  _common import versions, AddressLibrary

scriptName = "Hook All References to this function"
class MyScript(GhidraScript):
	def run(self):
		library = AddressLibrary(askChoice(scriptName, "Please Select The Game Version:", versions, versions[0]))
		refs = currentProgram.referenceManager.getReferencesTo(currentAddress)
		for ref in refs:
			address = ref.getFromAddress()
			func = getFunctionContaining(address)
			if func is not None:
				entryPoint = func.getEntryPoint()
				offset = address.subtract(entryPoint)
				library.PrintAddress(entryPoint, offset)


script = MyScript()
script.run()


