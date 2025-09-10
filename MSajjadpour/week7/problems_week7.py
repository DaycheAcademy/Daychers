# 1- Rewrite factorial without using recursion

def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Example usage
print(factorial(5))
print('=' * 40)
# 2 - Range to generate : range(2.3, 3.78, 0.01)


def float_range(start, stop, step):
    while start < stop:
        yield round(start, 10)  # round to avoid floating point issues
        start += step


# Example usage
for num in float_range(2.3, 3.78, 0.01):
    print(num)

print('=' * 40)

# 3 - Range to generate : range(c, x, 2)


def char_range(start, stop, step=1):
    for code in range(ord(start), ord(stop) + 1, step):
        yield chr(code)


# Example usage
for ch in char_range('c', 'x', 2):
    print(ch)
