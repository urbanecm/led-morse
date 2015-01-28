#!/usr/bin/env python

array = []
word = []
text = "abc abc abc"
text += " "
for char in text:
	print char
	if char == " ":
		array.append("".join(word))
		word = [] 
	elif char == "\n":
		array.append("".join(word))
		word = []
	else:
		word.append(char)
print array
