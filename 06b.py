lights=[[0 for x in range(1000)] for x in range(1000)] 

#lights[0][0]=1
#lights[9][9]=1

#print lights

f = open("06.input","r")

def turn(bit, start, finish):
	val=0
	if bit=="on":
		val=1

	start=start.split(",")
	start=int(start[0]),int(start[1])
	finish=finish.split(",")
	finish=int(finish[0]),int(finish[1])

	for i in range(start[0]-1,finish[0]):
		for j in range(start[1]-1, finish[1]):
			if bit=="on":
				lights[i][j]=lights[i][j]+1
			else:
				if lights[i][j]>0:
					lights[i][j]=lights[i][j]-1

def toggle(start, finish):
	start=start.split(",")
	start=int(start[0]),int(start[1])
	finish=finish.split(",")
	finish=int(finish[0]),int(finish[1])

	for i in range(start[0]-1,finish[0]):
		for j in range(start[1]-1, finish[1]):
			lights[i][j]=lights[i][j]+2



for line in f:
	line=line.strip()
	cmd=line.split(" ")
	if cmd[0]=="turn":
		turn(cmd[1], cmd[2],cmd[4])
	if cmd[0]=="toggle":
		toggle(cmd[1],cmd[3])
	print cmd

tots=0
for i in range(1000):
	for j in range(1000):
		tots=tots+lights[i][j]

print "tots", tots