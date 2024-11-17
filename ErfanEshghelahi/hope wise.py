print('\n'.join(
    'Hope Fizz' if i % 3 == 0 and i % 5 == 0 else
    'Hope' if i % 3 == 0 else
    'Fizz' if i % 5 == 0 else
    str(i)
    for i in range(1, 101)
))