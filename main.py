#INSERT PATH OF DIRECTORY YOU WANT TO AUTO SAVE IN autoSave.path. With \ at end. No quotations
LOOPTIME = 60 #Time of each loop


import os
import time
from datetime import datetime
class GeneralProgramError(Exception):
    pass
while True:
    #Saves Files to variables
    TASKLIST, savePath, storagePath = "", "", ""
    os.system("TASKLIST > tasklist.info")
    with open("tasklist.info") as TASKLIST_file:
        TASKLIST = TASKLIST_file.read().strip()
    os.system("del /Q tasklist.info")
    with open("autoSave.path") as savePath_file:
        savePath = savePath_file.read().strip()
    savePath = "\"" + savePath + "\""
    with open("savesLocation.path") as storagePath_file:
        storagePath = storagePath_file.read().strip()
    #Cheks if Adobe Animate is running
    previousAnimate = True
    if not ("Animate.exe" in TASKLIST):
        if previousAnimate:
            previousAnimate = False
        del TASKLIST
    else:
        previousAnimate = True
        #Clear memory of TASKLIST
        del TASKLIST
        os.system("dir /B {path} | findstr /R /C:\".fla\" > fileList.txt".format(path=savePath))
        files = []
        with open("fileList.txt") as FileList:
            files = FileList.read().splitlines()
        os.system("del /Q fileList.txt")
        if "File Not Found" in files:
            raise GeneralProgramError("FLA file(s) not found")
            exit()
        else:
            savePathFilename = savePath.strip('"')
            os.system(f"copy {savePath}*.* \"{storagePath}\" > foo")
            for file in files:
                nowtime = str(datetime.now()).replace(" ", "_").replace(":", "-")
                newFilename = "{time}{name}".format(time=nowtime,name=file)
                del nowtime
                newFilename = newFilename.strip(" ")
                os.system(f"ren \"{storagePath}{file}\" {newFilename}.autosave")
                del newFilename
            del files
    os.system("del /Q foo ")
    time.sleep(LOOPTIME)
