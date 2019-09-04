# Problem 005 - Smallest Multiples

commons = [i for i in range(2, 21)]
divisors = [2, 3, 5, 7, 11, 13, 17, 19]
smallest_multiple = 1

# Ugly method but this will do (temporarily)
# TODO: Think of a better way to solve this problem
idx = 0
print(f'Original: {commons}')
while sum(commons) != len(commons):
    saved = 0
    for i in range(len(commons)):
        if commons[i] % divisors[idx] == 0:
            commons[i] = int(commons[i] / divisors[idx])
            saved += 1

    if saved > 0:
        smallest_multiple *= divisors[idx]
        print(f'Divisor: {divisors[idx]} - {commons}')
    else:
        idx += 1

print(f'Smallest Multiple: {smallest_multiple}')