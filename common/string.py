import unicodedata

def _strip_accents(text):
	return str(''.join((c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')))

def normalize_text(text):
	text = _strip_accents(unicode(text)).lower()
	text = filter(_keep_char, text)
	return text

def _keep_char(char):
	return char.isalpha()