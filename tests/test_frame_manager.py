import sys
from os import path

import numpy as np
import cv2

sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
sys.path.append( path.join(path.dirname( path.dirname( path.abspath(__file__) ) ) , 'components'))

from components.frame_manager import FrameManager
from components.sequence_generator import RandomSequenceGenerator

def testEmbed():
	frame = np.ones((100, 100, 3))
	key = b'ZAQkxVlI1UyVVcVARrBT0x1eYNc6qDE61oTGlaaEcXQ='
	byte = b'a'
	fm = FrameManager(frame, key)
	fm.embed(byte)

def testFull():
	frame = np.ones((100, 100, 3))
	key = b'ZAQkxVlI1UyVVcVARrBT0x1eYNc6qDE61oTGlaaEcXQ='
	byte = b'a'
	fm = FrameManager(frame, key)
	total_blobs = fm.getBlobCount()
	for i in range(total_blobs):
		assert fm.full() == False
		fm.embed(byte)

	assert fm.full() == True

def testGetBlobCount():
	frame = np.ones((100, 100, 3))
	key = b'ZAQkxVlI1UyVVcVARrBT0x1eYNc6qDE61oTGlaaEcXQ='
	fm = FrameManager(frame, key)
	assert type(fm.getBlobCount()) == int and fm.getBlobCount() >= 0