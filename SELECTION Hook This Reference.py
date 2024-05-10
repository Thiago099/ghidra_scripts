#@author 
#@category _NEW_
#@keybinding ctrl h
#@menupath 
#@toolbar 

from ghidra.app.script import GhidraScript
from ghidra.util.task import ConsoleTaskMonitor
from ghidra.program.model.symbol import ReferenceManager

from  _common import AddressLibrary
scriptName = "Hook  this function"
class MyScript(GhidraScript):
	def run(self):
		library = AddressLibrary(currentProgram)

		if(not library.IsValid()):
			return
		
		func = getFunctionContaining(currentAddress)
		if func is not None:
			entryPoint = func.getEntryPoint()
			offset = currentAddress.subtract(entryPoint)
			library.PrintAddress(entryPoint,offset)
		else:
			print("address " + str(currentAddress) + " is not on a function")


script = MyScript()
script.run()

