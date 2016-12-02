def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


print factors(10)

count=1

print factors(1049160)

s=0
for i in factors(1049160):
	s=s+i*10

print s

#exit()


presents=36000000

m=50

while True:
	print "count", count
	s=0
	for el in factors(count):
		if el*50>=count:
			s=s+el*11

	print s

	if s>=presents:
		print s
		break

	count=count+1