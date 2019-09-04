# Problem 004 - Largest palindrome product

# TODO: Make this function work with any n?
def is_palindrome(n: int) -> bool:
    if ( (n // 100000) == (n % 10)  and 
         (n % 100000) // 10000 == (n % 100) // 10 and 
         (n % 10000) // 1000 == (n % 1000) // 100 ):
       return True
    else:
        return False

if __name__ == '__main__':
    largest_palindrome = 0
    n1 = 0
    n2 = 0
    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            k = i * j
            if k > 100000 and is_palindrome(k):
                if largest_palindrome < k:
                    largest_palindrome = k
                    n1 = i
                    n2 = j
    print(f'The largest palindrome product: {n1} x {n2} = {largest_palindrome}')