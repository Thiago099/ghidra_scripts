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

		id = askInt(scriptName, "Please enter an address library id:")
		isEqual = askYesNo(scriptName, "Is this address for the " + library.getGameVersion() + " version of skyrim?")

		if(isEqual):
			address = library.GetMemory(id)
		else:
			matchId = library.GetIdForCurrentVersion(str(id))
			if(matchId == "-1"):
				print("Your id was not found in the version match, you will need to find it manually")
				return
			address = library.GetMemory(matchId)

		createBookmark(currentProgram.getAddressFactory().getAddress(address), "Addresses", "Description")


script = MyScript()
script.run()