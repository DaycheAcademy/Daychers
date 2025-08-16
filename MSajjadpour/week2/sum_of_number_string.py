numberString = '76,876532,9.356,0,0.23,-234,6,87586,987,142526353526353526,6454737364654,-0.375'

# Split string by commas
numbers = numberString.split(',')

total_sum = 0

for num_str in numbers:
    # Convert each number string to float (handles integers and decimals, including negatives)
    total_sum += float(num_str)

print("Sum of numbers:", total_sum)
