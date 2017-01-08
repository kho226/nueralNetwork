# NeuralNetwork
## A neural network built with the purpose of recognizing handwritten characters.
###### A brief overview...
The concepts that underpin neural Networks are both **mathematical and cognitive in nature.** Mathematical concepts include **elements of linear algebra such as matrix multiplication and the transpose of a matrix, elements of calculus such as the derivative and gradient descent, elements of statistics such as the normal distribution and the standard deviation, and elements of algebra such as slope-intercept form** and **cognitive concepts such as a basic understanding of the structure of a neuron.**

Computers are effectively extremely fast calculators, which makes them perfect for carrying out calculations.
Humans brains are technically slower than calculators, yet we are capable of doing things that computers cannot; such as recognizing handwritten characters or even faces.

NeuralNetworks attempt to bridge the gap between the human brain and computers; allowing us to imbue computers with almost human-like cognitive abilities. Such as the ability to effectively teach itself.

The neuron is the most basic building block of intelligent life on earth. Neuron's consist of **dendrites, axons and terminals.** A dendrite of one neuron will connect to the terminal of another neuron, and within each neuron axons connect dendrites and terminals. Neurons are effectively the circuitry of our brains. They take an electrical signal as input and output another electrical signal. The output of a neuron does not share a linear relationship with it's input. Instead, a neuron will suppress it's output until the input crosses a threshold. An **activation function** is a function that takes an input signal and generates and output signal, but takes into account some threshold. I will be using the **Sigmoid function** or **logistic function** but there are many other candidates to use for the **activation function**.

We can model the neurons of a human brain with a matrix of nodes, where each node in the matrix represents a neuron. Take for example a 2 x 2 matrix of nodes. There are a total of 4 nodes. Each node in the first column has a link to every node in the second column. Each of these **links have an associated weight / probability** as well as an **activation function**. The activation functions and link weights determine how information travels through the matrix.

Information can **propagate forward** and **propagate backward** through the matrix of nodes.

Propagating information forward is carried out by applying the **activation function** to the **dot product** of the **input matrix** and the matrix representing the link weights between the **input layer** and the **hidden layer**. Repeating this algorithm for every matrix of link weights in the network. The resulting matrix we will refer to as the **output Matrix**

Propagating information backwards is carried out in a similar fashion as propagating information forward. Take the **dot product** of the **transpose of the matrix of respective link weights** and the **error matrix**. The **error matrix** is the difference between the **output Matrix** and the **matrix of expected values**.

***A neural network can learn.***

A neural network learns by **adjusting the weights associated with the links**. Link weights are adjusted using **gradient descent**. 

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
