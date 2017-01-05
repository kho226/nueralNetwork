#! usr/bin/python
from __future__ import print_function
from nueralNetwork import nueralNetwork
from pathlib import Path
import matplotlib.pyplot
import numpy

def main ():
       
        print ("Enter the dimensions for your network...")
        print ("As of now the only supported dimension is 3x3.")
        numInputNodes = int(input("Rows: "))
        numHiddenNodes = int(input("Columns: "))
        print ("Enter a learning - factor for your network...")
        learningFactor = input("learning factor: ")
        nueralNet = nueralNetwork(numInputNodes,numHiddenNodes,numInputNodes, learningFactor)
        #grab the training dats
        userInput = input("Enter the file path of your training data:")
        filePath = Path(userInput) 
        print (filePath)
        dataList = []
        if filePath.is_file():
            dataFile = open(userInput, 'r')
            dataList = dataFile.readlines()
            dataFile.close()
        else:
            print (str(filePath) + " does not exist")
        #testing purposes
        #print ("printing out the first value in dataList, the pixel color values associated with the first value, and the length of dataList.")
        #print (dataList[0])
        #print (len(dataList))
        splitVals = dataList[0].split(',')
        #print (splitVals)
        #take all except the first element of the list [1:], effectively ignoring the first label value
        #numpy.asfarray() -> creates a new array of real numbers from an array of text strings
        #reshapex(z,y) -> modifier that transforms an array into an z X y array
        #imageArray = numpy.asfarray(splitVals[1:]).reshape((28,28))
        #matplotlib.pyplot.imshow(imageArray, cmap = "Greys", interpolation = 'None')
        scaledInput = (numpy.asfarray(splitVals[1:]) / 255.00 * 0.99) + 0.01
        print (scaledInput)
        
         
    
if __name__ == '__main__':
        main()

