
with open("input.txt", "r") as f:
	b = f.read()
	f.close()

lst = b.split(' ')

for i in lst:
	if int(i) % 2 == 0:
		print(i)