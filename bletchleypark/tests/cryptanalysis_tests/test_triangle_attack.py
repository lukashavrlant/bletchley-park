import unittest
from bletchleypark.ciphers.caesar import Caesar
from bletchleypark.cryptanalysis.triangle_attack import TriangleAttack
from bletchleypark.common.string import normalize_text
from bletchleypark.common.lang_model import LangModel
from bletchleypark.common.files import get_lang_path
from bletchleypark.cryptanalysis.language_stats import LanguageStats

class TestTriangleForce(unittest.TestCase):
	def test_cs_crack(self):
		cipher = Caesar()
		cracker = TriangleAttack()
		open_text = normalize_text("Ja, Syn Poklopu, rozzuren do silenstvi, vodarnu srovnam se zemi, jmenem mistru kanvodstvi. Ja, matku vlastni, vsak kdo vi zda, prokouknutou mel, nikoliv jak pribuzni. Tak jako davno pred casem jsme svatou chatru topily, stejny konec pripravime podvodnikum z vodarny. Nelze verit nikomu, kdo ma tlamu plnou cistoty. Vsechny tyhle bestie ceka voda ze stoky.")
		key = "q"
		cipher_text = cipher.encrypt(open_text, key)
		langmodel = LangModel(get_lang_path('cs'))
		cracked_key = cracker.crack(cipher_text, LanguageStats(langmodel))
		self.assertEqual(cracked_key, key)