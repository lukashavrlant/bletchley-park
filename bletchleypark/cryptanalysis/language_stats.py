from bletchleypark.common.constants import ALPHABET_SIZE
import string
from collections import Counter

class LanguageStats(object):
	"""Statistic information about language"""
	def __init__(self, lang_model):
		super(LanguageStats, self).__init__()
		self.frequency = lang_model.get_frequency()
		self.model = lang_model

	def similarity_index(self, text):
		ltext = float(len(text))
		counter = Counter(text)
		rel_counter = {x:(counter.get(x, 0)/ltext)*100 for x in string.ascii_lowercase}
		unigrams = self._deviation(self.frequency['letters'], rel_counter)
		bigrams = self._normalize_deviation(self.frequency['bigrams'], text, 2)
		trigrams = self._normalize_deviation(self.frequency['trigrams'], text, 3)
		topwords_count = self._count_top_words(text)
		# print "uno: %s, bi: %s, tri: %s, topw: %s" % (unigrams, bigrams, trigrams, topwords_count)
		return unigrams + bigrams + trigrams + topwords_count

	def most_meaningful(self, texts):
		max_index = 0
		final_key = "?"
		for key, text in texts:
			index = self.similarity_index(text)
			if index > max_index:
				max_index = index
				final_key = key
		return final_key

	def most_common_letters(self, n):
		return map(lambda (a, b): a, Counter(self.frequency['letters']).most_common(n))

	def least_common_letters(self, n):
		return map(lambda (a, b): a, list(reversed(Counter(self.frequency['letters']).most_common()))[:n])

	def get_words(self, length):
		return self.model.get_words(length)

	def _count_top_words(self, text):
		return float(sum(1 if x in text else 0 for x in self.frequency['topwords'])) / (len(text))

	def _normalize_deviation(self, lang_freq, text, n):
		return self._deviation(lang_freq, self._ngrams_counter(text, n)) / n

	def _ngrams_counter(self, text, n):
		return Counter(text[x:x+n] for x in range(len(text)-n+1))

	def _deviation(self, lang_freq, text_freq):
		index = 0
		for k, v in text_freq.items():
			index += abs(v - lang_freq.get(k, 0))
		return 1/index