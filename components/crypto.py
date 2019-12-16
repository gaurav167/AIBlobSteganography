from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

class Crypto:
	"""Handles cryptographic module implementation as a helper to main algorithm.
	Can be swapped out for other implementations.
	Current Implementation : AES in CBC mode with 128-bit block size for encryption; using PKCS7 padding."""
	
	def __init__(self, key=None):
		self.digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
		self.key = key
		if self.key == None:
			self.key = Fernet.generate_key()
		self.enc = Fernet(self.key)
		
	def encrypt(self, data):
		return self.enc.encrypt(data)

	def mac(self, data):
		self.digest.update(data)
		hash_val = self.digest.finalize()
		encrypted_data = self.enc.encrypt(data)
		return encrypted_data + hash_val

	def decrypt(self, encrypted_data):
		return self.enc.decrypt(encrypted_data)

	def getKey(self):
		return self.key