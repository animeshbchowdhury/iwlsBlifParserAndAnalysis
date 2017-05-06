#from Node import Node
import globalVars

class Gate:
    gateName = None
    inputNodes = None
    outputNode = None
    outputNodeStatus = None
    inputNodeStatus = None
    outputNodeBooleanStatus = None
    literalList = None
    finalLiteralList = None


    def __init__(self,inputNodes,inputNodeStatus,outputNode,outputNodeStatus):
        self.inputNodes = inputNodes
        self.inputNodeStatus = inputNodeStatus
        self.outputNode = outputNode
        self.outputNodeStatus = outputNodeStatus
        self.outputNodeBooleanStatus = ""
        self.primaryLiteralExpression = []
        self.literalList = []
        self.finalLiteralList = []
        lenCount = 0
        '''
        while(lenCount<inputNodeStatus.__len__()):
            elm1 = inputNodes[lenCount]
            elm2 = inputNodeStatus[lenCount]
            #string = "( "+str(elm2)+" * "+elm1.getName()+" )"
            nodeName = elm1.getName()
            if(nodeName in globalVars.dictOfInternalSignalsLogic.keys()):
                primaryLiteralExpression = globalVars.dictOfInternalSignalsLogic[nodeName]
            elif(nodeName in globalVars.dictOfOutputSignalLogic.keys()):
                primaryLiteralExpression = globalVars.dictOfOutputSignalLogic[nodeName]
            else:
                primaryLiteralExpression = nodeName
            if(elm2 == 0):
                string = "(~"+ primaryLiteralExpression + ")"
            else:
                string = "(" + primaryLiteralExpression + ")"
            self.outputNodeBooleanStatus+=string
            lenCount+=1
        if(self.outputNodeStatus == 0):
            updateString = "(~"+self.outputNodeBooleanStatus+")"
            self.outputNodeBooleanStatus = updateString
        '''
        literalList = []
        while(lenCount<inputNodeStatus.__len__()):
            elm1 = inputNodes[lenCount]
            elm2 = inputNodeStatus[lenCount]
            primaryLogicObject = []
            # string = "( "+str(elm2)+" * "+elm1.getName()+" )"
            nodeName = elm1.getName()
            if (nodeName in globalVars.dictOfInternalSignalsLogic.keys()):
                #self.primaryLiteralExpression[:] = []
                #self.primaryLiteralExpression.append(globalVars.dictOfInternalSignalsLogic[nodeName])
                primaryLogicObject.append(globalVars.dictOfInternalSignalsLogic[nodeName])
            elif (nodeName in globalVars.dictOfOutputSignalLogic.keys()):
                #self.primaryLiteralExpression[:] = []
                #self.primaryLiteralExpression.append(globalVars.dictOfOutputSignalLogic[nodeName])
                primaryLogicObject.append(globalVars.dictOfOutputSignalLogic[nodeName])
            else:
                #self.primaryLiteralExpression[:] = []
                #self.primaryLiteralExpression.append(nodeName)
                primaryLogicObject.append(nodeName)

            if (elm2 == 0):
                #string = "(~" + primaryLiteralExpression + ")"
                primaryLogicObject.append(0)
            else:
                #string = "(" + primaryLiteralExpression + ")"
                primaryLogicObject.append(1)
            #self.outputNodeBooleanStatus += string
            #print self.primaryLiteralExpression
            #primaryLogicObject = self.primaryLiteralExpression
            literalList.append(primaryLogicObject)
            #print primaryLogicObject
            #self.primaryLiteralExpression[:] = []
            lenCount += 1

        #print literalList
        self.finalLiteralList.append(literalList)
        if (self.outputNodeStatus == 0):
            #updateString = "(~" + self.outputNodeBooleanStatus + ")"
            #self.outputNodeBooleanStatus = updateString
            self.finalLiteralList.append(0)
        else:
            self.finalLiteralList.append(1)



    def computeBooleanLogicValue(self):
        boolValue = 1
        lenCount = 0
        while (lenCount < self.inputNodeStatus.__len__()):
            elm1 = self.inputNodes[lenCount]
            elm2 = self.inputNodeStatus[lenCount]
            if (elm2 == 0):
                boolValue *= (elm1.computeLogicValue() ^ 1)
            else:
                boolValue *= elm1.computeLogicValue()
            lenCount += 1
        #print self.outputNode.getName(),boolValue
        #print self.outputNodeBooleanStatus
        if(self.outputNodeStatus == 0):
            return boolValue^1
        else:
            return boolValue


    def getOutputNodeBooleanStatus(self):
        return self.outputNodeBooleanStatus

    def getOutputNodeFinalLiteral(self):
        return self.finalLiteralList

    def getInputNodes(self):
        return self.inputNodes

    def getInputNodeStatus(self):
        return self.inputNodeStatus

    def getOutputNode(self):
        return self.outputNode

    def getOutputNodeStatus(self):
        return self.outputNodeStatus