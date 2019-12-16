import time

from crypto import Crypto
from video_manager import VideoManager
from frame_manager import FrameManager

class AISteganography:
	"""Driver class for algorithm to hide data in video"""

	def __init__(self, data, media_source, key=None):
		self.data = data.encode('utf-8')
		# Absolute path in Media Source
		self.media_source = media_source
		self.key = key
		# Size of key is 128-bit
		self.crypto = Crypto(self.key)
		if self.key == None:
			self.key = self.crypto.getKey()

	def embedData(self):
		start_time = time.process_time()
		print("Encrypting Data...")
		encrypted_data = self.crypto.mac(self.data)
		print("Reading Video...")
		stream = VideoManager(self.media_source, self.key)
		frame = stream.getNextFrame()
		current_frame_index = stream.getCurrentFrame()
		if frame.all() == -1:
			raise Exception("Video frames corrupted!")
		hot_frame = FrameManager(frame, self.key)
		number = 1
		print("Embedding Data...")
		for byte in encrypted_data:
			if hot_frame.full():
				# Find the next empty frame. Exit with exception if not available
				while True:
					if not stream.full():
						frame = stream.getNextFrame()
						current_frame_index = stream.getCurrentFrame()
						if frame.all() == -1:
							raise Exception("Video frames corrupted!")
						hot_frame = FrameManager(frame, self.key)
						if hot_frame.getBlobCount() != 0:
							break
					else:
						raise Exception("Data storage capacity exceeded!")
			hot_frame.save_frame("frame_before_" + str(number))
			hot_frame.embed(byte)
			stream.write_frame(current_frame_index, hot_frame.getFrame())
			hot_frame.save_frame("frame_after_" + str(number))
			number += 1
		print("Generating Video...")
		stream.generate_video()
		print("Done!")
		execution_time = round(time.process_time() - start_time, 3)
		print("Completed in", execution_time, "seconds")


	def extractData(self):
		start_time = time.process_time()
		print("Initiating Data Retrieval Process")
		print("Reading Video...")
		stream = VideoManager(self.media_source, self.key)
		frame = stream.getNextFrame()
		current_frame_index = stream.getCurrentFrame()
		if frame.all() == -1:
			raise Exception("Video frames corrupted!")
		retrieved_data = ""
		time.sleep(5)
		hot_frame = FrameManager(frame, self.key)
		number = 1
		print("Decrypting Data...")
		for byte in self.data:
			if hot_frame.full():
				# Find the next empty frame. Exit with exception if not available
				while True:
					if not stream.full():
						frame = stream.getNextFrame()
						current_frame_index = stream.getCurrentFrame()
						if frame.all() == -1:
							raise Exception("Video frames corrupted!")
						hot_frame = FrameManager(frame, self.key)
						if hot_frame.getBlobCount() != 0:
							break
					else:
						raise Exception("Data storage capacity exceeded!")
			retrieved_data += chr(byte)
			number += 1
		print("Done!")
		execution_time = round(time.process_time() - start_time, 3)
		print("Completed in", execution_time, "seconds")

		return retrieved_data