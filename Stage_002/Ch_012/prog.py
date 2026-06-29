# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 15:24:42 2026

@author: moxey
"""

# Positional arugments
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("square", help="display a square of a given number", type=int)
# args = parser.parse_args()
# print(args.square**2)


# Optional arugments 
# import argparse 
# parser = argparse.ArgumentParser()
# parser.add_argument("-v","--verbosity", help="increase output verbosity", action='store_true')
# args =  parser.parse_args()
# if args.verbosity:
#     print('verbosity turned on')



# Combing Posittional and Optional arguments
# import argparse 
# parser = argparse.ArgumentParser()
# parser.add_argument("square", type=int,
#                     help="display a squre of a give number")
# parser.add_argument("-v","--verbosity", action="count", default=0,
#                     help="increase output verbosity")
# args = parser.parse_args()
# answer  = args.square**2
# if args.verbosity >= 2:
#     print(f"the square of {args.square} equals {answer}")
# elif args.verbosity >= 1:
#     print(f"the square of {args.square}^2 == {answer}")
# else:
#     print(answer)



# Getting a litte more advance
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("x", type=int, help="the base")
# parser.add_argument("y",type=int, help="the exponent")
# parser.add_argument("-v", "--verbosity", action="count", default=0)
# args = parser.parse_args()
# answer = args.x**args.y 
# if args.verbosity >= 2:
#     print(f"{args.x} to the power {args.y} equals {answer}")
# elif args.verbosity >= 1:
#     print(f"{args.x}^{args.y} == {answer}")
# else:
#     print(answer)
# if args.verbosity >= 2:
#     print(f"Running '{__file__}'")
# if args.verbosity >= 1:
#     print(f"{args.x}^{args.y} == ", end="")
# print(answer)



# Specifying ambigous arguments 
# import argparse
# parser = argparse.ArgumentParser(prog='PROG')
# parser.add_argument('-n', nargs='+') #  one or more values
# parser.add_argument('args', nargs='*') # zero or more values

# # ambigous, so parse_args assuymes it's an option
# # parser.parse_args(['-f'])

# parse = parser.parse_args(['--','-f'])
# print(parse)

# # ambigous, so the -n option greedily accepts arguments
# parse = parser.parse_args(['-n','1','2','3'])
# print(parse)

# parse = parser.parse_args(['-n','1','--','2','3'])
# print(parse)


# Conflicting options 
# import argparse
# parser = argparse.ArgumentParser(description="calculate X to the power of Y")
# group = parser.add_mutually_exclusive_group()
# group.add_argument("-v","--verbose", action="store_true")
# group.add_argument("-q", "--quiet", action="store_true")
# parser.add_argument("x", type=int, help="the base")
# parser.add_argument("y", type=int, help="the exponent")
# args = parser.parse_args()
# answer = args.x**args.y 

# if args.quiet:
#     print(answer)
# elif args.verbose:
#     print(f"{args.x} to the power {args.y} equals {answer}")
# else:
#     print(f"{args.x}^{args.y} == {answer}")


# print(argparse.__file__)


# Custom type converters 
import argparse
parser = argparse.ArgumentParser(prefix_chars="-+")
parser.add_argument('-a', metavar='<value>', action="append", type=lambda x: ('-', x))
parser.add_argument('+a',metavar='<value>', action="append", type=lambda x: ('+', x))
args = parser.parse_args()
print(args)

