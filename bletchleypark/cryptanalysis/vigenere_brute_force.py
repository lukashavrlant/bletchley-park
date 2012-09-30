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
		ranked_keys = {k:langstats.similarity_index(self.vigenere.decrypt(cipher_text, k)) for k in keys}
		return self._choose_key(ranked_keys)

	def _choose_key(self, keys):
		values = set()
		filtered_keys = {}
		for k, v in sorted(keys.items(), key=lambda x: len(x[0])):
			if v not in values:
				values.add(v)
				filtered_keys[k] = v
		return sorted(filtered_keys.items(), key=lambda x: x[1], reverse=True)[0][0]

	def _get_possible_keys(self, cipher_text, langstats):
		for i in range(2, self.max_key_len + 1):
			partition = self._partition_text(cipher_text, i)
			keys = {k:self.caesar_cracker.crack(v, langstats) for k, v in partition.items()}
			key = "".join(map(lambda x: x[1], sorted(keys.items(), key=lambda x: x[0])))
			yield key

	def _partition_text(self, text, number):
		classes = {x:[] for x in range(number)}
		for i, char in enumerate(text):
			classes[i % number].append(char)
		return {k:"".join(v) for k, v in classes.items()}