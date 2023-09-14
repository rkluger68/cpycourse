# check_even.py

# Retrieve input from the user.
number = int(input('number: '))

# a mod b is a % b in Python. 
if (number % 2 == 0):
    print(f"The input value {number} is even.")
else:
    print(f"The input value {number} is odd.")
