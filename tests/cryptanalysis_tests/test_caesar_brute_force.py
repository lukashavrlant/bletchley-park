import unittest
from ciphers.caesar import Caesar
from cryptanalysis.caesar_brute_force import CaesarBruteForce
from common.string import normalize_text

class TestCaesarBruteForce(unittest.TestCase):
	def test_crack(self):
		cipher = Caesar()
		cracker = CaesarBruteForce()
		open_text = normalize_text("Python is a general-purpose, interpreted high-level programming language")
		key = "d"
		cipher_text = cipher.encrypt(open_text, key)
		decrypted_text = cracker.crack(cipher_text)
		print decrypted_text
		self.assertEqual(decrypted_text, open_text)
		self.assertEqual(1,2)
		