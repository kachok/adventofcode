f = open("13.input","r")

tots=0
people={}

def hap(s):
	if s=="lose":
		return "-"
	else:
		return ""

for line in f:
	print "---"
	line=line.strip()
	line=line.strip(".")
	cmd=line.split(" ")
	if cmd[0] not in people.keys():
		people[cmd[0]]={}

	people[cmd[0]][cmd[10]]=int(hap(cmd[2])+cmd[3])

	print cmd

	
print "tots", tots
print people

people["myself"]={}



import string
import itertools


def calc(seats):
	h=0
	for i in range(0,len(seats)):
		curr=seats[i]


		print curr, i

		if i==0:
			if seats[len(seats)-1] in people[curr]:
				h=h+people[curr][seats[len(seats)-1]]

			if seats[i+1] in people[curr]:
				h=h+people[curr][seats[i+1]]
		elif i==len(seats)-1:
			if seats[i-1] in people[curr]:
				h=h+people[curr][seats[i-1]]

			if seats[0] in people[curr]:
				h=h+people[curr][seats[0]]
		else:
			#print ">>>",people[people.keys()[i]]
			if seats[i-1] in people[curr]:
				h=h+people[curr][seats[i-1]]

			if seats[i+1] in people[curr]:
				h=h+people[curr][seats[i+1]]
			print h
	
	print "h", h
	return h

m=0

for p in itertools.permutations(people,len(people)):
	print "permutation", p
	c=calc(p)
	if c>m:
		m=c

print "max", m