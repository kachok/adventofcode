
times=40

def doit(s):
	count=0
	prev=""

	s2=""

	for d in s:
		#print d
		if prev=="":
			prev=d
			count=1
		elif prev==d:
			count=count+1
		else:
			s2=s2+str(count)+str(prev)
			prev=d
			count=1

	s2=s2+str(count)+str(prev)
	#print s2
	return s2

s="1113122113"
for i in range(0,times):
	print i, ">>>>>>"
	s=doit(s)
	print i, len(s)
