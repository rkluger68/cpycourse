# add_function.py

def add(x, y):
    """Add x and y and return the result.
    """
    return x + y


def ask_user_input():
    """Read 2 float values x and y from user input and return the tuple (x, y).
    """
    print()
    x = float(input('Please enter number x: '))
    y = float(input('Please enter number y: '))
    return (x, y)


while True:
    x, y = ask_user_input()
    calculated_sum = add(x, y)
    print(f'The sum of x and y is {calculated_sum}.')
    # Read user input, strip leading and trailing whitespace and convert the
    # text to lowercase for normalization.
    proceed = input('Do you want to continue (y/n)? [y] ').strip().lower()
    # If the user just pressed Enter without entering a value we default to
    # 'y'.
    proceed = 'y' if len(proceed) == 0 else proceed
    if proceed != 'y':
        # Break out of the loop - user does not want to continue.
        break
print('Goodbye!')
