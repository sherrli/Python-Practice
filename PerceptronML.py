# -*- coding: utf-8 -*-
"""
Spyder Editor

Create a Perceptron class with methods to train a Perceptron binary classifier.
Test your classifer on test data.
"""
# in terminal, >> spyder3

class Perceptron:
    # class fields
    # weights = []
    
    # constructor
    def __init__(self, dim):
        # initialize weights to 1
        self.weights = [1]*dim
        print("weights initialized" + str(self.weights))
        # learning rate tells us how much we want to steer our weight towards the actual label
        # A higher learning rate could lead to oversteering
        self.learning_rate = 0.1
    
    # class helper function to return sign of a constant
    def sign(self, val):
        if val>=0:
            return 1
        else: #val<0
            return -1
    
    # class algorithm
    # instance is the train instance as a feature vector
    # self.weights has the weight of each feature
    def predict(self, instance):
        sum = 0
        for i in range(0, len(self.weights)):
            sum += instance[i] * self.weights[i]
        output = self.sign(sum)
        return output
    
    # class function to modify class variable values
    def train(self, input, actual):
        prediction = self.predict(input)
        error = actual - prediction # error is 0 if prediction was correct
        for i in range(len(self.weights)):
            self.weights[i] += error * input[i] # updates upon error!
    
def main():
    p = Perceptron(5)
    train_input = [1, 2, 3, -10, 3] # input vector
    train_label = 1
    print("before training")
    print(p.predict(train_input))
    p.train(train_input, train_label)
    print("after training")
    print(p.predict(train_input)) # run perceptron alg on inputs vector
    
    
main()
