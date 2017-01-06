# NeuralNetwork
## A neural network built with the purpose of recognizing handwritten characters.
###### A brief overview...
The concepts that underpin neural Networks are both **mathematical and cognitive in nature.** Mathematical concepts include **elements of linear algebra such as matrix multiplication and the transpose of a matrix, elements of calculus such as the derivative and gradient descent, and elements of algebra such as slope-intercept form** and **cognitive concepts such as a basic understanding of the structure of a neuron.**

Computers are effectively extremely fast calculators, which makes them perfect for carrying out calculations.
Humans brains are technically slower than calculators, yet we are capable of doing things that computers cannot; such as recognizing handwritten characters or even faces.

NeuralNetworks attempt to bridge the gap between the human brain and computers; allowing us to imbue computers with almost human-like cognitive abilities.

The neuron is the most basic building block of intelligent life on earth. Neuron's consist of dendrites, axons and terminals. A dendrite of one neuron will connect to the terminal of another neuron, and within each neuron axons connect dendrites and terminals. Neurons are effectively the circuitry of our brains.

We can model the neurons of a human brain with a matrix of nodes, where each node in the matrix represents a neuron. Take for example a 2 x 2 matrix of nodes. There is a total of 4 nodes. Each node in the first column has a link to every node in the second column. Each of these links has a weight / probability associated with it as well as an activation function. The activation functions and link weights determine how information travels through the matrix.

Information can propagate forward and backward through the matrix of nodes. Propagating information forward is

#TODO...
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
- [x] clean up code in main()
- [ ] format README.md

![Alt text](/screenshots/usage.png?raw=true "Usage")

# [Jupyter / IPython quickstart](http://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/install.html)
> moved development to Jupyter / IPython since the Python IDLE does not support matplotlib interactive updates
