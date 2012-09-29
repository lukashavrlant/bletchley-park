import string
from collections import Counter

class LanguageStats(object):
	"""Statistic information about language"""
	def __init__(self, frequency):
		super(LanguageStats, self).__init__()
		self.frequency = frequency

	def similarity_index(self, text):
		ltext = float(len(text))
		counter = Counter(text)
		rel_counter = {x:counter.get(x, 0)/ltext for x in string.ascii_lowercase}

		index = 0
		lang_stats = self.frequency['letters']
		for k, v in rel_counter.items():
			index += abs(v - lang_stats[k])
		return 1/index
		
	def most_common_letters(self, n):
		return map(lambda (a, b): a, Counter(self.frequency['letters']).most_common(n))

	def least_common_letters(self, n):
		return map(lambda (a, b): a, list(reversed(Counter(self.frequency['letters']).most_common()))[:n])