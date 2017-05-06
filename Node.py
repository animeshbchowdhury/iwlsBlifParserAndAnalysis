#from Gate import Gate
import globalVars

class Node:
    nodeName = None
    isPI = None
    isPO = None
    parentGate = None
    successorGates = None
    noOfFanout = None
    nodeLogicValue = None
    listOfPIInFanInCone = None
    outputLogicFunction = None


    def __init__(self,nodeName,isPI,isPO):
        self.nodeName = nodeName
        self.isPI = isPI
        self.isPO = isPO
        self.successorGates = {}
        self.noOfFanout = 0
        self.nodeLogicValue = None
        self.outputLogicFunction = None

    def assignParentGate(self,parentGateObj):
        self.parentGate = parentGateObj
        '''
        if(self.isPI == False):
            self.outputLogicFunction = self.parentGate.getOutputNodeBooleanStatus()
            if(self.isPO == False):
                globalVars.dictOfInternalSignalsLogic[self.nodeName] = self.outputLogicFunction
            else:
                globalVars.dictOfOutputSignalLogic[self.nodeName] = self.outputLogicFunction
        '''
        if(self.isPI == False):
            self.outputLogicFunction = self.parentGate.getOutputNodeFinalLiteral()
            if(self.isPO == False):
                globalVars.dictOfInternalSignalsLogic[self.nodeName] = self.outputLogicFunction
            else:
                globalVars.dictOfOutputSignalLogic[self.nodeName] = self.outputLogicFunction


    def addSuccessorGate(self,gateDrivingLogic,gateObj,gateName):
        self.successorGates[gateName] = [gateDrivingLogic,gateObj]
        self.noOfFanout+=1

    def getFanoutGates(self):
        return self.successorGates

    def getParentGate(self):
        return self.parentGate

    def setLogicValue(self,nodeLogicValue):
        self.nodeLogicValue = nodeLogicValue

    def computeLogicValue(self):
        if(self.isPI == False and self.nodeLogicValue == None): # None, in order to not recompute, if already computed for that node.
                gateObj = self.parentGate
                self.nodeLogicValue = gateObj.computeBooleanLogicValue()
                return self.nodeLogicValue
        else:
            return self.nodeLogicValue

    def getName(self):
        return self.nodeName

    def getNodeType(self):
        if(self.isPI == True):
            return "PI"
        elif(self.isPO == True):
            return "PO"
        else:
            return "InternalSig"

    def setPIListOfFanInCone(self,list):
        self.listOfPIInFanInCone = list

    def getPIListOfFanInCone(self):
        return self.listOfPIInFanInCone

    def getOutputLogicFunction(self):
        return self.outputLogicFunction