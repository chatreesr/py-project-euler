# Problem 003 - Largest prime factor

target = 600851475143
factor = target
largest_prime = 2
divisor = 2

while factor != 1:
    if factor % divisor == 0:
        factor = factor / divisor
        largest_prime = divisor
    else:
        if divisor == 2:
            divisor = 3
        else:
            divisor += 2

print(f'The largest prime factor of {target} is {largest_prime}')
