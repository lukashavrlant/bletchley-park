from ciphers import caesar
from ciphers import substitution
from ciphers import vigenere
from common.string import normalize_text

# cip = substitution.Substitution()
# cip = caesar.Caesar()
cip = vigenere.Vigenere()
open_text = normalize_text("abcdxyz")
print cip.encode(open_text, "abx")
# res = cip.encode(open_text, "b")
# print res
# print cip.decode(res, "b")
