import string

class Substitution(object):
	"""Substitution cipher"""
	def __init__(self):
		super(Substitution, self).__init__()
	
	def encrypt(self, open_text, key):
		substitution = dict(zip(string.ascii_lowercase, key))
		return "".join(substitution[c] for c in open_text)

	def decrypt(self, cipher_text, key):
		substitution = dict(zip(key, string.ascii_lowercase))
		return "".join(substitution[c] for c in cipher_text)