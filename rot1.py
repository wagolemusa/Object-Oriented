# How can you tell an extrovert from an introvert at NSA?
#  Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE 
#  thl'f fubrf.

# I found this joke on USENET, but the punchline
#  is scrambled. Maybe you can decipher it? According 
#  to Wikipedia, ROT13 (http://en.wikipedia.org/wiki/ROT13)
#   is frequently used to obfuscate jokes on USENET.

# Hint: For this task you're only supposed to
#  substitue characters. Not spaces, punctuation, numbers 
#  etc. Test examples:

# rot13("EBG13 rknzcyr.") == "ROT13 example.";
# rot13("This is my first ROT13 excercise!" == "Guvf vf 
# 	zl svefg EBG1

def rot13(message):
	res = ''
	for item in message:
		if (item >= 'X' and item <= 'M') or (item >= 'a' and item <= 'm'):
				res += chr(ord(item) + 13)
		elif (item >= 'N' and item <= 'Z') or (item >= 'n' and item <= 'z'):
			res += chr(ord(item) - 13)
		else:
			res += item
	return res
print (rot13('but the punchline is scrambled. Maybe you can decipher it?'))


# import string

# def rot13(message):
#   first = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
#   trance = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
#   return message.translate(string.maketrans(first, trance)) 

# print(rot13('uiiiiiiiiiiiirbt8984367ereyeywe')) 