f = open("03.input","r")

houses={}

line = f.read()

pos=[0,0] # horizontal (left/right), vertical (up/down)
houses["0:0"]=1

for item in line:
	if (item=="<"):
		pos[0]=pos[0]-1
	if (item==">"):
		pos[0]=pos[0]+1
	if (item=="^"):
		pos[1]=pos[1]+1
	if (item=="v"):
		pos[1]=pos[1]-1

	if not str(pos[0])+":"+str(pos[1]) in houses:
		houses[str(pos[0])+":"+str(pos[1])]=1
	else:
		houses[str(pos[0])+":"+str(pos[1])]=houses[str(pos[0])+":"+str(pos[1])]+1


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
