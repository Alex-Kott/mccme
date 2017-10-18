
with open("input.txt", "r") as f:
	b = f.read()
	f.close()

# lst = b.split(' ')

for i in range(1, int(b)+1):
	if i**2 <= int(b):
		print(i**2)