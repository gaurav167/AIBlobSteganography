import cv2

from sequence_generator import RandomSequenceGenerator

class FrameManager:
	"""Responsible for extracting blobs, handling and embedding data in frames."""
	def __init__(self, frame, key):
		self.frame = frame
		self.key = key
		# TODO : find all blobs
		self.total_blobs = 2  # temp
		self.random_sequence = RandomSequenceGenerator(self.key, self.total_blobs).getSequence(self.total_blobs)
		self.next_blob_number_index = 0

	def embed(self, byte):
		# TODO : Add embedding algorithm. Modify original source with data
		self.next_blob_number_index += 1

	def full(self):
		return self.next_blob_number_index == len(self.random_sequence)
		
	def getBlobCount(self):
		return self.total_blobs