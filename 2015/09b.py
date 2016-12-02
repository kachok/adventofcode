f = open("09.input","r")
import string
import itertools

dists={}
cities=set()

count=0

for line in f:
	line=line.strip()
	line=line.split(" ")
	if line[0] not in cities:
		cities.add(line[0])
	if line[2] not in cities:
		cities.add(line[2])
	print line
	dists[line[0]+line[2]]=line[4]
	dists[line[2]+line[0]]=line[4]

#print cities

m2=0
for p in itertools.permutations(cities,len(cities)):
	l=len(cities)-1
	d=0
	for i in range(0, l):
		print p[i]+p[i+1]
		d=d+int(dists[p[i]+p[i+1]])

	if m2<d:
		m2=d

print m2