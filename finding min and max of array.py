numbers = [5,8,64,29,55]
max = numbers[0]
min = numbers[0]
for i in range(len(numbers)):
	if numbers[i] > max:
		max = numbers[i]
	if numbers[i] < min:
		min = numbers[i]
		
print(max)
print(min)