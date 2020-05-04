# McCulloch–Pitts Single Layer Perceptron Model

"""
This script is model of the basic single layer perceptron.
In this model is the very beginning of the decision making for computers.
"""

"""
Step 1 = Create inputs
Step 2 = Create weigths
Step 3 = Multiply and sum the values
Step 4 = Insert the values into the 'Sigmoid Function'.

If the value is bigger than 0 it will classified as 1
else, classified as 0.
"""

import random
import numpy

class Perceptron(object):

	def create_inputs(self, number_of_inputs):
		input_list = []
		for _ in range(number_of_inputs):
			number = random.uniform(-1, 1)
			input_list.append(number)
		return input_list

	def create_weights(self, number_of_weights):
		weights_list = []
		for _ in range(number_of_weights):
			weigth = random.uniform(0, 1)
			weights_list.append(weigth)
		return weights_list

	def sigmoid(self, value):
		# 'e' value is the constant for the sigmoid function
		e = 2.718281828459045
		sigmoid = 1 / (1 + e ** value)
		return sigmoid

	def epoch(self, inputs, weigths):
		val = True
		threshold = 0.5
		sum_of_arrays = 0
		for inp in inputs:
			for w in weigths:
				sum_of_arrays += inp * w
		value = self.sigmoid(sum_of_arrays)
		print(f'OUTPUT: {round(value, 5)}')
		if value > threshold:
			print('-->', 1)
		else:
			print('-->', 0)


num_of_elements = 5

ins = Perceptron()
inputs = ins.create_inputs(num_of_elements)
weigths = ins.create_weights(num_of_elements)
print('INPUT:', inputs)
ins.epoch(inputs, weigths)