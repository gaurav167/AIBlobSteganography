import random

class RandomSequenceGenerator:
	"""Generates sequence of numbers based on range and key"""

	# Mersenne Twister pseudo-random sequence generator
	rng = random
	max_range = 0

	def __init__(self, key, max_range):
		self.key = key
		self.max_range = max_range
		self.rng.seed(key)

	def getNext(self):
		return self.rng.randint(1, self.max_range + 1)

	def getSequence(self, sequence_length):
		return self.rng.sample(range(1, self.max_range + 1), sequence_length)

	def shuffle(self, sequence):
		_ = sequence.copy()
		self.rng.shuffle(_)
		return _