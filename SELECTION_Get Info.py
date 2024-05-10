#@author 
#@category _NEW_
#@keybinding 
#@menupath 
#@toolbar 

from ghidra.app.script import GhidraScript
from ghidra.util.task import ConsoleTaskMonitor
from ghidra.program.model.symbol import ReferenceManager

from  _common import AddressLibrary
scriptName = "Get Info"
class MyScript(GhidraScript):
	def run(self):
		library = AddressLibrary(currentProgram)
		data = library.GetMemoryData(currentAddress)
		if data == "-1":
			try:
				instruction = getInstructionAt(currentAddress)
				ref_address = instruction.getOperandReferences(0)[0].getToAddress()
				data = library.GetMemoryData(ref_address)
			except:
				print("definition not found")

		if data:
			if(data == "-1"):
				print("definition not found")
				return
			print(data["definition"])
script = MyScript()
script.run()

