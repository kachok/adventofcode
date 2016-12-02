f = open("08.input","r")
import string

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

	line=string.replace(line,"\\\\","|")
	line=string.replace(line,"\\\"","|")

	count=0
	prev=""
	for char in line:
		count=count+1
		if prev=="\\" and char=="x":
			count=count-3
		prev=char

	chars=chars+count
	print "count", count

	print "tots, chars", tots, chars
	
print "tots", tots
print "chars", chars

print "answer", tots-chars
