import hashlib

key="ckczppom"

for i in range(1000000):
	m = hashlib.md5()
	m.update(key+str(i))

	if (m.hexdigest()[0:5]=="00000"):
		print i, m.hexdigest()


