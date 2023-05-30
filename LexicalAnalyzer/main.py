class LexicalAnalyzer:
	def __init__(self, code):
		KEYWORDS = ['int', 'float', 'char', 'double', 'long', 'if', 'else', 'while', 'do', 'switch', 'case', 'goto', 'void', 'printf', 'scanf']
		self.TOKENS = []
		lines = []
		for line in code:
			formatted_line = line.replace('\t', '').replace('\n', '').replace(';', '').replace(',', '').strip()
			lines.append(formatted_line)
		for _ in lines:
			syms = _.split(" ")
			for i in syms:
				if i in KEYWORDS:
					self.TOKENS.append([i, 'Keyword'])
				elif i in '+-*/%=':
					self.TOKENS.append([i, 'Operator'])
				elif i.isdigit():
					self.TOKENS.append([i, 'Number'])
				elif i in '({[]})':
					self.TOKENS.append([i, 'Symbol'])
				else:
					self.TOKENS.append([i, 'Function'] if '()' in i else [i, 'Identifier'])
	def printTokens(self):
		for i in self.TOKENS:
			print(i[0]+' => '+i[1])
			
program_file = open('program.c')
lines = program_file.readlines()
LEXICALANALYZER = LexicalAnalyzer(lines)
LEXICALANALYZER.printTokens()
program_file.close()
