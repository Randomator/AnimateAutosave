# Adobe Animate Autosave Log

Instead of relying on an _RECOVER file, keep a log of all saves to .fla file.

## Getting Started

Works on windows only.

To use this app, you must first need to have a set directory where your .fla script(s) are stored. Even if only one script is open, all scripts in this directory will be backed up. You must also have a set location where you want your autosave files to be stored.

### Prerequisites

You will need up to date python3 with os, time, and datetime modules.

You can check this with
```
python3 --version
```

If you dont have python at all, you can download it here: https://www.python.org/downloads/


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

## About

Every 5 minutes (or set time) this program will copy the files in specified directory and move them to the savesLocation directory. The files will then be named their exact time + origional filename. 

File main.fla will look something like
```
2020-05-05_14-06-06.804226main.fla
```

This program will never delete any autosaves, so you will manualy have to remove old saves that are no longer needed.

## Changing save time

By default, this program will save every 5 minutes, but if you would like to change it, you can easily change variable LOOPTIME in main.py. Open main.py with a text editor of your choice and change LOOPTIME to the ammount of seconds in between each autosave.


## Author

* **Random Animator**  - An unexperienced noob at programing
