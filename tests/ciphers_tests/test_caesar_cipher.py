import unittest
from bletchleypark.ciphers.caesar import Caesar
from bletchleypark.common.string import normalize_text

class TestCaesarCipher(unittest.TestCase):
	def test_encrypt(self):
		cipher = Caesar()
		open_text = normalize_text("Python is a general-purpose, interpreted high-level programming language")
		cipher_text = cipher.encrypt(open_text, "a")
		self.assertEqual(cipher_text, open_text)

		cipher_text = cipher.encrypt(open_text, "k")
		expected = "zidryxsckqoxobkvzebzycosxdobzbodonrsqrvofovzbyqbkwwsxqvkxqekqo"
		self.assertEqual(cipher_text, expected)

		self.assertEqual(cipher.encrypt("", "a"), "")

	def test_decrypt(self):
		cipher = Caesar()
		cipher_text = "zidryxsckqoxobkvzebzycosxdobzbodonrsqrvofovzbyqbkwwsxqvkxqekqo"
		open_text = cipher.decrypt(cipher_text, "k")
		expected = "pythonisageneralpurposeinterpretedhighlevelprogramminglanguage"
		self.assertEqual(open_text, expected)

		self.assertEqual(cipher.decrypt("", "a"), "")