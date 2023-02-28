import numpy as np


def calc_stuff(x):
	y =0
	if isinstance(x, int) or isinstance(x, float):
		for i in range(6):
			y += np.log(np.exp(x+i))
	return y