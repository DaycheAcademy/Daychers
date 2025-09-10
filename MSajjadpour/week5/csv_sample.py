
emails = []
numbers = []
first_names = []
last_names = []

with open("csv_sample", "r") as f:
    for line in f:
        # Remove newline and split by ";"
        parts = line.strip().split(";")
        if len(parts) == 4:
            emails.append(parts[0])
            numbers.append(parts[1])
            first_names.append(parts[2])
            last_names.append(parts[3])

print("Emails:", emails)
print("Numbers:", numbers)
print("First Names:", first_names)
print("Last Names:", last_names)