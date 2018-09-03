import Code

class Parser:
	A_CMD = 1
	C_CMD = 2
	L_CMD = 3
	def __init__(self, file):
		self.file_obj = open(file, "r")
		self.current_cmd = None
		self.commandType = None
		self.symbol = None
		self.dest = None
		self.comp = None
		self.jump = None

	def advance(self):
		# skip comments and whitespace lines. 
		while True:
			current_cmd = self.file_obj.readline()
			self.current_cmd = current_cmd
			# reached end of file, no more instructions to read.
			if (current_cmd == ""):
				print("Reached end of assembly file. Closing file object...")
				self.file_obj.close()
				break
			if (self.validInstruction(current_cmd.strip())):
				break

		return self.current_cmd

	def validInstruction(self, current_cmd):
		cmd_l = current_cmd.split()
		if ((cmd_l != []) and (cmd_l[0] != "//")):
			self.current_cmd = cmd_l[0]
			if (self.current_cmd[0] == "@"):
				self.commandType = Parser.A_CMD
				self.symbol = self.current_cmd[1:]
			elif (self.current_cmd[0] == "("):
				self.commandType = Parser.L_CMD
				self.symbol = self.current_cmd[1:-1]
			else:
				self.commandType = Parser.C_CMD
				self.symbol = None
				dest_cmd_l = self.current_cmd.split("=")
				comp_index = 0
				if (len(dest_cmd_l) != 2):
					self.dest = None
				else: 
					self.dest = dest_cmd_l[0]
					comp_index = 1

				cmp_l = dest_cmd_l[comp_index].split(";")
				self.comp = cmp_l[0]
				if (len(cmp_l) != 2):
					self.jump = None
				else:
					self.jump = cmp_l[1]

			return True
		return False

	def commandType(self):
		return self.commandType

	def symbol(self):
		pass

	def dest(self):
		pass

	def comp(self):
		pass

	def jump(self):
		pass

