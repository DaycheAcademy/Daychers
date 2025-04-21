# Without the use of built-in functions
string_number = '65,777,0.21,0,00009,-333,8487847840,3.14,11111,91,10'

sum_numbers = 0
num = 0
is_negative = False
is_decimal = False
decimal_divisor = 1
decimal_place = 0

for char in string_number + ",":
    if char == "-":
        is_negative = True
    elif char == ".":
        is_decimal = True
    elif "0" <= char <= "9":
        digit = (char == "0") * 0 + (char == "1") * 1 + (char == "2") * 2 + (char == "3") * 3 + \
                (char == "4") * 4 + (char == "5") * 5 + (char == "6") * 6 + (char == "7") * 7 + \
                (char == "8") * 8 + (char == "9") * 9

        if is_decimal:
            decimal_place = decimal_place * 10 + digit
            decimal_divisor *= 10
        else:
            num = num * 10 + digit
    else:
        final_number = num + decimal_place / decimal_divisor
        if is_negative:
            final_number = -final_number

        sum_numbers += final_number


        num = 0
        decimal_place = 0
        decimal_divisor = 1
        is_negative = False
        is_decimal = False

print(f'sum of numbers: {sum_numbers}')






# using built-in functions

string_number = '65,777,0.21,0,00009,-333,8487847840,3.14,11111,91,10'

print(f'sum of numbers: {sum(float(i) for i in string_number.split(","))}')
