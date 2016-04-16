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


presents=3600000

while True:
	print "count", count
	s=0
	for el in factors(count):
		s=s+el*1

	print s

	if s>=presents:
		print s
		break

	count=count+1