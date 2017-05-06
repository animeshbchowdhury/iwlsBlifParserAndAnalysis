import os
import re
import globalVars
from Node import Node
from Gate import Gate
import math
import time


def setInputs():
    globalVars.flagStatus = 1
    return

def setOutputs():
    globalVars.flagStatus = 2
    return

def setLogic():
    globalVars.flagStatus = 3
    return

dictOfParseFunctions = {
    '.inputs' : setInputs,
    '.outputs': setOutputs,
    '.names': setLogic
}


def setFlag(keyVal):
    if keyVal in dictOfParseFunctions.keys():
        dictOfParseFunctions[keyVal]()


def processInputs(word):
    #print word
    if (word[0]!= '.inputs'):
        startPos = 0
    else:
        startPos = 1

    for inp in word[startPos:]:
        nodeObj = Node(inp,True,False)
        globalVars.dictOfInputs[inp] = nodeObj

def processOutputs(word):
    #print word
    if (word[0]!= '.outputs'):
        startPos = 0
    else:
        startPos = 1

    for out in word[startPos:]:
        nodeObj = Node(out,False,True)
        globalVars.dictOfOutputs[out] = nodeObj

def processLogic(word,word2):
    #print word,word2
    if(len(word)==4):
        inputNode1 = word[1]
        inputNode2 = word[2]
        outputNode = word[3]
        nodeObj1 = None
        nodeObj2 = None
        nodeObj3 = None
        if inputNode1 not in globalVars.dictOfInputs.keys():
            if inputNode1 not in globalVars.dictOfInternalSignals.keys():
                nodeObj1 = Node(inputNode1,False,False)
                globalVars.dictOfInternalSignals[inputNode1] = nodeObj1
            else:
                nodeObj1 = globalVars.dictOfInternalSignals[inputNode1]
        else:
            nodeObj1 = globalVars.dictOfInputs[inputNode1]

        if inputNode2 not in globalVars.dictOfInputs.keys():
            if inputNode2 not in globalVars.dictOfInternalSignals.keys():
                nodeObj2 = Node(inputNode1,False,False)
                globalVars.dictOfInternalSignals[inputNode2] = nodeObj2
            else:
                nodeObj2 = globalVars.dictOfInternalSignals[inputNode2]
        else:
            nodeObj2 = globalVars.dictOfInputs[inputNode2]

        if outputNode not in globalVars.dictOfOutputs.keys():
            if outputNode not in globalVars.dictOfInternalSignals.keys():
                nodeObj3 = Node(outputNode,False,False)
                globalVars.dictOfInternalSignals[outputNode] = nodeObj3
            else:
                nodeObj3 = globalVars.dictOfInternalSignals[outputNode]
        else:
            nodeObj3 = globalVars.dictOfOutputs[outputNode]


        inpLogicStatus = word2[0]
        outLogicStatus = int(word2[1])
        inputNodeLogicStatus = []
        for elm in inpLogicStatus:
            inputNodeLogicStatus.append(int(elm))


        gateObj = Gate([nodeObj1,nodeObj2],inputNodeLogicStatus,nodeObj3,outLogicStatus)
        nodeObj3.assignParentGate(gateObj)
        globalVars.gateCount+=1
        gateName = "gate_"+str(globalVars.gateCount)
        nodeObj1.addSuccessorGate(inputNodeLogicStatus[0],gateObj,gateName)
        nodeObj2.addSuccessorGate(inputNodeLogicStatus[1],gateObj,gateName)



startTime = time.time()
readFileLoc = open('read.txt','r+')
lines = readFileLoc.readlines()
line = lines[0].split('\n')[0]
writeLine = lines[1]
readFile = open(line,'r+')
linesOfBlifFile = readFile.readlines()[1:-1]
totalLine = len(linesOfBlifFile)
counter = 0

while(counter<totalLine):
    line = linesOfBlifFile[counter]
    word = re.findall('[]a-zA-Z0-9.[]+',line)
    setFlag(word[0])
    if(globalVars.flagStatus == 1):
        processInputs(word)
    elif(globalVars.flagStatus == 2):
        processOutputs(word)
    elif(globalVars.flagStatus == 3):
        line2 = linesOfBlifFile[counter+1]
        word2 = re.findall('[]a-zA-Z0-9.[]+',line2)
        processLogic(word,word2)
        counter+=1
    counter+=1

print "\n\n##### INPUT SIGNALS ####\n\n"
for element in globalVars.dictOfInputs.keys():
    print element


print "\n\n#### INTERNAL SIGNALS ####\n\n"
for element in globalVars.dictOfInternalSignals.keys():
    #parentGateElement = globalVars.dictOfInternalSignals[element].getParentGate()
    #print element,parentGateElement.getOutputNodeBooleanStatus()
    print element

'''
writeFile = open(writeLine,'w+')

for element in globalVars.dictOfOutputs.keys():
    writeFile.write(element)
    #print element
    writeFile.write("\n\n")
    writeFile.write(str(globalVars.dictOfOutputSignalLogic[element]))
    writeFile.write("---------------\n")
'''

print "\n\n##### OUTPUT SIGNALS ####\n\n"
for element in globalVars.dictOfOutputs.keys():
    print "\n---------------"
    print element
    print "\n\n"
    print globalVars.dictOfOutputSignalLogic[element]
    print "---------------\n"


'''
inpNodes = []
outNodes = []

for element in globalVars.dictOfInputs.keys():
    inpNodes.append(globalVars.dictOfInputs[element])


for element in globalVars.dictOfOutputs.keys():
    outNodes.append(globalVars.dictOfOutputs[element])
'''

'''
inpNodes[0].setLogicValue(0)
inpNodes[1].setLogicValue(1)
inpNodes[2].setLogicValue(1)
'''


'''
print "\n\n##### RESULT #####"
lenOfSeq = int(math.pow(2,inpNodes.__len__()))-1
print lenOfSeq


while(lenOfSeq>=0):
    binValueFormatString = '{0:0'+str(inpNodes.__len__())+'b}'
    #binValue = '{0:03b}'.format(lenOfSeq)
    binValue = binValueFormatString.format(lenOfSeq)
    lenOfBinSeq=len(binValue)-1
    print lenOfBinSeq
    print inpNodes.__len__()
    print binValue
    while(lenOfBinSeq>=0):
        vectorInp = int(binValue[lenOfBinSeq])
        inpNodeInstance = inpNodes[lenOfBinSeq]
        inpNodeInstance.setLogicValue(vectorInp)
        lenOfBinSeq-=1

    print "\n\n------------------"
    print "Input Output Vector\n------------------"
    print binValue

    for element in inpNodes:
        buffer = element.getName()+" = "+str(element.computeLogicValue())
        print buffer

    print "------------------"
    for element in outNodes:
        buffer = element.getName()+" = "+str(element.computeLogicValue())
        print buffer

    print "------------------"
    print "------------------\n\n"

    lenOfSeq -= 1
'''


'''

# BACKTRACING ALGORITHM for FAN-IN Analysis of PIs
for element in outNodes:
    nodeAlreadyExplored = []
    nodeToBeExplored = [element]
    listOfPI = []
    while(len(nodeToBeExplored)>0):
        stackElement = nodeToBeExplored.pop(0)
        parentGate = stackElement.getParentGate()
        drivingNodes = parentGate.getInputNodes()
        for elementNode in drivingNodes:
            if(elementNode.getNodeType() == "PI"):
                if(elementNode not in listOfPI):
                    listOfPI.append(elementNode)
            else:
                if(elementNode not in nodeAlreadyExplored):
                    if(elementNode not in nodeToBeExplored):
                        nodeToBeExplored.append(elementNode)
        nodeAlreadyExplored.append(stackElement)

    element.setPIListOfFanInCone(listOfPI)



print "\n\n ######### FAN IN CONE Analysis ###########\n\n"

for element in outNodes:
    listOfPI = element.listOfPIInFanInCone
    print "--------------"
    print "PRIMARY OUTPUT :",element.getName()
    print "PIs in FanIn Cone :"
    for elementNode in listOfPI:
        print elementNode.getName()
    print "------------------"
    print "------------------\n\n"
'''

endTime = time.time()
print "\n\nTime Taken :"+str(endTime-startTime)+" seconds"
'''

yLogicInternalNodesExplored = []
logicGateAssignments = []

for outNodeElement in outNodes:
    nodeToBeExplored = [outNodeElement]
    logicGateAssignmentsOfPO = []
    while(len(nodeToBeExplored)>0):
        stackElement = nodeToBeExplored.pop(0)
        parentGate = stackElement.getParentGate()
        drivingNodes = parentGate.getInputNodes()
        drivingNodesStatus = parentGate.getInputNodeStatus()
        stackElementStatus = parentGate.getOutputNodeStatus()
        if(stackElementStatus == 0):
            strAssign = stackElement.getName()+" = Y2( "
            lenCount = 0
            while (lenCount < drivingNodesStatus.__len__()):
                elm1 = drivingNodes[lenCount]
                elm2 = drivingNodesStatus[lenCount]
                if(elm2 == 0):
                    strAssign+=(elm1.getName()+", ")
                else:
                    strAssign+=("~"+elm1.getName()+" ,")
                lenCount+=1
            strAssign+=("1)")
        else:
            strAssign = stackElement.getName() + " = Y2( "
            lenCount = 0
            while (lenCount < drivingNodesStatus.__len__()):
                elm1 = drivingNodes[lenCount]
                elm2 = drivingNodesStatus[lenCount]
                if (elm2 == 1):
                    strAssign += (elm1.getName() + ", ")
                else:
                    strAssign += ("~" + elm1.getName() + " ,")
                lenCount += 1
            strAssign += ("0)")
        yLogicInternalNodesExplored.append(stackElement)
        logicGateAssignmentsOfPO.append(strAssign)
        for inNode in drivingNodes:
            if(inNode.getNodeType()!="PI"):
                if(inNode not in yLogicInternalNodesExplored):
                    print inNode.getName()
                    nodeToBeExplored.append(inNode)

    for elm in logicGateAssignmentsOfPO[::-1]:
        logicGateAssignments.append(elm)


for elm in logicGateAssignments:
    print elm

noOfInps = inpNodes.__len__()
noOfOuts = outNodes.__len__()
noOfInternalSignals = yLogicInternalNodesExplored.__len__() - noOfOuts


writeFile = open(writeLine,'w+')
writeFile.write('.i %d\n' % noOfInps)
writeFile.write('.o %d\n' % noOfOuts)
writeFile.write('.w %d\n' % noOfInternalSignals)
for elm in logicGateAssignments:
    writeFile.write('%s\n' % elm)
writeFile.write('.e\n')


'''