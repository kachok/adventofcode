f = open("05.input","r")

tots=0

for line in f:
	vowels=set(["a","e","i","o","u"])

	bad=set(["ab","cd","pq","xy"])
	isbad=False

	vow=0

	prev=""
	double=False

	print line
	print "---"

	for item in line:
		if item in vowels:
			vow=vow+1
		if item==prev:
			double=True

		if prev+item in bad:
			isbad=True

		prev=item
		#print item


	print vow
	print double
	print isbad

	print "---"

	if vow>=3 and double and  not isbad:
		print "Nice"
		tots=tots+1
	else:
		print "Naughty"


print "tots", tots