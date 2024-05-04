#@author 
#@category _NEW_
#@keybinding ctrl alt b
#@menupath 
#@toolbar 

from ghidra.app.script import GhidraScript
from ghidra.util.task import ConsoleTaskMonitor
from  _common import versions, AddressLibrary


scriptName = "Bookmark address library"
class MyScript(GhidraScript):
	def run(self):
		version = askChoice(scriptName, "Please Select The Game Version:", versions, versions[0])
		library = AddressLibrary(version)
		address = library.GetMemory(askInt(scriptName, "Please enter your address: "))
		createBookmark(currentProgram.getAddressFactory().getAddress(address), "Addresses", "Description")


script = MyScript()
script.run()