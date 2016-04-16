f = open("14.input","r")

tots=0
deers={}

def hap(s):
	if s=="lose":
		return "-"
	else:
		return ""

for line in f:
	print "---"
	line=line.strip()
	line=line.strip(".")
	cmd=line.split(" ")
	if cmd[0] not in deers.keys():
		deers[cmd[0]]={"fly":int(cmd[3]), "time":int(cmd[6]), "break":int(cmd[13]), "points":0}


	print cmd


tots=2503

for tots in range (1, tots+1):
	m=0
	dd=""

	print tots


	distances={}
	for d in deers:
		#print ">>>"
		#print d
		time=deers[d]["time"]
		fly=deers[d]["fly"]
		wait=deers[d]["break"]

		dist=tots/(time+wait)*time*fly
		#print tots/(time+wait), (tots//(time+wait))*time*fly,  dist, time, fly

		left=tots % (time+wait)

		dist=dist+fly*min(left, time)

		#print d, dist

		distances[d]=dist

		if m<dist:
			m=dist
			dd=d

	for d in distances:
		if distances[d]==m:
			deers[d]["points"]=deers[d]["points"]+1

print "----"
print dd, m, deers[dd]

print "pick max points from list below"	
print deers
