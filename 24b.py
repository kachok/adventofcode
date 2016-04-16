f= open("24.input","r")

pk=[]

s=0
count=0

for line in f:
	line=line.replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace(",","").strip().split(" ")[0]
	pk.append(int(line))
	#print line
	s=s+int(line)

print pk
print s
print s/4
print len(pk)


#exit()

import itertools


low=215971340287000
for var in itertools.permutations(range(0,len(pk)),4):
	#print var
	tots=pk[var[0]]+pk[var[1]]+pk[var[2]]+pk[var[3]] #+pk[var[4]]+pk[var[5]]
	if tots==s/4:
		print pk[var[0]],pk[var[1]],pk[var[2]],pk[var[3]] #,pk[var[4]],pk[var[5]]
		qe=pk[var[0]]*pk[var[1]]*pk[var[2]]*pk[var[3]] #*pk[var[4]]*pk[var[5]]

		if qe<low:
			low=qe
		print qe
		print "lowest", low
		print "--"

print low

exit()
