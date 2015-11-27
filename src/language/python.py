
from .language import Language

class Python(Language):
	def __init__(self):
		super(Python, self).__init__()

		self.load_language()

	def load_language( self ):

		# add ignore filename(s)
		self.add_ignore_file([".gitignore"])

		# add skip directories 
		self.add_ignore_dir("tests")

		# valid extensions 
		self.add_valid_extensions([".py"])

		# invalid extenions 
		self.add_invalid_extensions([".pyw"])