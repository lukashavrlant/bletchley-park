from common.constants import ALPHABET_SIZE

class Caesar(object):
	"""Caesar cipher"""
	def __init__(self):
		super(Caesar, self).__init__()

	def encode(self, open_text, key):
		shift_key = ord(key) - ord('a')
		cipher_text = map(lambda c: self._shift_char(c, shift_key), open_text)
		return "".join(cipher_text)

	def _shift_char(self, char, shift_key):
		shift_char = ord(char) + shift_key
		return chr(shift_char) if shift_char <= ord('z') else chr(shift_char - ALPHABET_SIZE)