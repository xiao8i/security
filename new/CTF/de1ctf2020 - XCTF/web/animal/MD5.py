from hashlib import md5
for i in range(100000000):
	if md5(str(i).encode()).hexdigest()[:6] == '62c9fc':
		print(i)
		break
# chr() ord()
