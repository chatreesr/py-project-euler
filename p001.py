# Problem 001 - Multiples of 3 and 5

total = sum(n for n in range(1000) if n % 3 == 0 or n % 5 == 0)
print(f'The sum of all the multiples of 3 or 5 below 1000 is {total}')