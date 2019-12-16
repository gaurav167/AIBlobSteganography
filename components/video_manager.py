from os import path, sep
import cv2
import numpy as np

from sequence_generator import RandomSequenceGenerator

media_path = r'/home/alpha/Documents/research/blob-steg/media'

class VideoManager:
	"""Responsible for extracting unique and random frame sequence from video"""
	def __init__(self, media_source, key):
		self.media_source = media_source
		self.key = key
		self.video = cv2.VideoCapture(self.media_source)
		self.modified_frames = {}
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

	def getCurrentFrame(self):
		return self.random_frame_sequence[self.next_frame_number_index]

	def write_frame(self, frame_index, frame):
		self.modified_frames[frame_index] = frame

	def generate_video(self):
		from os import sep
		name = self.media_source.split(sep)[-1].split('.')[0]
		extension = '.' + self.media_source.split(sep)[-1].split('.')[1]
		width = int(self.video.get(cv2.CAP_PROP_FRAME_WIDTH))
		height = int(self.video.get(cv2.CAP_PROP_FRAME_HEIGHT))
		fps = int(self.video.get(cv2.CAP_PROP_FPS))
		out = cv2.VideoWriter(path.join(media_path, 'Modified_' + name + extension), cv2.VideoWriter_fourcc('M','J','P','G'), fps, (width, height))
		success, frame = self.video.read()
		success = True
		count = 1
		while success:
			frame = self.modified_frames.get(count, frame)
			out.write(frame)
			count += 1
			success, frame = self.video.read()
		out.release()
