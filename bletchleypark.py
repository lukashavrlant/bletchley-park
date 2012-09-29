from ciphers import caesar
from ciphers import substitution
from common.string import normalize_text

cip = substitution.Substitution()
# cip = caesar.Caesar()
open_text = normalize_text("abcdxyz")
key = 
print cip.encode(open_text, "bacdefghijklmnopqrstuvwxyx")
# res = cip.encode(open_text, "b")
# print res
# print cip.decode(res, "b")
