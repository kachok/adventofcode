f = open("08.input","r")

tots=0
chars=0

for line in f:
	print "---"
	#line=line.strip()
	#cmd=line.split(" ")
	print line
	print "len",len(line)
	tots=tots+len(line)

	#remove quotes
	line=line[1:-1]
	print line

	count=0
	prev=""
	for char in line:
		count=count+1
		if prev=="\\" and char=="\\":
			count=count-1
		elif prev=="\\" and char=="\"":
			count=count-1
		elif prev=="\\" and char=="x":
			count=count-3
		prev=char

	chars=chars+count
	print "count", count

	print "tots, chars", tots, chars
	
print "tots", tots
print "chars", chars

print "answer", tots-chars
