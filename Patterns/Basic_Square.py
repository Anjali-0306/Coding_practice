#Basic Square Pattern

# *****
# *****
# *****
# *****
# *****
n = 5
for i in range(n):
	for j in range(n):
		print("* ",end="")
	print()

print("-"*20)
#Pythonic way
for i in range(n):
	print("* "*n)
	