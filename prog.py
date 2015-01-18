#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Module
import sys

try:
	while True:
		print "Zvolte činnost: "
		print "1) Převádění"
		print "2) Signalizace"
		print "3) Konec"
		
		action = raw_input("Činnost: ")
		
		if (action == "1"):
			print "1) Text -> morseovka"
			print "2) Morseovka -> test"
			print "3) Zpět"
			action = raw_input("Činnost: ")
			if (action == "1"):
				text = raw_input("Zadejte text k převedení do morseovky (bez diakritiky): ")
				codes = Module.textToCode(text)
				for code in codes:
					print code
			elif (action == "2"):
				print "Zadejte text psaný morseovkou (jeden znak, jeden řádek)"
				print "Zadávání ukončete stiskem enter"
				code = Module.readCode()
				text = Module.codeToText(code)
				print "Text převedený z morseovky: ", text
			elif (action == "3)"):
				continue
			else:
				print "Zvolena nesprávná akce"
		elif (action == "2"):
			pass
		elif (action == "3"):
			break
		else:
			print "Zvolena nesprávná akce"
except KeyboardInterrupt:
	print
	sys.exit()

