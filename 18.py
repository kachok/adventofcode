dim=100

lights=[[0 for x in range(dim+2)] for x in range(dim+2)] 

lights_next=[[0 for x in range(dim+2)] for x in range(dim+2)] 

f = open("18.input","r")

def conv(ch):
	if ch=="#":
		return 1
	else:
		return 0


count=1
for line in f:
	line=line.strip()
	for i in range(dim):
		lights[count][i+1]=conv(list(line)[i])
	count=count+1


def neighbors(x,y):
	return lights[x-1][y-1]+lights[x-1][y]+lights[x-1][y+1]+lights[x][y-1]+lights[x][y+1]+lights[x+1][y-1]+lights[x+1][y]+lights[x+1][y+1]

for i in range(100):
	print i

	for k in range(dim):
		for l in range(dim):
			ne=neighbors(k+1,l+1)
			if ne==3:
				lights_next[k+1][l+1]=1
			elif ne==2 and lights[k+1][l+1]==1:
				lights_next[k+1][l+1]=1
			else:
				lights_next[k+1][l+1]=0
	lights=lights_next
	lights_next=[[0 for x in range(dim+2)] for x in range(dim+2)] 

	for q in range(dim+2):
		print lights[q]

tots=0

for k in range(dim):
	for l in range(dim):
		tots=tots+lights[k+1][l+1]

print "tots",tots
