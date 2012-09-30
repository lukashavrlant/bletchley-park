import unittest
from ciphers.substitution import Substitution
from common.string import normalize_text
import string

class TestSubstitutionCipher(unittest.TestCase):
	def test_encrypt(self):
		cipher = Substitution()
		open_text = normalize_text("Python is a general-purpose, interpreted high-level programming language")
		cipher_text = cipher.encrypt(open_text, string.ascii_lowercase)
		self.assertEqual(cipher_text, open_text)

		cipher_text = cipher.encrypt(open_text, "camntwqzipryofxkhdlusbevjg")
		expected = "kjuzxfilcqtftdcyksdkxltifutdkdtutnziqzytbtykdxqdcooifqycfqscqt"
		self.assertEqual(cipher_text, expected)

		self.assertEqual(cipher.encrypt("", "a"), "")

	def test_decrypt(self):
		cipher = Substitution()
		cipher_text = "kjuzxfilcqtftdcyksdkxltifutdkdtutnziqzytbtykdxqdcooifqycfqscqt"
		open_text = cipher.decrypt(cipher_text, "camntwqzipryofxkhdlusbevjg")
		expected = "pythonisageneralpurposeinterpretedhighlevelprogramminglanguage"
		self.assertEqual(open_text, expected)

		self.assertEqual(cipher.decrypt("", "a"), "")