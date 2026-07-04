#Inverted Right Half Pyramid
n = 5
for i in range(n,0,-1):
	for j in range(i):
		print("*",end="")

	print()

print("-"*20)

for i in range(n):
	for j in range(n-i):
		print("*",end="")

	print()

print("-"*20)

for i in range(1,n+1):
	for j in range(n-i+1):
		print(j+1,end="")

	print()