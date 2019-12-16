from os import path, sep
import cv2
import numpy as np
import random

from sequence_generator import RandomSequenceGenerator

media_path = r'/home/alpha/Documents/research/blob-steg/media'


class FrameManager:
	"""Responsible for extracting blobs, handling and embedding data in frames."""
	def __init__(self, frame, key):
		self.frame = frame
		self.key = key
		self.extract_blobs()
		self.total_blobs = len(self.keypoints)
		self.random_sequence = RandomSequenceGenerator(self.key, self.total_blobs).getSequence(self.total_blobs)
		self.next_blob_number_index = 0

		# Uncomment for testing
		# print(self.random_sequence)
		# self.save_frame("before")
		# self.display_blobs()

	def extract_blobs(self):
		# Setup SimpleBlobDetector parameters.
		params = cv2.SimpleBlobDetector_Params()
		# Change thresholds
		params.minThreshold = 10;
		params.maxThreshold = 200;
		# Filter by Area.
		params.filterByArea = True
		params.minArea = 50
		# Filter by Circularity
		params.filterByCircularity = True
		params.minCircularity = 0.1
		# Filter by Convexity
		params.filterByConvexity = True
		params.minConvexity = 0.65
		# Filter by Inertia
		params.filterByInertia = True
		params.minInertiaRatio = 0.01
		# Create a detector with the parameters
		detector = cv2.SimpleBlobDetector_create(params)
		gray_frame = cv2.cvtColor(self.frame, cv2.COLOR_RGB2GRAY)
		# detector = cv2.SimpleBlobDetector()
		self.keypoints = detector.detect(gray_frame)

	def embed(self, byte):
		pixel = self.keypoints[self.random_sequence[self.next_blob_number_index]-1]
		self.frame[int(pixel.pt[1]), int(pixel.pt[0])][0] = byte
		self.next_blob_number_index += 1

	def full(self):
		return self.next_blob_number_index == len(self.random_sequence)
		
	def getBlobCount(self):
		return self.total_blobs
	
	def getFrame(self):
		return self.frame

	""" Utils"""
	def display_blobs(self):
		im_with_keypoints = cv2.drawKeypoints(self.frame, self.keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
		self.save_frame("blob"+str(random.randint(1,100)), im_with_keypoints)
		self.display_frame("keypoint blobs", im_with_keypoints)

	def display_frame(self, name, frame=np.array([np.NaN])):
		if frame.all() == np.NaN:
			frame = self.frame
		cv2.imshow(name, frame)
		cv2.waitKey(0)

	def save_frame(self, name, frame=np.array([[[np.NaN]]])):
		if np.isnan(frame[0,0,0]):
			frame = self.frame
		cv2.imwrite(path.join(media_path, "out" + sep +name+".jpg"), frame)