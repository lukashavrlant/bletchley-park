from zipfile import ZipFile
import json

class LangModel(object):
	"""docstring for LangModel"""
	def __init__(self, lang_file_path):
		super(LangModel, self).__init__()
		self.path = lang_file_path
		self.zipfile = None

	def get_words(self, length):
		return self._zipfile().read("words/%s.dic" % length).split()

	def get_frequency(self):
		return self.JSONUnicode2Str(json.loads(self._zipfile().read("words/letters.json")))

	def _zipfile(self):
		if not self.zipfile:
			self.zipfile = ZipFile(self.path, "r")
		return self.zipfile

	def JSONUnicode2Str(self, json):
		newdict = {}
		for k, v in json.items():
			newInnerDict = {}
			if isinstance(v, dict):
				for a, b in v.items():
					newInnerDict[str(a)] = b 
				newdict[str(k)] = newInnerDict
			else:
				newdict[str(k)] = map(str, v)
		return newdict