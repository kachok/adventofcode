rep=[]

mol=""

bucket=[]

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
		rep.append({"el":cmd[0],"repl":cmd[2]})


print rep
print mol

print "---"

tots=0


def make(input):
	mol=input

	for el in rep:
		num=str.count(mol,el["el"])

		curr=-1
		mol2=""
		for i in range(num):
			#print ">>",curr, mol[curr+1:]
			if curr==-1:
				curr=str.find(mol, el["el"])
			else:
				curr=curr+1+str.find(mol[curr+1:], el["el"])

			#print curr, mol[curr+1:], mol

			#print "<<<",mol[0:curr]+el["repl"]+mol[curr+len(el["el"]):]
			bucket.append(mol[0:curr]+el["repl"]+mol[curr+len(el["el"]):])


	boom=set(bucket)
	return boom

inputs=set(["e"])

count=0

print mol

while True:
	results=set([])
	for m in inputs:
		#print "making from ", m
		prod=make(m)
		results=results.union(prod)


	count=count+1
	print "count(iteration): ", count

	if mol in inputs:
		print ">>>>>!!!!"
		print mol
		#print inputs

		break
	else:
		inputs=results

	print "len of inputs: ", len(inputs)
	maxlen=0
	for s in inputs:
		if len(s)>maxlen:
			maxlen=len(s)
	print "len of longest input", maxlen


print count

'''
print tots
print bucket
print len(bucket)
print boom
'''


