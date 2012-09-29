import string

class Substitution(object):
	"""Substitution cipher"""
	def __init__(self):
		super(Substitution, self).__init__()
	
	def encode(self, open_text, key):
		substitution = dict(zip(string.ascii_letters, key))
		cipher_text = map(lambda c: substitution[c], open_text)
		return "".join(cipher_text)