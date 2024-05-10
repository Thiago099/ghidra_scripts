#TODO write a description for this script
#@author
#@category _NEW_
#@keybinding
#@menupath
#@toolbar


from ghidra.program.model.symbol import SourceType
from ghidra.app.script import GhidraScript
from  _common import versions, AddressLibrary

symbol_table = currentProgram.getSymbolTable()

scriptName = "Rename All Known Code Units"

class MyScript(GhidraScript):
    def run(self):
        while(True):
            version = askChoice(scriptName, "Please Select The Game Version:", versions, versions[0])
            library = AddressLibrary(version)
            procceed = askYesNo(scriptName, "Are you using skyrim "+library.getGameVersion()+" with this exact version: "+library.getExactVersion())
            if(not procceed):
                tryagain = askYesNo(scriptName, "Do you want to try again?")
                if tryagain:
                    continue
                return
            procceed = askYesNo(scriptName, "This function will lot of code units, are you sure?")
            if not procceed:
                return
            
            break
        code_units_renamed = 0
        for id in library.GetAllIds():
            address = library.GetMemory(id)
            if(address == "-1"):
                continue
            program_address = currentProgram.getAddressFactory().getAddress(address)
            code_unit = currentProgram.getListing().getCodeUnitAt(program_address)
            data = library.GetAddressData(id)
            if(data == "-1"):
                continue
            if(code_unit is not None):
                if("name" in data):
                    code_units_renamed += 1

                    existing_label = symbol_table.getPrimarySymbol(program_address)
                    if existing_label is not None:
                        symbol_table.removeSymbolSpecial(existing_label)

                    symbol_table.createLabel(program_address, data["name"], SourceType.USER_DEFINED)
            else:
                print("code unit not found at address "+address)

            pass
        print("Done, code units renamed "+str(code_units_renamed))

script = MyScript()
script.run()
