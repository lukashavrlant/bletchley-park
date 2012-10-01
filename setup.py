from distutils.core import setup
setup(name='bletchleypark',
      version='1.0',
      packages = ['bletchleypark', 'bletchleypark.ciphers', 'bletchleypark.cryptanalysis', 'bletchleypark.common'],
      package_data = {'bletchleypark' : ['../data/lang/*.zip']},
      scripts = ["bletchleypark/bletchleypark"]
      )