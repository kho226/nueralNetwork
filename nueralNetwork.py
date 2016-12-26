class nueralNetwork:
    #nueral network initializer
    def __init__(self, numInputNodes, numHiddenNodes, numOutputNodes, learningFactor):
        self.inputNodes = numInputNodes
        self.hiddenNodes = numHiddenNodes
        self.outputNodes = numOutputNodes

        #learning factor - ⍺
        self.lf = learningFactor
        self.display()
        pass

    #query the data
    def query(self):
        pass

    #train the nueral network
    def train(self):
        pass

    def display(self):
        print ("input Nodes:" + str(self.inputNodes))
        print("hidden Nodes:" + str(self.hiddenNodes))
        print("output Nodes:" + str(self.outputNodes))
        print ("learning factor:" + str(self.lf))
        pass
    
        
