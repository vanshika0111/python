# creating command line utility

import argparse
import sys 

def calc(args):
    if args.o == 'add':
        return args.x + args.y
    elif args.o == 'sub':
        return args.x - args.y
    elif args.o == 'mul':
        return args.x * args.y
    elif args.o == 'div':
        return args.x / args.y
    else:
        return "something went wrong."

if __name__ == '__main__':
    parser  = argparse.ArgumentParser()
    parser.add_argument('--x', type = float, default = 1.0,
                        help = "Enter first number. Please try agian")
    parser.add_argument('--y', type = float, default = 3.0,
                        help = "Enter first number. Please try agian")
    parser.add_argument('--o', type = str, default = "add",
                        help = "Please try agian for more.")
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))

"""
Steps to be followed on windows power shell:
1. cd
2. cd <path>
3. --x 6 --y 2 --o add
4. --x 6 --y 2 --o sub
5. --x 6 --y 2 --o mul
6. --x 6 --y 2 --o div
"""
    