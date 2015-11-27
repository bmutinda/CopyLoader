
class Language(object):
	'''
	Programming Language mapper that should be subclassed 
	by any new Language
	'''

	valid_extensions = []
	invalid_extensions = []
	ignore_files = []
	ignore_dirs = []

	def __init__(self):
		pass 

	def load_language( self ):
		raise NotImplementedError("load_language should be implemented.... :D")

	def add_valid_extension( self, extension ):
		self.valid_extensions.append( extension )

	def add_invalid_extension( self, extension ):
		self.valid_extensions.append( extension )

	def add_ignore_file( self, filename ):
		if type(filename) is str:
			self.ignore_files.append(filename)
		if type(filename) is list:
			self.add_ignore_files( filename )

	def add_ignore_files( self, filenames ):
		if type(filenames) is list:
			for f in filenames:
				self.ignore_files.append(f)

		return self.ignore_files

	def add_ignore_dir( self, directory ):
		if not type(directory) is str:
			return
		self.ignore_dirs.append( directory )

	def add_ignore_dirs( self, directories ):
		if not type(directory) is list:
			return
		for d in directories:
			self.ignore_dirs.append(d)

	def add_valid_extensions(self, extensions):
		if type(extensions) is list:
			for ext in  extensions:
				self.valid_extensions.append( "."+ext if "." not in ext else ext )

	def add_invalid_extensions(self, extensions):
		if type(extensions) is list:
			for ext in  extensions:
				self.invalid_extensions.append( "."+ext if "." not in ext else ext )
