from ciphers.caesar import Caesar
from itertools import cycle

class Vigenere(object):
	"""Vigenere cipher"""
	def __init__(self):
		super(Vigenere, self).__init__()
		self.caesar = Caesar()
	
	def encode(self, open_text, key):
		return self._transform_text(open_text, key, self.caesar.shift_char_enc)

	def decode(self, cipher_text, key):
		return self._transform_text(cipher_text, key, self.caesar.shift_char_dec)

	def _transform_text(self, text, key, shift_fun):
		return "".join(map(lambda (c, k): shift_fun(c, ord(k) - ord('a')), zip(text, cycle(key))))