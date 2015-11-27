
class LanguageDetector(object):

	LANGUAGE_EXTENSIONS = [
		{"lang": "python", "ext": "py"},
		{"lang": "javascript", "ext": "js"},
	]

	def __init__(self):
		pass 

	@staticmethod
	def detect(extension):
		if not extension:
			return null

		for lang in LanguageDetector.LANGUAGE_EXTENSIONS:
			if extension in lang["ext"]:
				return lang["lang"]
		return null