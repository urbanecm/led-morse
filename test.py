#!/usr/bin/env python

import Module

text = raw_input("Text: ")

codes = Module.textToCode(text)

for code in codes:
	Module.signalizeChar(code)
