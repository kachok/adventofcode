f = open("03b.input","r")

houses={}

line = f.read()

pos_santa=[0,0] # horizontal (left/right), vertical (up/down)
pos_robot=[0,0]

houses["0:0"]=2

curr=0
for item in line:
	if (curr % 2 == 0):

		if (item=="<"):
			pos_santa[0]=pos_santa[0]-1
		if (item==">"):
			pos_santa[0]=pos_santa[0]+1
		if (item=="^"):
			pos_santa[1]=pos_santa[1]+1
		if (item=="v"):
			pos_santa[1]=pos_santa[1]-1

		if not str(pos_santa[0])+":"+str(pos_santa[1]) in houses:
			houses[str(pos_santa[0])+":"+str(pos_santa[1])]=1
		else:
			houses[str(pos_santa[0])+":"+str(pos_santa[1])]=houses[str(pos_santa[0])+":"+str(pos_santa[1])]+1
	if (curr % 2 == 1):

		if (item=="<"):
			pos_robot[0]=pos_robot[0]-1
		if (item==">"):
			pos_robot[0]=pos_robot[0]+1
		if (item=="^"):
			pos_robot[1]=pos_robot[1]+1
		if (item=="v"):
			pos_robot[1]=pos_robot[1]-1

		if not str(pos_robot[0])+":"+str(pos_robot[1]) in houses:
			houses[str(pos_robot[0])+":"+str(pos_robot[1])]=1
		else:
			houses[str(pos_robot[0])+":"+str(pos_robot[1])]=houses[str(pos_robot[0])+":"+str(pos_robot[1])]+1
	curr=curr+1

#print houses

lucky=0
tots=0

for h in houses:
	tots=tots+houses[h]
	if houses[h]>0:
		print h, houses[h]
		lucky=lucky+1

print "# houses", len(houses)

print "lucky", lucky

print "tots", tots #checksum should be equal chars in input +1 (original 0,0 location)
print "line length", len(line)
