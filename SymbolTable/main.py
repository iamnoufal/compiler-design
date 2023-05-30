import sys

class SymbolTable:
	def __init__(self, code):
		DTYPES = {'int': 2, 'float': 4, 'double': 8, 'long': 4, 'char': 4, 'bool': 1, 'void': 0}
		self.symbols = {}
		lines = []
		for line in code:
			formatted_line = line.replace('\t', '').replace('\n', '').replace(';', '').replace('(', '').replace(')', '').replace('{', '').replace('}', '').replace(',', '').strip()
			lines.append(formatted_line)
		for _ in lines:
			syms = _.split(" ")
			if syms[0] in DTYPES:
				for each in syms[1:]:
					self.symbols[each] = {'varName': each, 'size': DTYPES[syms[0]], 'address': id(each)}
			else:
				for each in syms:
					if each not in self.symbols and each not in '+-*/%**=' and not each.isdigit():
						print("Invalid code. Variable "+each+" used before declaration")
						sys.exit()
	def printTable(self):
		print('Symbol\tAddress')
		for i in self.symbols:
			sym = self.symbols[i]
			print(sym['varName']+'\t'+str(sym['address']))

program_file = open('program.c')
lines = program_file.readlines()
SYMBOLTABLE = SymbolTable(lines)
SYMBOLTABLE.printTable()
program_file.close()
