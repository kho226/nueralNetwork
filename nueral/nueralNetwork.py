import numpy
import scipy.special

class nueralNetwork:
    #nueral network initializer
    def __init__(self, numInputNodes, numHiddenNodes, numOutputNodes, learningFactor):
        self.inputNodes = numInputNodes
        self.hiddenNodes = numHiddenNodes
        self.outputNodes = numOutputNodes

        #learning factor - ⍺
        self.lf = learningFactor

        #link weights, wih and woh
        #links inside the arrays are Wij
        #the link and associated weight are from node i to node j
        #W11, W22, etc
        #A matrix for the link weights between input and hidden layers; Winput_hidden of size (inputNodes x hiddenNodesnode)
        self.wih=(numpy.random.rand(self.hiddenNodes, self.inputNodes)-0.5)
        #A matrix for the link weights between input and hidden layers; Whidden_output of size(hiddenNodes x outputNodes)
        self.woh=(numpy.random.rand(self.outputNodes, self.hiddenNodes)-0.5)

        #more sophisticated weights
        #sample the weights from a normal dist. with mean = 0 and std. deviation = (# of incoming links)^(-1/2)
        #   self.wih = (numpy.random.normal(0.0, pow (self.hiddenNodes, -0.5), self.inputNodes, self.hiddenNodes)
        #self.woh = (numpy.random.normal(0.0, pow(self.hiddenNodes,-0.5), self.hiddenNodes, self.outputNodes)
        #activation function
        self.activationFunction = lambda x : scipy.special.expit(x)
        self.display()
        pass

    #query the data
    def query(self,inputsList):
        inputs = numpy.array(inputsList, ndmin = 2).T
        #send input signals through wih
        hiddenInputs = numpy.dot(self.wih,inputs)
        #apply activation function
        hiddenOutputs = self.activationFunction(hiddenInputs)
        #send signals through woh
        finalInputs = numpy.dot(self.woh,inputs)
        #apply activation function
        finalOutputs = self.activationFunction(finalInputs)
        return finalOutputs


    #train the nueral network
    def train(self):
        pass

    def display(self):
        print ("input Nodes:" + str(self.inputNodes))
        print("hidden Nodes:" + str(self.hiddenNodes))
        print("output Nodes:" + str(self.outputNodes))
        print ("learning factor:" + str(self.lf))
        print(self.wih)
        print(self.woh)
        pass
    
        
