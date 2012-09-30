from bletchleypark.ciphers.caesar import Caesar
from itertools import cycle, izip

class Vigenere(object):
	"""Vigenere cipher"""
	def __init__(self):
		super(Vigenere, self).__init__()
		self.caesar = Caesar()
	
	def encrypt(self, open_text, key):
		return self._transform_text(open_text, key, self.caesar.shift_char_enc)

	def decrypt(self, cipher_text, key):
		return self._transform_text(cipher_text, key, self.caesar.shift_char_dec)

	def _transform_text(self, text, key, shift_fun):
		return "".join(shift_fun(c, ord(k) - ord('a')) for c, k in izip(text, cycle(key)))