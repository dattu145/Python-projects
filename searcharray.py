from array import *

arr = array("i",[])
x = int(input("Enter the length ot the array : "))
for i in range(x):
	y = int(input("Enter a number : "))
	arr.append(y)
print(arr)

search = int(input("Enter the number you wonna search :"))

if(search in arr):
	print(arr.index(search))
else:
	print(search,"is not in the array")
		