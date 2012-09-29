from ciphers import caesar
from common.string import normalize_test

cip = caesar.Caesar()
open_text = normalize_test("abcd eZ")
print cip.encode(open_text, 'b')
