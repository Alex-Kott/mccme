from math import ceil

k = int(input()) # котлеты на сковороде
m = int(input()) # минуты
n = int(input()) # кол-во

if n % k == 0:
	r = m * 2 * n
	#r = ceil(n / k) * m * 2
	print(int(r))
else:
	a = 2 * n
	b = ceil(a / k)
	
	print(int(b*m))

