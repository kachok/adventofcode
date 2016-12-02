f = open("12.json","r")

data = f.read()

import json

j=json.loads(data)

tots=0

def count(o):
	global tots
	#print ">>>>o", type(o), o

	for i in o:
		#print "i",i
		if type(o) is list:
			el=i
		if type(o) is dict:
			el=o[i]

		if type(el) is list or type(el) is dict:
			#print
			#print "---"
			count(el)
		if type(el) is int:
			tots=tots+int(el)
		if type(el) is str and is_number(el):
			tots=tots+int(el)


#print j
count(j)

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

print "tots", tots

