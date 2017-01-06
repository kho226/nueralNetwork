#! usr/bin/python
from __future__ import print_function
from nueralNetwork import nueralNetwork
from pathlib import Path
import matplotlib.pyplot
import numpy

def main ():
        
       #initialize the network
        print ("Enter the dimensions for your network...")
        numInputNodes = int(input("Rows: "))
        numHiddenNodes = int(input("Columns: "))
        print ("Enter a learning - factor for your network...")
        learningFactor = input("learning factor: ")
        nueralNet = nueralNetwork(numInputNodes,numHiddenNodes,numInputNodes, learningFactor)
        
        #grab the training data
        userInput = input("Enter the file path of your training data:")
        filePath = Path(userInput) 
        print (filePath)
        dataList = []
        
        #verify the file
        if filePath.is_file():
            dataFile = open(userInput, 'r')
            dataList = dataFile.readlines()
            dataFile.close()
        else:
            print (str(filePath) + " does not exist")
            
        #train the network
        epochs = 5
        for e in range (epochs):
                for record in dataList:
                        #split the record by commas
                        splitVals = record.split(',')
                        #scale and shift the inputs
                        scaledInputs = (numpy.asfarray(splitVals[1:]) / 255.0 * 0.99) + 0.01
                        #create the target output values (all 0.01, except the desired label which is 0.99)
                        targets = numpy.zeros(output_nodes) + 0.01
                        targets[int(splitVals[0])] = 0.99
                        nueralNet.train(scaledInputs,targets)
                pass
        pass

        #get the test data
        testDataList = []               
        userInput = input("Enter the file path of your training data:")
        filePath = Path(userInput) 
        print (filePath)
        if filePath.is_file():
                dataFile = open(userInput, 'r')
                testDataList = dataFile.readlines()
                dataFile.close()
        else:
                print (str(filePath) + "does not exist")
                
        #test the nueral network
        #scorecard for perforamance of neural network
        # go through all the records in the test data set
        for record in testDataList:
            # split the record by the ',' commas
            allValues = record.split(',')
            # correct answer is first value
            correctLabel = int(allValues[0])
            # scale and shift the inputs
            inputs = (numpy.asfarray(allValues[1:]) / 255.0 * 0.99) + 0.01
            # query the network
            outputs = nueral.query(inputs)
            # the index of the highest value corresponds to the label
            label = numpy.argmax(outputs)
            # append correct or incorrect to list
                if (label == correctLabel):
                # network's answer matches correct answer, add 1 to scorecard
                scorecard.append(1)
            else:
                # network's answer doesn't match correct answer, add 0 to scorecard
                scorecard.append(0)
                pass
        pass

        # calculate the performance score, the fraction of correct answers
        scorecardArray = numpy.asarray(scorecard)
        print ("performance = ", scorecardArray.sum() / scorecardArray.size)

 if __name__ == '__main__':
        main()

