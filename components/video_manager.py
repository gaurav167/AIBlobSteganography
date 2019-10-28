import cv2
import numpy as np

from sequence_generator import RandomSequenceGenerator

class VideoManager:
	"""Responsible for extracting unique and random frame sequence from video"""
	def __init__(self, media_source, key):
		self.media_source = media_source
		self.key = key
		self.video = cv2.VideoCapture(self.media_source)
		property_id = int(cv2.CAP_PROP_FRAME_COUNT)
		self.total_frames = int(cv2.VideoCapture.get(self.video, property_id))
		self.random_frame_sequence = RandomSequenceGenerator(self.key, self.total_frames).getSequence(self.total_frames)
		self.next_frame_number_index = 0
		
	def getNextFrame(self):
		try:
			self.video.set(cv2.CAP_PROP_POS_FRAMES, self.random_frame_sequence[self.next_frame_number_index] - 1)
			self.next_frame_number_index += 1
			_, frame = self.video.read()
		except:
			return np.ones((1,1,1)) * -1
		return frame

	def full(self):
		return self.next_frame_number_index == len(self.random_frame_sequence)
