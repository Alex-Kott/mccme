n = int(input())

def fact_fract(k):
	r = 1
	for i in range(1,k+1):
		r = r*i
	return 1/r

l = 0
for i in range(n+1):
	l += fact_fract(i)

print(l)