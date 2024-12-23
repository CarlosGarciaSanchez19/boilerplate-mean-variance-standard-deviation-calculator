import numpy as np

def create_output(matrix):
	dictionary = {
		'mean': [list(np.mean(matrix, axis=0)), list(np.mean(matrix, axis=1)), np.mean(matrix)],
		'variance': [list(np.var(matrix, axis=0)), list(np.var(matrix, axis=1)), np.var(matrix)],
		'standard deviation': [list(np.std(matrix, axis=0)), list(np.std(matrix, axis=1)), np.std(matrix)],
		'max' : [list(np.max(matrix, axis=0)), list(np.max(matrix, axis=1)), np.max(matrix)],
		'min' : [list(np.min(matrix, axis=0)), list(np.min(matrix, axis=1)), np.min(matrix)],
		'sum' : [list(np.sum(matrix, axis=0)), list(np.sum(matrix, axis=1)), np.sum(matrix)]
	}
	return dictionary

def calculate(list):
	if len(list) != 9:
		raise ValueError("List must contain nine numbers.")
	matrix = np.ones((3, 3))
	matrix[0, :] = list[:3]
	matrix[1, :] = list[3:6]
	matrix[2, :] = list[6:9]
	return create_output(matrix)