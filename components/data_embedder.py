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
		encrypted_data = self.crypto.encrypt(self.data)
		stream = VideoManager(self.media_source, self.key)
		frame = stream.getNextFrame()
		if frame.all() == -1:
			raise Exception("Video frames corrupted!")
		hot_frame = FrameManager(frame, self.key)
		for byte in encrypted_data:
			if hot_frame.full():
				# Find the next empty frame. Exit with exception if not available
				while True:
					if not stream.full():
						frame = stream.getNextFrame()
						if frame.all() == -1:
							raise Exception("Video frames corrupted!")
						hot_frame = FrameManager(frame, self.key)
						if hot_frame.getBlobCount() != 0:
							break

					else:
						raise Exception("Data storage capacity exceeded!")

			hot_frame.embed(byte)

	def extractData(self):
		pass
