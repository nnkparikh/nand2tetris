from Commands import *

class Parser:
	A_CMD = 1
	C_CMD = 2
	L_CMD = 3
	def __init__(self, file):
		self._file_obj = open(file, "r")
		self._current_cmd = None
		self._commandType = None
		self._commandObj = None

	def advance(self):
		# skip comments and whitespace lines. 
		while True:
			current_cmd = self._file_obj.readline()
			self._current_cmd = current_cmd
			# reached end of file, no more instructions to read.
			if (current_cmd == ""):
				print("Reached end of assembly file. Closing file object...")
				self._file_obj.close()
				break
			if (self.validInstruction(current_cmd.strip())):
				break

		return self._current_cmd

	def validInstruction(self, current_cmd):
		cmd_l = current_cmd.split()
		if ((cmd_l != []) and (cmd_l[0] != "//")):
			self._current_cmd = cmd_l[0]
			if (self._current_cmd[0] == "@"):
				self._commandType = Parser.A_CMD
				self._commandObj = A_cmd(self._current_cmd)

			elif (self._current_cmd[0] == "("):
				self._commandType = Parser.L_CMD
				self._commandObj = L_cmd(self._current_cmd)
			else:
				self._commandType = Parser.C_CMD
				self._commandObj = C_cmd(self._current_cmd)
			return True
		return False

	def commandType(self):
		return self._commandType

	def commandObj(self):
		return self._commandObj

	def currentCmd(self):
		return self._current_cmd
