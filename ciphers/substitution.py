import string

class Substitution(object):
	"""Substitution cipher"""
	def __init__(self):
		super(Substitution, self).__init__()
	
	def encode(self, open_text, key):
		substitution = dict(zip(string.ascii_lowercase, key))
		cipher_text = map(lambda c: substitution[c], open_text)
		return "".join(cipher_text)

	def decode(self, cipher_text, key):
		substitution = dict(zip(key, string.ascii_lowercase))
		open_text = map(lambda c: substitution[c], cipher_text)
		return "".join(open_text)