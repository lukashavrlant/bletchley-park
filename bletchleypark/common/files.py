import inspect, os

DATA_DIRECTORY = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))), "../data"))

def get_lang_path(lang):
	return DATA_DIRECTORY + "/lang/%s.zip" % lang

def readfile(path):
	with open(path, "r") as f:
		return f.read()

def savefile(path, content):
	with open(path, "w") as f:
		f.write(content)

def send_to_output(content, output):
	if output:
		savefile(output, content)
	else:
		print content