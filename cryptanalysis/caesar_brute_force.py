from ciphers.caesar import Caesar
import string

class CaesarBruteFroce(object):
	"""Cryptanalysis method for Caesar cipher"""
	def __init__(self):
		super(CaesarBruteFroce, self).__init__()
		self.caesar = Caesar()
		
	def crack(self, cipher_text, langstats):
		keys = {}
		for key in string.ascii_lowercase:
			keys[key] = langstats.similarity_index(self.caesar.decode(cipher_text, key))
		return sorted(keys.items(), key=lambda x: x[1], reverse=True)[0][0]