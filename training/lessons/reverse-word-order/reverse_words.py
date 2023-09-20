"""reverse_words.py"""

import argparse
# https://docs.python.org/3/howto/argparse.html

def reverse_order(words):
    list_of_words= words.split(' ')
    list_of_words.reverse() # NOTE: reverse is inplace 
    return ' '.join(list_of_words)

# Use 'eval'-builtin
def format(words, style='title'):
    _format = f'"{words}".{style}()' # dynamically create expression
    print(_format)

    return eval(_format) # evaluate the expression

# Hardcoded expressions
def format2(words, style='title'):
    ''' Explicit coded'''
    if style=='capitalize':
        return words.capitalize()
    elif style=='title':
        return words.title()
    elif style=='lower':
        return words.lower()
    elif style=='upper':
        return words.upper()
    else:
        pass # Never should come here because cli-argument 'format_sytle' defined choices

def main(args):
    if not args.words: # optional-argument
        words = input("words: ")
    else:
        words = args.words

    if args.reverse: # flag
        print(f'args.reverse: {args.reverse}')
        words = reverse_order(words)

    if args.format_style: # optional-argument
        words = format(words, args.format_style)
        #words = format2(words, args.format_style)

    print(words)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--words',
        help='String of blank-separated words e.g. "Hi says Mary"')
    parser.add_argument('--reverse', help='Reverse order flag',
        action='store_true')
    parser.add_argument('--format_style', help='format_style', type=str,
        choices=['capitalize', 'lower', 'upper', 'title'])
    args = parser.parse_args()

    main(args)
