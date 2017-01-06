import numpy
import scipy.special

# neural network class definition
class neuralNetwork:
    
    
    # initialise the neural network
    def __init__(self, inputNodes, hiddenNodes, outputNodes, learningRate):
        # set number of nodes in each input, hidden, output layer
        self.inputNodes = inputNodes
        self.hiddenNodes = hiddenNodes
        self.outputNodes = outputNodes
        
        #link weights matrices, wih and woh
        #links inside the arrays are Wij
        #the link and associated weight are from node i to node j
        #W11, W22, etc
        #A matrix for the link weights between input and hidden layers; Winput_hidden of size (inputNodes x hiddenNodesnode)
        self.wih = numpy.random.normal(0.0, pow(self.hiddenNodes, -0.5), (self.hiddenNodes, self.inputNodes))
        self.who = numpy.random.normal(0.0, pow(self.outputNodes, -0.5), (self.outputNodes, self.hiddenNodes))

        # learning rate
        self.lr = learningRate
        
        # activation function is the sigmoid function
        self.activationFunction = lambda x: scipy.special.expit(x)
        
        self.display()
        
        pass

    
    # train the neural network
    def train(self, inputsList, targetsList):
        # convert inputs list to 2d array
        inputs = numpy.array(inputsList, ndmin=2).T
        targets = numpy.array(targetsList, ndmin=2).T
        
        # calculate signals into hidden layer
        hiddenInputs = numpy.dot(self.wih, inputs)
        # calculate the signals emerging from hidden layer
        hiddenOutputs = self.activationFunction(hiddenInputs)
        
        # calculate signals into final output layer
        finalInputs = numpy.dot(self.who, hiddenOutputs)
        # calculate the signals emerging from final output layer
        finalOutputs = self.activationFunction(finalInputs)
        
        # output layer error is the (target - actual)
        outputErrors = targets - finalOutputs
        # hidden layer error is the output_errors, split by weights, recombined at hidden nodes
        #propogate error backwards by multiply error matrix by the transpose of the matrices of link weights, who
        hiddenErrors = numpy.dot(self.who.T, outputErrors) 
        
        # update the weights for the links between the hidden and output layers
        self.who += self.lr * numpy.dot((outputErrors * finalOutputs * (1.0 - finalOutputs)), numpy.transpose(hiddenOutputs))
        
        # update the weights for the links between the input and hidden layers
        self.wih += self.lr * numpy.dot((hiddenErrors * hiddenOutputs * (1.0 - hiddenOutputs)), numpy.transpose(inputs))
        
        pass

    
    # query the neural network
    def query(self, inputsList):
        # convert inputs list to 2d array
        inputs = numpy.array(inputsList, ndmin=2).T
        
        # calculate signals into hidden layer
        hiddenInputs = numpy.dot(self.wih, inputs)
        # calculate the signals emerging from hidden layer
        hiddenOutputs = self.activationFunction(hiddenInputs)
        
        # calculate signals into final output layer
        finalInputs = numpy.dot(self.who, hiddenOutputs)
        # calculate the signals emerging from final output layer
        finalOutputs = self.activationFunction(finalInputs)
        
        return finalOutputs
    
    def display(self):
        print ("input Nodes:" + str(self.inputNodes))
        print("hidden Nodes:" + str(self.hiddenNodes))
        print("output Nodes:" + str(self.outputNodes))
        print ("learning factor:" + str(self.lr))
        print(self.wih)
        print(self.who)
        pass
