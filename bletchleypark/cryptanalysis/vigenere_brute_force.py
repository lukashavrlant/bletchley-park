from bletchleypark.cryptanalysis.triangle_attack import TriangleAttack
from bletchleypark.ciphers.vigenere import Vigenere

class VigenereBruteForce(object):
	"""Cryptanalysis method for Vigenere cipher"""
	def __init__(self):
		super(VigenereBruteForce, self).__init__()
		self.max_key_len = 10
		self.caesar_cracker = TriangleAttack()
		self.vigenere = Vigenere()
	
	def crack(self, cipher_text, langstats):
		keys = self._get_possible_keys(cipher_text, langstats)
		return langstats.most_meaningful(keys)

	def _get_possible_keys(self, cipher_text, langstats):
		for i in range(2, self.max_key_len + 1):
			partition = self._partition_text(cipher_text, i)
			key = "".join(self.caesar_cracker.crack(v, langstats) for v in partition)
			yield key, self.vigenere.decrypt(cipher_text, key)

	def _partition_text(self, text, number):
		classes = {x:[] for x in range(number)}
		for i, char in enumerate(text):
			classes[i % number].append(char)
		return ("".join(v) for k, v in classes.iteritems())