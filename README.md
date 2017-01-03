# nueralNetwork
## A nueral network built with the purpose of recognizing handwritten letters.
###### An example initialization of the nueralNetwork...
- inputNodes = 3
- hiddenLayerNodes = 3
- outputNodes = 3
- learningFactor = 0.1
- nueralNetwork = nueralNetwork(inputNodes, hiddenLayerNodes, outputNodes, learningFactor)
- [x] write skeleton of class
- [x] wrote display function for testing purposes
- [x] add numpy to package
- [x] updated initializer to create matrices of link weights
- [x] updated initializer to randomly select link weights based off of the normal distribution with mean = 0 and standard deviation = (# of incoming links to a node)^(-1/2)
- [x] add scipy to the package
- [x] write query method
- [x] write train method
- [x] updated GUI
- [x] added main function
## usage...
###### text in bold represents your own input
- Rows: ***3***
- Columns: ***3***
- Enter a learning - factor for your network...
- learning factor: ***0.3***
- input Nodes:3
- hidden Nodes:3
- output Nodes:3
- learning factor:0.3
- [[-0.35913703 -0.28463042 -0.43497972]
-  [-0.09382639 -0.08885616  0.34644719]
- [-0.39197225 -0.07319985 -0.47155144]]
- [[ 0.30015968 -0.37006166 -0.14607813]
- [ 0.45860297  0.05808311  0.19152052]
-  [-0.39386964  0.45022823 -0.00251951]]
