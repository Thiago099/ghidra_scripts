#TODO write a description for this script
#@author
#@category _NEW_
#@keybinding
#@menupath
#@toolbar


from ghidra.program.model.symbol import SourceType
from ghidra.app.script import GhidraScript
from  _common import AddressLibrary

symbol_table = currentProgram.getSymbolTable()

scriptName = "Rename All Known Code Units"

class MyScript(GhidraScript):
    def run(self):
        delete_existing_symbols = False

        library = AddressLibrary(currentProgram)
        
        if(not library.IsValid()):
            return

        delete_existing_symbols = askYesNo(scriptName, "Do you want to delete existing symbols to the renamed functions?")
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

                    if delete_existing_symbols:
                        existing_label = symbol_table.getPrimarySymbol(program_address)
                        if existing_label is not None:
                            symbol_table.removeSymbolSpecial(existing_label)

                    symbol_table.createLabel(program_address, data["name"], SourceType.USER_DEFINED)

                    code_units_renamed += 1

            else:
                print("code unit not found at address "+address)

            pass
        print("Done, code units renamed "+str(code_units_renamed))

script = MyScript()
script.run()
