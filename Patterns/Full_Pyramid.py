#Full Pyramid
n = 5
for i in range(5):
	for j in range(n-i-1):
		print("s",end="")
	for j in range(2*i+1):
		print("*",end="")
	# for j in range(n-i-1):
	# 	print("s",end="")
	print()
