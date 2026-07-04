# LEft half Pyramid
n = 5

for i in range(n):
	for j in range(n-i):
		print("s",end="")
	for j in range(i+1):
		print("*",end="")
	print()