import unittest
from bletchleypark.ciphers.transposition import Transposition
from bletchleypark.cryptanalysis.long_word_attack import LongWordAttack
from bletchleypark.common.string import normalize_text
from bletchleypark.common.lang_model import LangModel
from bletchleypark.common.files import get_lang_path
from bletchleypark.cryptanalysis.language_stats import LanguageStats

class TestLongWord(unittest.TestCase):
	def setUp(self):
		self.cipher = Transposition()
		self.cracker = LongWordAttack()
		self.open_text = normalize_text("jajasynpoklopurozzuresndosilenstvivodarnusrovnamsezemijmenemmistrukanvodstvijamatkuvlastnivsakkdovizdaprokouknutoumelnikolivjakpribuznismrtlidemzvodarnysmrtivrchnizradkynijenslavumistrumzcistirnytedvidisotcecozzenstinytveuzralouzjetotadybratretyslezlzradcumdozadkujensedobrepodivejcostvojijimkouprovedlimusimedrzetpospoluatuznenimarnesnazenivejmenusatanarozpoutejmepeklouzsevmychpredstavachrodisedevyjevykrasnemodrenadrzecimtakrychlecernajinenitonahodouodpadnivodamrtverybynahazimedovodarenskychobjektuuznehodlamdalnaslouchattemvodarenskymblabolumsedekrysysezerouzbytkyvodarenskychkonstrukcipredpovidamvecnouskazuvodarenskemafiitakjakodavnopredcasemjsmesvatouchatrutopilystejnykonecpripravimepodvodnikumzvodarnynelzeveritnikomukdomatlamuplnoucistotyvsechnytyhlebestiecekavodazestokysmrtlidemzvodarnysmrtivrchnizradkynijenslavumistrumzcistirnyzevsechstrannavodarnusilaspinyutocizhorastavbydrtizeleznemepoklopydokristalovevodytecoucistirenskesplaskysabotaztospachanavejmenusedepravdy")

	def test_cs_keylen4(self):
		self._help_test_method("pass")

	def test_cs_keylen7(self):
		self._help_test_method("hfewqjn")

	def test_cs_keylen10(self):
		self._help_test_method("fhwtudxnbs")

	def _help_test_method(self, key):
		key = self.cipher._repair_key(key)
		cipher_text = self.cipher.encrypt(self.open_text, key)
		langmodel = LangModel(get_lang_path('cs'))
		langmodel.get_words = self.get_words
		cracked_key = self.cracker.crack(cipher_text, LanguageStats(langmodel))
		self.assertEqual(cracked_key, key)

	def get_words(self, length):
		words = {
			4: ['ucis', 'vody', 'ahoj', 'burt', 'test', 'fail'],
			7: ['poklopu', 'asdfghj', 'poklopy'],
			10: ['kristalove']
		}

		return words.get(length, [])