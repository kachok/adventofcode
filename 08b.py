f = open("08.input","r")
import string

tots=0
new=0

for line in f:
	print "---"
	line=line.strip()
	#cmd=line.split(" ")
	print line
	print "len",len(line)
	tots=tots+len(line)

	line=string.replace(line,"\"","||")
	line=string.replace(line,"\\","||")
	print line
	new=new+len(line)+2
	#remove quotes

	
print "tots", tots
print "new", new

print "answer", new-tots
