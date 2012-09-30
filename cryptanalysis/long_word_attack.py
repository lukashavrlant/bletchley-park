from bletchleypark.ciphers.transposition import Transposition
from collections import Counter

class LongWordAttack(object):
	"""Cryptanalysis method for transposition cipher"""
	def __init__(self):
		super(LongWordAttack, self).__init__()
		self.max_keylen = 15
		self.transposition = Transposition()

	def crack(self, cipher_text, langstats):
		key_text_pair = lambda key: (key, self.transposition.decrypt(cipher_text, key))
		texts = (key_text_pair(key) for key in self._get_possible_keys(cipher_text, langstats))
		return langstats.most_meaningful(texts)

	def _get_possible_keys(self, cipher_text, langstats):
		reshuffle_text = self.transposition._partition_text_decrypt
		for keylen in self._key_lengths(cipher_text):
			all_words = langstats.get_words(keylen)
			for cipher_word in reshuffle_text(cipher_text, len(cipher_text) / keylen):
				cipher_counter = Counter(cipher_word)
				for real_word in all_words:
					if Counter(real_word) == cipher_counter:
						for key in self._get_valid_keys(cipher_word, real_word):
							yield key

	def _get_valid_keys(self, cipher_word, real_word):
		for perm in self._get_perms(real_word, 0, [], self.get_positions(cipher_word)):
			yield "".join(map(lambda x: chr(x + ord('a')), perm))

	def _get_perms(self, word, currPos, visited, positions):
		if currPos == len(word):
			yield visited
		else:
			c = word[currPos]
			for free in positions[c] - set(visited):
				for vis in self._get_perms(word, currPos + 1, visited + [free], positions):
					yield vis

	def get_positions(self, word):
		pos = {}
		for i, char in enumerate(word):
			if char in pos:
				pos[char].add(i)
			else:
				pos[char] = {i}
		return pos


	def _key_lengths(self, cipher_text):
		ltext = len(cipher_text)
		for i in range(2, self.max_keylen + 1):
			if ltext % i == 0:
				yield i