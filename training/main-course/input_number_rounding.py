# input_number_rounding.py

import decimal


def input_rounding_digits(default='0'):
    """Get the user input for the number of rounding digits.
    """
    prompt = f'Round to decimal digits [{default}]: '
    while True:
        input_text = input(prompt).strip() or default
        try:
            rounding_digits = int(input_text)
            break
        except ValueError:
            print('Please enter an integer value.')
    return rounding_digits


def input_number(typ=float):
    """Return a number of type 'typ' from user input.
    """
    while True:
        input_text = input('Please enter a number: ').strip()
        try:
            # Handle non-fractional int input separately for correct int
            # rounding.
            number = int(input_text)
            break
        except ValueError:
            try:
                number = typ(input_text)
                break
            except (ValueError, decimal.InvalidOperation) as exc:
                print(exc)
    return number


def input_number_mode(default='float'):
    """Return a number type selected by user input.
    """
    number_types = {
        'float': float,
        'decimal': decimal.Decimal
        }
    while True:
        input_text = input(
            'Please number type (float/decimal) [float]: ').strip() or default
        if input_text in ['float', 'decimal']:
            return number_types[input_text]


def main():
    number_type = input_number_mode()
    rounding_digits = input_rounding_digits()
    while True:
        # Break out with Ctrl-c i.e. KeyboardInterrupt.
        number  = input_number(number_type)
        if rounding_digits == 0:
            rounded_down = int(number)
            if isinstance(number, int):
                rounded_up = rounded_down
            else:
                rounded_up = rounded_down + 1
            print(f'Rounded down: {rounded_down}')
            print(f'Rounded up: {rounded_up}')
        else:
            rounded = round(number, rounding_digits)
            print(f'Rounded to {rounding_digits} digits: {rounded}')


if __name__ == '__main__':
    main()
