rep=[]

mol=""

bucket=[]

oldone=set([])

#f = open("19-test.input","r")
f = open("19b-mod.input","r")

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

mol2=mol

count=0
for el in rep:

	if el["repl"].find("Ar")>0:
		mol2=mol2.replace(el["repl"], el["el"])
		print len(mol), len(mol2)

print mol2

def make(input, results):
	mol=input

	for el in rep:
		num=str.count(mol,el["el"])

		if len(mol)>3 and el["el"]=="e":
			continue

		l=len(el["el"])

		curr=-1
		mol2=""
		for i in xrange(num):
			#print ">>",curr, mol[curr+1:]
			if curr==-1:
				curr=str.find(mol, el["el"])
			else:
				curr=curr+1+str.find(mol[curr+1:], el["el"])

			#print curr, mol[curr+1:], mol

			#print "<<<",mol[0:curr]+el["repl"]+mol[curr+len(el["el"]):]
			results.add(mol[0:curr]+el["repl"]+mol[curr+l:])


	#boom=set(bucket)
	#return boom
	return results

inputs=set([mol])

count=0

print mol

oldone=set([])
while True:
	results=set([])
	for m in inputs:
		#print "making from ", m
		prod=make(m, results)
		#results=results.union(prod)
		results=prod


	count=count+1
	print "count(iteration): ", count

	if "e" in inputs:
		print ">>>>>!!!!"
		print mol
		#print inputs

		break
	else:		
		print ">>>>"
		print len(results), len(oldone), len(inputs)
		inputs=results.difference(oldone)
		oldone=oldone.union(results)
		results=inputs
		inputs=results
		print len(results), len(oldone), len(inputs)







	print "len of inputs: ", len(inputs)
	maxlen=0
	minlen=len(mol)+1
	shortest=""
	for s in inputs:
		if len(s)>maxlen:
			maxlen=len(s)
		if len(s)<minlen:
			shortest=s
			minlen=len(s)
	print "len of longest input", maxlen
	print "len of shortest input", minlen
	#inputs=set([shortest])

	oldone=oldone.union(inputs)
	print "len of oldone: ", len(oldone)
	print "len of inputs after pruning: ", len(inputs)


print count

'''
print tots
print bucket
print len(bucket)
print boom
'''


