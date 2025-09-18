hopWiz = ["HopWiz" if num % 3 == 0 and num % 5 == 0 else("Hop" if num % 3 == 0 else ("Wiz" if num % 5 == 0  else (str(num)))) for num in range (1,101)]
print(hopWiz)