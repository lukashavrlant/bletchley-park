import unittest
from ciphers.caesar import Caesar
from common.string import normalize_text

class TestCaesarCipher(unittest.TestCase):
	def test_encode(self):
		cipher = Caesar()
		open_text = normalize_text("Python is a general-purpose, interpreted high-level programming language")
		cipher_text = cipher.encode(open_text, "a")
		self.assertEqual(cipher_text, open_text)

		cipher_text = cipher.encode(open_text, "k")
		expected = "zidryxsckqoxobkvzebzycosxdobzbodonrsqrvofovzbyqbkwwsxqvkxqekqo"
		self.assertEqual(cipher_text, expected)

		self.assertEqual(cipher.encode("", "a"), "")

	def test_decode(self):
		cipher = Caesar()
		cipher_text = "zidryxsckqoxobkvzebzycosxdobzbodonrsqrvofovzbyqbkwwsxqvkxqekqo"
		open_text = cipher.decode(cipher_text, "k")
		expected = "pythonisageneralpurposeinterpretedhighlevelprogramminglanguage"
		self.assertEqual(open_text, expected)

		self.assertEqual(cipher.decode("", "a"), "")