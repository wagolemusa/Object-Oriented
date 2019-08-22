# There’s a classic coding interview question named FizzBuzz that can be solved by iterating over both indices and values. In FizzBuzz, you are given a list of integers. Your task is to do the following:

#     Replace all integers that are evenly divisible by 3 with "fizz"
#     Replace all integers divisible by 5 with "buzz"
#     Replace all integers divisible by both 3 and 5 with "fizzbuzz"

# Often, developers will solve this problem with range():


numbers = [45, 22, 14, 65, 97, 72]

for i in range(len(numbers)):
	if numbers[i] % 3 == 0 and numbers[i] % 5 == 0:
		numbers[i] = 'fizzbuzz'
	elif numbers[i] % 3 == 0:
		numbers[i] = 'fizz'
	elif numbers[i] % 5 == 0:
		numbers[i] = 'buzz'
	elif numbers[i] % 2 == 0:
		numbers[i] = 'refuge'

print (numbers)