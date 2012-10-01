from bletchleypark.ciphers.caesar import Caesar
import string

class CaesarBruteForce(object):
	"""Cryptanalysis method for Caesar cipher"""
	def __init__(self):
		super(CaesarBruteForce, self).__init__()
		self.caesar = Caesar()
		
	def crack(self, cipher_text, langstats):
		keys = ((k,self.caesar.decrypt(cipher_text, k)) for k in string.ascii_lowercase)
		return langstats.most_meaningful(keys)