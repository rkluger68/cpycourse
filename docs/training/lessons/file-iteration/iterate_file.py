""" interate_file"""
#import sys
import argparse
# https://docs.python.org/3/howto/argparse.html

def gen(lines, separator=','):
    print(lines)
    #_lines = lines.split(separator)
    for line in lines:
        for _line in line.split(separator):
            yield _line

def main(args):
    if not args.input_file: # optional-argument
        input_file = input("input_file: ")
    else:
        input_file = args.input_file

    with open(input_file) as my_input_file:
        if args.output_file:
            if args.output_separator:
                out_separator = args.output_separator
            else:
                out_separator = "\n"
            with open(args.output_file, 'w') as my_output_file:
                for line in gen(my_input_file.readlines()):
                    my_output_file.write(line.rstrip()+ out_separator) # rstrip(): removes trailing whitespaces and newlines
        else:
            for line in gen(my_input_file.readlines()):
                print(line.rstrip()) # rstrip(): removes trailing whitespaces and newlines


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', help='Path to file"')
    parser.add_argument('--input_separator', help='line separator of input file')
    parser.add_argument('--output_file', help='Path to file"')
    parser.add_argument('--output_separator', help='line separator of output file')

    args = parser.parse_args()

    main(args)