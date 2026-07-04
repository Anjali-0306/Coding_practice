#Left Aligned Triangle

n = 5
for i in range(n):
	for j in range(i+1):
		print("*",end="")
	print()

print("-"*20)

for i in range(n):
	for j in range(i+1):
		print(j+1,end="")
	print()

print("-"*20)

for i in range(n):
	for j in range(i+1):
		print(i+1,end="")
	print()
