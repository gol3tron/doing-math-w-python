""" Challenge 3: Summing a series
    Write a program that finds the sum of an arbitrary series when input is them
    nth term of the series and the number of terms, e.g.
    Enter the nth term: a+(n-1)*d
    Enter the number of terms: 3
    Answer: 3a + 3d
    Note: Not explicitly stated in the text, but in order to get the answer
    shown, need to start series at n=1."""


# Import sympy stuff
from sympy import *

def sumSeries():
    nthTerm = input("Enter the nth term: ")
    nTerms = input("Enter the number of terms: ")

    try:
        expr = sympify(nthTerm)
    except SympifyError:
        print("cant sympify, try again with diff input")

    n = Symbol('n')

    return summation(expr, (n, 1, nTerms))


if __name__ == '__main__':
    pprint(sumSeries())
