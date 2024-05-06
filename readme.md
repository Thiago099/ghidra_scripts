## Address Library scripts or Ghidra

### General

All scripts that interact with the address library will ask for a game version; you should provide it with the correct one for your executable

### Bookmark An Address.py

This script will ask you for an address library ID, it will bookmark the address of that id

### Hook All References to this function.py

This script will print on the console the address library IDs of the function it is in, and the offset, for all references to the selected address. If the selected address is a reference, it will do that for the original address

### Hook This Reference.py

If the selected address is in a function, it will display the address of this function on the Address Library and the offset of where this address is in that function

### Using a specific version of skyrim:

You can generate a dump of your specific version of skyrim by adding this code to any SKSE plugin. You can get the header file [here](https://www.nexusmods.com/skyrimspecialedition/mods/32444?tab=files)

```c++


#include "versiondb.h"

bool DumpSpecificVersion()
{
VersionDb db;

// Try to load database of version 1.5.62.0 regardless of running executable version.
if (!db.Load(1, 5, 62, 0))
{
_FATALERROR("Failed to load database for 1.5.62.0!");
return false;
}

// Write out a file called offsets-1.5.62.0.txt where each line is the ID and offset.
db.Dump("offsets-1.5.62.0.txt");
_MESSAGE("Dumped offsets for 1.5.62.0");
return true;
}
```

After you do that, you can put the file you generated in the data folder of this project

it needs to follow this naming convetion

offsets-`<game-version>`.txt

Finally, you can finally run the only cell on the ipynb file to update the database used by these scripts
