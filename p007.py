# Problem 007 -- The 10,001st prime number
import math

# attempt 0 - the brute force trial division :)
def is_prime(n: int) -> bool:
    if n == 1:
        return False

    if n == 2:
        return True

    # 2 is the only prime number
    if n % 2 == 0:
        return False

    i = 3
    while i <= math.floor(math.sqrt(n)):
        if n % i == 0:
            return False
        i += 1
    
    return True

if __name__ == '__main__':
    position = 10001
    count = 0
    roll = 1
    while True:
        if is_prime(roll):
            print(f'#{count} = {roll}')
            count += 1
        
        if count == position:
            break;

        roll += 1

    print(f'{roll}')
        