""" Challenge 1: recall factor() prints the factors on an expression.
    Write a program that will ask user to input an expression, calculate its
    factors, and print them. Program should be able to handle invalid input by
    exception handling."""

# Import sympy stuff
from sympy import *

def factorFinder():
    # Define a function to factorize input and print factors in a nice way
    # Also need to do exception handling

    # First get the input
    expr = input("Enter expression to factor: ")

    try:
        output = factor(expr)
        return output
    except ValueError:
        print("haha try again; bad input")
        factorFinder()

if __name__ == '__main__':
    #init_printing()
    pprint(factorFinder())
