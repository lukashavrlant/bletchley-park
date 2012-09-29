import string
from itertools import combinations
from collections import Counter
from common.constants import ALPHABET_SIZE
from ciphers.caesar import Caesar

class TriangleAttack(object):
	"""Cryptanalysis method for Caesar cipher"""
	def __init__(self):
		super(TriangleAttack, self).__init__()
		self.take_chars = 6
		self.chars_from_lang = 3
		self.caesar = Caesar()
		
	def crack(self, cipher_text, langstats):
		top_lang_letters = langstats.most_common_letters(self.chars_from_lang)
		least_lang_letters = langstats.least_common_letters(self.chars_from_lang)
		
		counter = self._get_counter(cipher_text)
		top_text_letters = map(lambda (a, b): a, counter.most_common(self.take_chars))
		least_text_letters = map(lambda (a, b): a, list(reversed(counter.most_common()))[:self.take_chars])

		top = self._find_triangle(top_lang_letters, top_text_letters)
		least = self._find_triangle(least_lang_letters, least_text_letters)

		top_keys = self._get_set_of_keys(top_lang_letters, top)
		least_keys = self._get_set_of_keys(least_lang_letters, least)
		return self._choose_key(top_keys, least_keys)
		

	def _choose_key(self, top_keys, least_keys):
		intersection = top_keys & least_keys
		if intersection:
			return list(intersection)[0]
		else:
			union = top_keys | least_keys
			if union:
				return list(union)[0]
			else:
				return None

	def _get_set_of_keys(self, lang_letters, list_of_text_letters):
		temp_keys = {self._get_key("".join(lang_letters), x) for x in list_of_text_letters}
		return set(filter(lambda x: x, temp_keys))

	def _get_key(self, lang_letters, text_letters):
		for key in string.ascii_lowercase:
			if set(self.caesar.encode(lang_letters, key)) == set(text_letters):
				return key

	def _get_counter(self, text):
		counter = Counter(text)
		for char in string.ascii_lowercase:
			if char not in counter:
				counter[char] = 0
		return counter

	def _find_triangle(self, lang_letters, text_letters):
		triangles = []
		distances = self._compute_distances(lang_letters)
		for perm in combinations(text_letters, self.chars_from_lang):
			curr_distances = self._compute_distances(perm)
			if curr_distances == distances:
				triangles.append("".join(perm))
		return triangles


	def _compute_distances(self, letters):
		return sorted([self._letter_distance(a, b) for a, b in combinations(letters, 2)])

	def _letter_distance(self, char1, char2):
		distance = abs(ord(char1) - ord(char2));
		return distance if distance <= ALPHABET_SIZE / 2 else ALPHABET_SIZE - distance