class A_cmd:
	def __init__(self, cmd):
		# A command should be of the form: @<symbol>
		self._cmd = cmd
		self._symbol = cmd[1:]

	def symbol(self):
		return self._symbol

	def binaryCode(self):
		pass

class L_cmd:
	def __init__(self, cmd):
		# A command should be of the form: @<symbol>
		self._cmd = cmd
		self._symbol = cmd[1:-1]
	
	def symbol(self):
		return self_symbol

	def binaryCode(self):
		pass

class C_cmd:
	def __init__(self, cmd):
		self._cmd = cmd
		self._dest = None
		self._comp = None
		self._jump = None
		self._setFields()
		self._compCodes = {}

	def _setFields(self):
		# set dest field
		dest_l = self._cmd.split("=")
		comp_index = 0
		if (len(dest_l) != 2):
			self._dest = None
		else: 
			self._dest = dest_l[0]
			comp_index = 1

		# set comp field 
		cmp_l = dest_l[comp_index].split(";")
		self._comp = cmp_l[0]

		# set jump field
		if (len(cmp_l) != 2):
			self._jump = None
		else:
			self._jump = cmp_l[1]

	def dest(self):
		return self._dest

	def comp(self):
		return self._comp

	def jump(self):
		return self._jump

	def binaryCode(self, field):
		binary = None
		if (field == "dest" and self._dest != None):
			binary = self._compCodes[self._dest]
		elif (field == "comp" and self._comp != None):
			binary = self._compCodes[self._comp]
		elif (field == "jump" and self._jump != None):
			binary = self._compCodes[self._jump]
		else: 
			print("Invalid field.")
			
		return binary