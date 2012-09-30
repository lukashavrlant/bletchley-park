import inspect, os

DATA_DIRECTORY = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))), "../data"))

def get_lang_path(lang):
	return DATA_DIRECTORY + "/lang/%s.zip" % lang