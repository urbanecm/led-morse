#!/usr/bin/env python

def textToCode(text):
	array = list(text)
	delka = len(array)
	morse = []
	i = 0
	while (i < delka):
		morse.append(charToCode(array[i]))
		i = i + 1
	return morse

def charToCode(zpracovat):
	char = zpracovat.upper()
	vratit = ""
	if (char == "A"):
		vratit = ".-"
	elif (char == "B"):
		vratit = "-..."
	elif (char == "C"):
		vratit = "-.-."
	elif (char == "D"):
		vratit = "-.."
	elif (char == "E"):
		vratit = "."
	elif (char == "F"):
		vratit = "..-."
	elif (char == "G"):
		vratit = "--."
	elif (char == "H"):
		vratit = "...."
	elif (char == "CH"):
		vratit = "----"
	elif (char == "I"):
		vratit = ".."
	elif (char == "J"):
		vratit = ".---"
	elif (char == "K"):
		vratit = "-.-"
	elif (char == "L"):
		vratit = ".-.."
	elif (char == "M"):
		vratit = "--"
	elif (char == "N"):
		vratit = "-."
	elif (char == "O"):
		vratit = "---"
	elif (char == "P"):
		vratit = ".--."
	elif (char == "Q"):
		vratit = "--.-"
	elif (char == "R"):
		vratit = ".-."
	elif (char == "S"):
		vratit = "..."
	elif (char == "T"):
		vratit = "-"
	elif (char == "U"):
		vratit = "..-"
	elif (char == "V"):
		vratit = "...-"
	elif (char == "W"):
		vratit = ".--"
	elif (char == "X"):
		vratit = "-..-"
	elif (char == "Y"):
		vratit = "-.--"
	elif (char == "Z"):
		vratit = "--.."
	return vratit
def codeToText(code):
	delka = len(code)
	texta = []
	i = 0
	while (i < delka):
		texta.append(codeToChar(code[i]))
		i = i + 1
	text = ''.join(texta)
	return text

def codeToChar(code):
	if (code == ".-"):
		vratit = "A"
	elif (code == "-..."):
		vratit = "B"
	elif (code == "-.-."):
		vratit = "C"
	elif (code == "-.."):
		vratit = "D"
	elif (code == "."):
		vratit = "E"
	elif (code == "..-."):
		vratit = "F"
	elif (code == "--."):
		vratit = "G"
	elif (code == "...."):
		vratit = "H"
	elif (code == "----"):
		vratit = "CH"
	elif (code == ".."):
		vratit = "I"
	elif (code == ".---"):
		vratit = "J"
	elif (code == "-.-"):
		vratit = "K"
	elif (code == ".-.."):
		vratit = "L"
	elif (code == "--"):
		vratit = "M"
	elif (code == "-."):
		vratit = "N"
	elif (code == "---"):
		vratit = "O"
	elif (code == ".--."):
		vratit = "P"
	elif (code == "--.-"):
		vratit = "Q"
	elif (code == ".-."):
		vratit = "R"
	elif (code == "..."):
		vratit = "S"
	elif (code == "-"):
		vratit = "T"
	elif (code == "..-"):
		vratit = "U"
	elif (code == "...-"):
		vratit = "V"
	elif (code == ".--"):
		vratit = "W"
	elif (code == "-..-"):
		vratit = "X"
	elif (code == "-.--"):
		vratit = "Y"
	elif (code == "--.."):
		vratit = "Z"
	return vratit
