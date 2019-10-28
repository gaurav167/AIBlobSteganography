import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from components.sequence_generator import RandomSequenceGenerator

def testRSGGetNext():
	max_range = 100
	key = "key"
	rsg = RandomSequenceGenerator(key, max_range)
	_next = rsg.getNext()
	assert _next <= max_range and _next > 0

def testRSGGetSequence():
	max_range = 100
	key = "key"
	sequence_length = 5
	rsg = RandomSequenceGenerator(key, max_range)
	sequence = rsg.getSequence(sequence_length)
	assert len(set(sequence)) == sequence_length

def testRSGShuffle():
	max_range = 100
	key = "key"
	sequence_length = 5
	rsg = RandomSequenceGenerator(key, max_range)
	sequence = rsg.getSequence(sequence_length)
	shuffled_sequence = rsg.shuffle(sequence)
	assert len(sequence) == len(shuffled_sequence) and set(sequence) == set(shuffled_sequence)

