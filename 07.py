wires=[]

inputs={}

f = open("07.input","r")


def run(cmd):
	print cmd
	if cmd[0]=="NOT":
		if str.isdigit(cmd[1]):
			inputs[cmd[3]]=~int(cmd[1])
		else:
			inputs[cmd[3]]=~int(inputs[cmd[1]])
	else:
		if str.isdigit(cmd[0]):
			a=int(cmd[0])
		else:
			a=int(inputs[cmd[0]])

		if str.isdigit(cmd[2]):
			b=int(cmd[2])
		else:
			b=int(inputs[cmd[2]])

		if cmd[1]=="AND":
			inputs[cmd[4]]=a & b
		if cmd[1]=="OR":
			inputs[cmd[4]]=a | b
		if cmd[1]=="LSHIFT":
			inputs[cmd[4]]=a << b
		if cmd[1]=="RSHIFT":
			inputs[cmd[4]]=a >> b

for line in f:
	line=line.strip()
	cmd=line.split(" ")
	#print cmd
	wires.append(cmd)


#print wires
#print inputs



while len(wires)>0:
	curr=wires.pop(0)

	if curr[1]=="->":
		if str.isdigit(curr[0]):
			print "executed", curr
			inputs[curr[2]]=int(curr[0])
		elif curr[0] in inputs:
			print "executed", curr
			inputs[curr[2]]=int(inputs[curr[0]])
		else:
			#print "append ", curr
			wires.append(curr)

	elif curr[0]=="NOT":
		if (curr[1] in inputs or str.isdigit(curr[1])):
			#print "inputs", inputs
			print "run", curr
			run(curr)
		else:
			#print "append ", curr
			wires.append(curr)
	else:
		if (curr[0] in inputs or str.isdigit(curr[0]))and (curr[2] in inputs  or str.isdigit(curr[2])):
			print "run", curr
			run(curr)
		else:
			#print "append ", curr
			wires.append(curr)

	#print "len", len(wires)


print "inputs[a]", inputs["a"]