from cryptography.fernet import Fernet

class Crypto:
	"""Handles cryptographic module implementation as a helper to main algorithm.
	Can be swapped out for other implementations.
	Current Implementation : AES in CBC mode with 128-bit block size for encryption; using PKCS7 padding."""
	
	def __init__(self, key=None):
		self.key = key
		if self.key == None:
			self.key = Fernet.generate_key()
		self.enc = Fernet(self.key)
		
	def encrypt(self, data):
		return self.enc.encrypt(data)

	def decrypt(self, encrypted_data):
		return self.enc.decrypt(encrypted_data)

	def getKey(self):
		return self.key