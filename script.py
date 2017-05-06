import os

currentPath = os.getcwd()
blifFileParentFolder = currentPath+os.sep+"testFiles"
yigFilesParentFolder = currentPath+os.sep+"yFiles"

for blifFile in os.listdir(blifFileParentFolder):
    if(os.path.isfile(os.path.join(blifFileParentFolder,blifFile))):
        writeFile = open('read.txt','w+')
        blifFilePath = blifFileParentFolder+os.sep+blifFile
        writeFile.write("%s\n" % blifFilePath)
        print "--------------------------------"
        print "Process started for : "+blifFile
        logFile = blifFile.split('.blif')
        logFileName = logFile[0]+".txt"
        yigFileName = logFile[0]+".yig"
        yigFilePath = yigFilesParentFolder+os.sep+yigFileName
        writeFile.write("%s" % yigFilePath)
        writeFile.close()

        cmd = "python Main.py > reportGenerated/"+logFileName
        os.system(cmd)
        print "Process ended for : "+blifFile
        print "--------------------------------\n\n"