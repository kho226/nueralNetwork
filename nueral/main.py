#! usr/bin/python
from __future__ import print_function
from nueralNetwork import nueralNetwork

def main ():
        print ("Enter the dimensions for your network...")
        print ("As of now the only supported dimension is 3x3.")
        numInputNodes = int(input("Rows: "))
        numHiddenNodes = int(input("Columns: "))
        print ("Enter a learning - factor for your network...")
        learningFactor = input("learning factor: ")
        nueralNet = nueralNetwork(numInputNodes,numHiddenNodes,numInputNodes, learningFactor)
        
    
if __name__ == '__main__':
        main()

