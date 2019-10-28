import sys
from os import path

import numpy as np
import cv2

sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
sys.path.append( path.join(path.dirname( path.dirname( path.abspath(__file__) ) ) , 'components'))

from components.video_manager import VideoManager
from components.sequence_generator import RandomSequenceGenerator

def testGetNextFrame():
	source = "/home/alpha/Documents/research/blob-steg/media/dog.mp4"
	key = b'ZAQkxVlI1UyVVcVARrBT0x1eYNc6qDE61oTGlaaEcXQ='
	vm = VideoManager(source, key)
	assert type(vm.getNextFrame()) == np.ndarray

def testFull():
	source = "/home/alpha/Documents/research/blob-steg/media/dog.mp4"
	key = b'ZAQkxVlI1UyVVcVARrBT0x1eYNc6qDE61oTGlaaEcXQ='
	vm = VideoManager(source, key)
	video = cv2.VideoCapture(source)
	property_id = int(cv2.CAP_PROP_FRAME_COUNT)
	total_frames = int(cv2.VideoCapture.get(video, property_id))
	for i in range(total_frames):
		assert vm.full() == False
		vm.getNextFrame()

	assert vm.full() == True