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
print s/3
print len(pk)


#exit()

import itertools


low=215971340287000
for var in itertools.permutations(range(0,len(pk)),6):
	#print var
	tots=pk[var[0]]+pk[var[1]]+pk[var[2]]+pk[var[3]]+pk[var[4]]+pk[var[5]]
	if tots==s/3:
		print pk[var[0]],pk[var[1]],pk[var[2]],pk[var[3]],pk[var[4]],pk[var[5]]
		qe=pk[var[0]]*pk[var[1]]*pk[var[2]]*pk[var[3]]*pk[var[4]]*pk[var[5]]

		if qe<low:
			low=qe
		print qe
		print "lowest", low
		print "--"

print low

exit()

for var in pk:

	g1=[]
	g2=[]
	g3=[]
	s1=0
	s2=0
	s3=0

	done=False

	for el in var :
		if s1>s/3 or s2>s/3 or s3>s/3:
			break

		if s1<(s/3):
			g1.append(pk[ len(pk)-el-1])
			s1=s1+pk[len(pk)-el-1]

		elif s2<(s/3):
			g2.append(pk[len(pk)-el-1])
			s2=s2+pk[len(pk)-el-1]
		elif s3<(s/3):
			g3.append(pk[len(pk)-el-1])
			s3=s3+pk[len(pk)-el-1]

		if s1==s/3 or s2==s/3 or s3==s/3:
			done=True

	if done:
		print "done! ", s1,s2,s3,g1,g2,g3
	"""else:
		print ""
		print "----"
		print "bad"
		print var
		print s1,s2,s3,g1,g2,g3
	"""


