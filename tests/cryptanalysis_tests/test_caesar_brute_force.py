import unittest
from ciphers.caesar import Caesar
from cryptanalysis.caesar_brute_force import CaesarBruteForce
from common.string import normalize_text
from common.lang_model import LangModel
from common.files import get_lang_path
from cryptanalysis.language_stats import LanguageStats

class TestCaesarBruteForce(unittest.TestCase):
	def test_cs_crack(self):
		cipher = Caesar()
		cracker = CaesarBruteForce()
		open_text = normalize_text("Python is a general-purpose, interpreted high-level programming language")
		key = "d"
		cipher_text = cipher.encrypt(open_text, key)
		langmodel = LangModel(get_lang_path('cs'))
		cracked_key = cracker.crack(cipher_text, LanguageStats(langmodel))
		self.assertEqual(cracked_key, key)	