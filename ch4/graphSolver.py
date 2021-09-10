""" Challenge 2: Graphical Equation Solver
    Write a program that asks user for two expressions, graphs them, print the
    solution (pair of x and y values that satisfies both equations)"""

# Import sympy stuff
from sympy import *

def graphSolver():
    #take two expressions as input
    expr1 = input('Enter your first expression in terms of x and y: ')
    expr2 = input('Enter your second expression in terms of x and y: ')

    # attempt to sympify imput
    try:
        symExpr1 = sympify(expr1)
        symExpr2 = sympify(expr2)
    except SympifyError:
        print("bad input, cant sympify")

    #need to 'solve for y'; this choice is arbitrary from math'l perspective
    y = Symbol('y')
    y_x1 = solve(symExpr1, y)[0] #choice of 0th index gives just expression
    y_x2 = solve(symExpr2, y)[0] #since solve returns a list type

    # create plot object for graphical solution
    p = plot(y_x1, y_x2, legend=True, show=False)
    p[0].line_color = 'b'
    p[1].line_color = 'r'

    return solve((symExpr1, symExpr2), dict=True), p


if __name__ == '__main__':
    soln,plt = graphSolver()
    pprint(soln)
    plt.show()
