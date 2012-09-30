import unittest
from ciphers.transposition import Transposition
from common.string import normalize_text
import string

class TestTranspositionCipher(unittest.TestCase):
	def test_encrypt(self):
		cipher = Transposition()
		open_text = normalize_text("Python is a general-purpose, interpreted high-level programming language")
		cipher_text = cipher.encrypt(open_text, "password")
		expected = "hnpripiapapnevannrsrhogeiaeelglxsliteraxterehlmuoeopgrngygutdemg"
		self.assertEqual(cipher_text, expected)

	def test_decrypt(self):
		cipher = Transposition()
		open_text = normalize_text("Python is a general-purpose, interpreted high-level programming language")
		key = "password"
		cipher_text = cipher.encrypt(open_text, key)
		decrypted_text = cipher.decrypt(cipher_text, key)
		expected = open_text + "xx"
		self.assertEqual(decrypted_text, expected)