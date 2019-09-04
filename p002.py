# Problem 002 - Even Fibonacci Numbers

def fib(n: int) -> int:
    """Iterative implementation of fibonacci numbers"""
    if (n < 2):
        return n

    first = 0
    second = 1   

    if (n >= 2):
        for i in range(2, n):
            second, first = first + second, second
        return second


if __name__ == '__main__':
    i = 0
    total = 0
    value = fib(i)
    while value < 4000000:
        if value % 2 == 0:
            total += value
        i += 1
        value = fib(i)
    print(f'Sum of even-valued terms less than 4m: {total}')