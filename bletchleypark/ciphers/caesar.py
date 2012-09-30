from bletchleypark.common.constants import ALPHABET_SIZE

class Caesar(object):
	"""Caesar cipher"""
	def __init__(self):
		super(Caesar, self).__init__()

	def encrypt(self, open_text, key):
		return self._transform_text(open_text, key, self.shift_char_enc)

	def decrypt(self, cipher_text, key):
		return self._transform_text(cipher_text, key, self.shift_char_dec)

	def _transform_text(self, text, key, fun):
		shift_key = ord(key) - ord('a')
		transformed_text = map(lambda c: fun(c, shift_key), text)
		return "".join(transformed_text)

	def shift_char_enc(self, char, shift_key):
		shift_char = ord(char) + shift_key
		return chr(shift_char) if shift_char <= ord('z') else chr(shift_char - ALPHABET_SIZE)

	def shift_char_dec(self, char, shift_key):
		shift_char = ord(char) - shift_key
		return chr(shift_char) if shift_char >= ord('a') else chr(shift_char + ALPHABET_SIZE)