# McCulloch–Pitts Single Layer Perceptron Model

"""
This script is modelling of the basic single layer perceptron.
This is the a very beginning of the decision making for computers.
"""

"""
Step 1 = Create inputs --> random for this example (between -1 and 1)
Step 2 = Create weigths --> random for this example (between 0 and 1)
Step 3 = Multiply the arrays of inputs and weights
Step 4 = Get the sum of these values
Step 5 = Insert the values into the 'Sigmoid Function'.
Sigmoid Function = 1 / (1 + e ** value)

After the sigmoid function:
If the value is bigger than threshold (for this example, threshold is 0) it will returns 1
else, returns 0.
"""

import random

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
		threshold = 0
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
# This part of script returns an output of the model, single value, 0 or 1.
