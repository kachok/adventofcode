f = open("01.input","r")

floor=0
count=0

line = f.read()

for item in line:
	if (item=="("):
		#print "up"
		count=count+1
		floor=floor+1
	elif (item==")"):
		#print "down"
		count=count+1
		floor=floor-1

		if (floor==-1):
			print count


	else:
		print "WTF!", item

	#print "count, floor", count, floor

#print line
