# Inverted Full Pyramid
n = 5

for i in range(n):
	for j in range(i):
		print("s",end="")
	for j in range(2*(n-i)-1):
		print("*",end="")
	print()