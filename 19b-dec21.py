rep=[]

mol=""

bucket=[]

oldone=set([])

#f = open("19-test.input","r")
f = open("19.input","r")

lastone=False
for line in f:
	line=line.strip()

	if line=="":
		lastone=True
	elif lastone:
		mol=line.strip()
	else:
		cmd=line.split(" ")
		rep.append({"repl":cmd[0],"el":cmd[2]})


print rep
print mol

print "---"

tots=0


for el in rep:
	if mol.find(el["el"])>-1:
		print el["el"], len(mol.split(el["el"]))

exit()

def reduce(input, depth):
	print depth
	if len(input)==1:
		print "asdasd"
		exit()

	el2=""
	len2=0
	for el in rep:
		if input.find(el["el"])>-1:
			if len(el["el"])>=len2:
				el2=el
				len2=len(el["el"])

	curr=input.find(el2["el"])

	l=len(el2["el"])
	input=input[0:curr]+el2["repl"]+input[curr+l:]

	input=reduce(input, depth+1)

	return input

count=0

input=mol

while True:
	input=reduce(input,0)
	count=count+1
	print count
	print ">", len(input), input


print count



