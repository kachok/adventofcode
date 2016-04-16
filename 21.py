def play(u1,u2,u3, e1,e2,e3):
	#points, damage, armor
	outcome=False

	while u1>0 or e1>0:
		e1=e1-max(1, u2-e3)
		print "player attacks boss", e1

		if e1<=0:
			return True

		u1=u1-max(1,e2-u3)
		print "boss attacks player", u1

		if u1<=0:
			return False

	if u1>0:
		return True
	if u1<=0:
		return False


#play(8,5,5,12,7,2)

#play(100,4,0,100,8,2)

#exit()


f = open("21.input","r")

line=f.readline().strip().split(":")[1]
e1=int(line)
line=f.readline().strip().split(":")[1]
e2=int(line)
line=f.readline().strip().split(":")[1]
e3=int(line)

print e1,e2,e3

f= open("21.store","r")

count=0
rings={}
armors={}
weapons={}
for line in f:
	count=count+1

	line=line.replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").strip().split(" ")
	#print line

	if count>15:
		#add ring
		item={"cost":int(line[1]),"damage":int(line[2]),"armor":int(line[3])}
		rings[line[0]]=item
	elif count>8 and count<14:
		#add armor
		item={"cost":int(line[1]),"damage":int(line[2]),"armor":int(line[3])}
		armors[line[0]]=item
	elif count>1 and count<7:
		#add weapon
		item={"cost":int(line[1]),"damage":int(line[2]),"armor":int(line[3])}
		weapons[line[0]]=item

armors["none"]={"cost":0,"damage":0,"armor":0}
rings["none1"]={"cost":0,"damage":0,"armor":0}
rings["none2"]={"cost":0,"damage":0,"armor":0}


#print rings, armors, weapons


cheap=100000
for w in weapons:
	for a in armors:
		for r1 in rings:
			for r2 in rings:
				if r1!=r2:
					#print w,a,r1,r2
					u1=100
					u2=weapons[w]["damage"]+armors[a]["damage"]+rings[r1]["damage"]+rings[r2]["damage"]
					u3=weapons[w]["armor"]+armors[a]["armor"]+rings[r1]["armor"]+rings[r2]["armor"]
					cost=weapons[w]["cost"]+armors[a]["cost"]+rings[r1]["cost"]+rings[r2]["cost"]

					if play(u1,u2,u3,e1,e2,e3):
						#print cost
						if cost==8:
							print w,a,r1,r2
							print u1,u2,u3,e1,e2,e3
							print "cheap ", cost
						if cheap>cost:
							cheap=cost

print cheap



