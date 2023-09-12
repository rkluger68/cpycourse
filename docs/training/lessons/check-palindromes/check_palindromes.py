"""check_palindromes.py
"""

import sys


def is_palindrome(text):
    """Check if text is a palindrome.
    """
    reversed_text = ''.join(reversed(text))
    return text == reversed_text


def is_palindrome_ext_slicing(text):
    reversed_text = text[::-1]
    return text == reversed_text


def is_palindrome_loop(text):
    reversed_order = []
    for idx, character in enumerate(text):
        idx_back = -(idx + 1)
        if text[idx] != text[idx_back]:
            return False 
    return True


def parse_args(args=None):
    """Parse arguments from sys.argv if args is None (the default) or from args
    sequence otherwise.
    """
    # https://docs.python.org/3/howto/argparse.html
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'texts', nargs='*',
        help='One or more palindrome candidate texts')
    args = parser.parse_args(args)
    return args


def main(args=None):
    """Main module function.
    
    Exposes this module's executable functionality for use as a module
    function. 
    Parses arguments from sys.argv if args is None (the default) or from args
    sequence otherwise.
    """
    args = parse_args(args)
    if not args.texts:
        # optional-argument
        text = input("text: ")
        texts = [text]
    else:
        texts = args.texts

    for text in texts:
        print(f'\nentered text: {text}')
        print(f'reverse text: {text[::-1]}')
        for method in [
                is_palindrome,
                is_palindrome_ext_slicing,
                is_palindrome_loop
                ]:
            print(f'{method.__name__}("{text}") --> {method(text)}')


if __name__ == "__main__":
    sys.exit(main())
