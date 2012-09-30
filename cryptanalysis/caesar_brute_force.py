from ciphers.caesar import Caesar
import string

class CaesarBruteForce(object):
	"""Cryptanalysis method for Caesar cipher"""
	def __init__(self):
		super(CaesarBruteForce, self).__init__()
		self.caesar = Caesar()
		
	def crack(self, cipher_text, langstats):
		keys = {}
		for key in string.ascii_lowercase:
			keys[key] = langstats.similarity_index(self.caesar.decrypt(cipher_text, key))
		return sorted(keys.items(), key=lambda x: x[1], reverse=True)[0][0]