#!/usr/bin/env python

import unicodedata

def deaccent(text):
    unistr = text.decode('unicode-escape')
    return "".join(aChar 
                   for aChar in unicodedata.normalize("NFD", unistr) 
                   if not unicodedata.combining(aChar))
