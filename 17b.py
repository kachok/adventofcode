f = open("17.input","r")

tots=0

cont=[]

for line in f:
	#print "---"
	line=line.strip()

	cont.append(int(line))

	#print cmd
print cont

tots=0

vol=150

import itertools

bin=set()
bin.add(0)
bin.add(1)

tots=0

m=len(cont)

def num(a):
	s=0
	for x in a:
		s=s+x
	return s


print bin
for x in itertools.product(bin, repeat=len(cont)):
	this=0
	#print x
	for i in range(0, len(cont)):
		this=this+cont[i]*x[i]
	if this==vol:
		print ">>", num(x), this, x
		if num(x)<m:
			m=num(x)
			tots=1
		elif num(x)==m:
			tots=tots+1

	#else:

		#print this, x


print tots, m