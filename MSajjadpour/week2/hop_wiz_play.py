# Print numbers from 0 to 100, replacing multiples of 3 with "Hop", multiples of 5 with "Wiz", and both with "HopWiz"
for i in range(101): print("Hop" * (i % 3 == 0) + "Wiz" * (i % 5 == 0) or i)
