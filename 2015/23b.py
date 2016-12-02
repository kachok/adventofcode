f= open("23.input","r")

cmd=[]

for line in f:
	line=line.replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace(",","").strip().split(" ")
	cmd.append(line)
	#print line

a=1
b=0
curr=0

print cmd

while curr<len(cmd) and curr>=0:
	print "curr:",curr, "a:",a,"b:",b,cmd[curr]
	com=cmd[curr]

	if com[0]=="hlf":
		if com[1]=="a":
			a=a/2
		if com[1]=="b":
			b=b/2
		curr=curr+1
	elif com[0]=="tpl":
		if com[1]=="a":
			a=a*3
		if com[1]=="b":
			b=b*3
		curr=curr+1

	elif com[0]=="inc":
		if com[1]=="a":
			a=a+1
		if com[1]=="b":
			b=b+1
		curr=curr+1

	elif com[0]=="jmp":
		curr=curr+int(com[1])
	elif com[0]=="jie":
		if com[1]=="a" and a %2==0:
			curr=curr+int(com[2])
		elif com[1]=="b" and b %2==0:
			curr=curr+int(com[2])
		else:
			curr=curr+1

	elif com[0]=="jio":
		#print "jio"
		if com[1]=="a" and a ==1:
			curr=curr+int(com[2])
		elif com[1]=="b" and b ==1:
			curr=curr+int(com[2])
		else:
			curr=curr+1


print "curr:",curr, "a:",a,"b:",b

"""
hlf r sets register r to half its current value, then continues with the next instruction.
tpl r sets register r to triple its current value, then continues with the next instruction.
inc r increments register r, adding 1 to it, then continues with the next instruction.
jmp offset is a jump; it continues with the instruction offset away relative to itself.
jie r, offset is like jmp, but only jumps if register r is even ("jump if even").
jio r, offset is like jmp, but only jumps if register r is 1 ("jump if one", not odd).
"""




