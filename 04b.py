import hashlib

key="ckczppom"

for i in range(10000000):
	m = hashlib.md5()
	m.update(key+str(i))

	if (m.hexdigest()[0:6]=="000000"):
		print i, m.hexdigest()


