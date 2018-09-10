class A_cmd:
	def __init__(self, cmd):
		# A command should be of the form: @<symbol>
		self._cmd = cmd
		self._symbol = cmd[1:]

	def symbol(self):
		return self._symbol

	def evalSymbol(self, symbol):
		return symbol

	def binaryCode(self):
		binaryCode = format(int(self.evalSymbol(self._symbol)), 'b')
		return "0" + binaryCode.zfill(15)

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
		self._compCodes = {
		"0":"0101010", "1":"0111111", "-1":"0111010", "D":"0001100",
		"A":"0110000", "!D":"0001101", "!A":"0110001", "-D":"0001111",
		"-A":"0110011", "D+1":"0011111", "A+1":"0110111", "D-1":"0001110", 
		"A-1":"0110010", "D+A":"0000010", "D-A":"0010011", "A-D":"0000111", 
		"D&A":"0000000", "D|A":"0010101", "M":"1110000", "!M":"1110001", 
		"-M":"1110011", "M+1":"1110111", "M-1":"1110010","D+M":"1000010",
		"D-M":"1010011","M-D":"1000111", "D&M":"1000000","D|M":"1010101"
		}
		self._destCodes = {
		"null":"000","M":"001","D":"010","MD":"011",
		"A":"100","AM":"101","AD":"110","AMD":"111"
		}
		self._jumpCodes = {
		"null":"000","JGT":"001","JEQ":"010","JGE":"011",
		"JLT":"100","JNE":"101","JLE":"110","JMP":"111"
		}

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

	def binaryCode(self, field=""):
		binary = ["0000000","000","000"]
		if (self._comp != None):
			binary[0] = self._compCodes[self._comp]
		if (self._dest != None):
			binary[1] = self._destCodes[self._dest]
		if (self._jump != None):
			binary[2] = self._jumpCodes[self._jump]

		if (field == ""): return "111" + "".join(binary)
		elif (field == "comp"): return binary[0]
		elif (field == "dest"): return binary[1]
		elif (field == "jump"): return binary[2]
		print("Invalid field.")
		return ""