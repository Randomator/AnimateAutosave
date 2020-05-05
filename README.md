# Adobe Animate Autosave Log

Instead of relying on an _RECOVER file, keep a log of all saves to .fla file.

## Getting Started

To use this app, you must first need to have a set directory where you .fla script(s) are stored. Keep in mind, even if only one script is open, all scripts will be backed up. You must also have a set location where you want AUTOSAVE files to be stored.

### Prerequisites

You will need up to date python3 with os, time, and datetime modules.

```
Give examples
```

### Installing

To install change autoSave.path and savesLocation.path to the path you would like to read and write from. 

For example:

If I were to want to save .fla files from 
```
C:\Users\YOURNAME\Desktop\Video\
```
I would paste that into autoSave.path (you can open with TEXTEDIT and paste path)

Remember to inclue the "\" in the end of the path


Same goes for where you would want to save the autosave files.

Put the path of the save location in savesLocation.path


###Changing save time
By default, this program will save every 5 minutes, but if you would like to change it, you can easily change variable LOOPTIME in main.py. Open main.py with a text editor of your choice and change LOOPTIME to the ammount of seconds in between each autosave.


## Author

* **Random Animator**  - An unexperienced noob at programing