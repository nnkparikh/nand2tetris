from Parser import Parser

cmdTypes = ["","A_CMD", "C_CMD", "L_CMD"]
def parseAssembly(file_name):
	parser = Parser(file_name)
	line_num = 0
	while True:
		current_cmd = parser.advance()
		if (current_cmd == ""): break
		cmd_type = parser.commandType()
		print("({}) [current_cmd: {}] [cmd_type: {}]".format(line_num, current_cmd, cmdTypes[int(cmd_type)]))
		cmd_obj = parser.commandObj()
		cmd_binary = cmd_obj.binaryCode()
		line_num += 1
		
if (__name__ == "__main__"):
	parseAssembly('MaxL.asm')