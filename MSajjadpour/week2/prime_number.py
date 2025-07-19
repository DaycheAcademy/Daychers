# Loop through numbers from 2 to 1000 (1 is not a prime)
for num in range(2, 1001):
    # Check if the number is divisible by any number from 2 to sqrt(num)
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            break  # Not a prime number
    else:
        # This else runs only if the loop is NOT broken (i.e., num is prime)
        print(num)
