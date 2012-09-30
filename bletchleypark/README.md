# Cryptanalysis historical ciphers

Bletchley Park is a python implementation of an enrypting/decrypting/cracking library for historical ciphers like Caesar shift cipher, substitution cipher, Vigenère cipher, and transposition cipher. For cracking only czech language is supported right now.

[Why Bletchley Park?](http://en.wikipedia.org/wiki/Bletchley_Park)

## Installation

You will need Python 2.7. Installation using git:

	$ git clone git@github.com:havrlant/bletchley-park.git
	$ cd bletchley-park/
	$ python setup.py install
	$ bletchleypark -h

Or simply download zip file and do the same without `git clone` part.

## Usage

See `bletchleypark -h`. Supported ciphers are: 

- `caesar` (for Caesar/Shift cipher)
- `vig` (for Vigenère cipher)
- `subs` (for Substitution cipher; only encrypt/decrypt methods, no cracking method yet)
- `trans` (for Transposition cipher)

## Examples
	
If you want to encrypt a text "Hello World" using Caesar (Shift) cipher and the "b" key:

	$ bletchleypark -t "Hello World" -e caesar -k b
	ifmmpxpsme

To decrypt back to "Hello World" use:

	$ bletchleypark -t "ifmmpxpsme" -d caesar -k b
	helloworld

If you want to crack a text "..." which was encrypted by Vigenère cipher:

	$ bletchleypark -c vig -t "..."

Or you can always use `-i path` option instead of `-t`:

	$ bletchleypark -c vig -i path/to/file.txt