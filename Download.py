#!/usr/bin/env python

def deaccent(unistr):
    return "".join(aChar 
                   for aChar in unicodedata.normalize("NFD", unistr) 
                   if not unicodedata.combining(aChar))
