import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from components.crypto import Crypto

def testEncryptDecrypt():
	message = 'test data'.encode('utf-8')
	crypto_with_key = Crypto(b'ZAQkxVlI1UyVVcVARrBT0x1eYNc6qDE61oTGlaaEcXQ=')
	crypto_without_key = Crypto()

	enc_data1 = crypto_with_key.encrypt(message)
	enc_data2 = crypto_without_key.encrypt(message)

	dec_data1 = crypto_with_key.decrypt(enc_data1)
	dec_data2 = crypto_without_key.decrypt(enc_data2)

	assert dec_data1 == message and dec_data2 == message


def testGetKey():
	message = 'test data'
	key = b'ZAQkxVlI1UyVVcVARrBT0x1eYNc6qDE61oTGlaaEcXQ='
	crypto_with_key = Crypto(key)
	crypto_without_key = Crypto()

	assert crypto_with_key.getKey() == key
	assert len(crypto_without_key.getKey()) == len(key)