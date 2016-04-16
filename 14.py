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
		deers[cmd[0]]={"fly":int(cmd[3]), "time":int(cmd[6]), "break":int(cmd[13])}


	print cmd

m=0
dd=""

tots=2503

#tots=1000

for d in deers:
	print ">>>"
	print d
	time=deers[d]["time"]
	fly=deers[d]["fly"]
	wait=deers[d]["break"]

	dist=tots/(time+wait)*time*fly
	print tots/(time+wait), (tots//(time+wait))*time*fly,  dist, time, fly

	left=tots % (time+wait)

	dist=dist+fly*min(left, time)

	print d, dist

	if m<dist:
		m=dist
		dd=d


print "----"
print dd, m
	
