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

'''
def ways(arr, vol):
	print "ways", len(arr), vol, arr
	if vol==0:
		return 0
	if len(arr)==1:
		if vol % arr[0] ==0:
			return 1
		else:
			return 0
	else:
		num=1

		count=0 #variations
		#while True:
		if vol >= arr[0]*num:
			sub=ways(arr[1:], vol-arr[0]*num)
			print "sub", sub
			if sub>0:
				count=count+sub				
		#	else:
		#		break
		#	num=num+1
				
		return count




print ways(cont, vol)
'''

vol=150

import itertools

bin=set()
bin.add(0)
bin.add(1)

tots=0

print bin
for x in itertools.product(bin, repeat=len(cont)):
	this=0
	#print x
	for i in range(0, len(cont)):
		this=this+cont[i]*x[i]
	if this==vol:
		print ">>", this, x
		tots=tots+1
	#else:

		#print this, x


print tots