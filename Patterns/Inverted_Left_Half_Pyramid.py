#Inverted Left Half Pyramid

n = 5
for i in range(5):
	for j in range(i):
		print("s",end="")
	for j in range(n-i):
		print("*",end="")
	print()