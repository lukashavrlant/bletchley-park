import unittest
from bletchleypark.ciphers.vigenere import Vigenere
from bletchleypark.common.string import normalize_text

class TestVigenereCipher(unittest.TestCase):
	def test_encrypt(self):
		cipher = Vigenere()
		open_text = normalize_text("Python is a general-purpose, interpreted high-level programming language")
		cipher_text = cipher.encrypt(open_text, "a")
		self.assertEqual(cipher_text, open_text)

		cipher_text = cipher.encrypt(open_text, "bc")
		expected = "qaujppjubifpftbnqwsrpufkovftqtfvffikhjmgwgmrsqhtbonkoimcoivchg"
		self.assertEqual(cipher_text, expected)

		cipher_text = cipher.encrypt(open_text, "password")
		expected = "eylzkbzvpgwfafroeujhkgvlctwjlfvwtdzacvchkedhncxupmeajucdcgmscs"
		self.assertEqual(cipher_text, expected)

		self.assertEqual(cipher.encrypt("", "a"), "")

	def test_decrypt(self):
		cipher = Vigenere()
		cipher_text = "eylzkbzvpgwfafroeujhkgvlctwjlfvwtdzacvchkedhncxupmeajucdcgmscs"
		open_text = cipher.decrypt(cipher_text, "password")
		expected = "pythonisageneralpurposeinterpretedhighlevelprogramminglanguage"
		self.assertEqual(open_text, expected)

		self.assertEqual(cipher.decrypt("", "a"), "")