ps="cqjxjnds"

def next(s):
	s=s[0:7]+chr(ord(s[7])+1)

	for i in range(0,7):
		#print i

		if chr(ord(s[7-i]))>"z":
			s=s[0:7-i]+"a"+s[8-i:]
			s=s[0:7-i-1]+ chr(ord(s[7-1-i])+1)  +s[8-1-i:]
		#print ">>",s
	return s


def test(s):
	valid=True

	if s.find("i")>0:
		valid=False
	if s.find("o")>0:
		valid=False
	if s.find("l")>0:
		valid=False

	rsame=False
	rinc=False

	samecount=0
	same=0
	inc=0
	for i in range(1,8):
		#print ">",i
		if s[i]==s[i-1]:
			same=same+1
		else:
			same=0

		if same==1:
			samecount=samecount+1

		if ord(s[i])==ord(s[i-1])+1:
			inc=inc+1
		else:
			inc=0

		if samecount>=2:
			rsame=True

		if inc==2:
			rinc=True

			print ">>>>>>>>>>"

	print s, valid, rsame, rinc, same, inc, samecount

	return valid and rsame and rinc

while True:
	#print ps
	ps=next(ps)

	if test(ps):
		print "yes - ", ps
		break


while True:
	#print ps
	ps=next(ps)

	if test(ps):
		print "yes - ", ps
		break

