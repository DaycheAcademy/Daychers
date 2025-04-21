numbers = []
while  (num:=input('enter numbers and press q:')) != 'q':
    numbers.append(float(num))
print(f'average is : {sum(numbers) / len(numbers)}')





print('----------------------------------------------------------------')
numbers = []
while (num := input('Enter a number (or q to finish): ')) != 'q':
    try:
        numbers.append(float(num))
    except ValueError:
        print("Invalid input. Please enter a number or 'q' to finish.")
if numbers:
    print(sum(numbers) / len(numbers))
else:
    print("No numbers were entered.")





print('----------------------------------------------------------------')
numbers = []
while True :
    numbers.append(float(num := input('enter numbers and press q:')))
    if num == 'q':
        break
print(f'average is : {sum(numbers) / len(numbers)}')



