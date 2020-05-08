# McCulloch–Pitts Single Layer Perceptron Model

"""
This script is model of the basic single layer perceptron.
This is a very beginning of the decision making for computers.
"""

"""
Step 1 = Create inputs --> random for this example (between -1 and 1)
Step 2 = Create weigths --> random for this example (between 0 and 1)
Step 3 = Multiply the arrays of inputs and weights
Step 4 = Get the sum of these values
Step 5 = Insert the values into Threshold value

If the value is bigger than threshold (for this example, threshold is 0) it will returns 1
else, returns 0.
"""

import random

class Perceptron(object):

	def create_inputs(self, number_of_inputs):
		input_list = [random.uniform(-1, 1) for _ in range(number_of_inputs)]
		return input_list

	def create_weights(self, number_of_weights):
		weights_list = [random.uniform(0, 1) for _ in range(number_of_weights)]
		return weights_list

	def epoch(self, inputs, weigths):
		self.inputs = inputs
		self.weights = weights
		val = True
		threshold = 0
		sum_of_arrays = 0
		for i in range(len(self.inputs)):
			sum_of_arrays += self.inputs[i] * self.weights[i] 
		print(f'OUTPUT: {round(sum_of_arrays, 5)}')
		if sum_of_arrays > threshold:
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
