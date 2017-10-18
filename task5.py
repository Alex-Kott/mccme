n = int(input())

d = n % 10
if d == 0 or d == 5:
	a = 0
	b = n / 5
	print("{} {}".format(a, int(b)))


else:
	for i in range(n):
		for j in range(n):
			if 3*i + 5*j == n:
				print("{} {}".format(int(i), int(j)))
				exit()
	print("IMPOSSIBLE")


