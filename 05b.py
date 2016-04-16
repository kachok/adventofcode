f = open("05b.input","r")

tots=0

for line in f:

	prev=""
	prev2=""

	middle=False

	doubles={}
	double=False

	print line
	print "---"

	curr=0
	for item in line:
		if item==prev2:
			middle=True

		if prev+item in doubles:			
			if curr>=doubles[prev+item]+2:
				double=True
		else:
			doubles[prev+item]=curr


		prev2=prev
		prev=item
		#print item

		curr=curr+1

	print middle
	print double

	print "---"

	if middle and double:
		print "Nice"
		tots=tots+1
	else:
		print "Naughty"


print "tots", tots