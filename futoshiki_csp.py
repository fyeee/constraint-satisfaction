#Look for #IMPLEMENT tags in this file.
'''
All models need to return a CSP object, and a list of lists of Variable objects 
representing the board. The returned list of lists is used to access the 
solution. 

For example, after these three lines of code

    csp, var_array = futoshiki_csp_model_1(board)
    solver = BT(csp)
    solver.bt_search(prop_FC, var_ord)

var_array[0][0].get_assigned_value() should be the correct value in the top left
cell of the Futoshiki puzzle.

1. futoshiki_csp_model_1 (worth 20/100 marks)
    - A model of a Futoshiki grid built using only 
      binary not-equal constraints for both the row and column constraints.

2. futoshiki_csp_model_2 (worth 20/100 marks)
    - A model of a Futoshiki grid built using only n-ary 
      all-different constraints for both the row and column constraints. 

'''
from cspbase import *
import itertools


def futoshiki_csp_model_1(futo_grid):
    size = len(futo_grid)
    dom = []
    for i in range(1, size + 1):
        dom.append(i)
    vars = []
    for i in range(size):
        row = []
        for j in range(0, size, 2):
            row.append(Variable('Q({0}, {1})'.format(i + 1, j // 2 + 1), dom))
        vars.append(row)
    cons = []
    # row inequality constraints
    for row in range(size):
        for i in range(size):
            for j in range(i + 1, size):
                con = Constraint("C(Q({0}, {1}),Q({0}, {2})".format(row + 1, i + 1, j + 1), [vars[row][i], vars[row][j]])
                sat_tuples = []
                greater_sign = False
                less_sign = False
                if i + 1 == j:
                    if futo_grid[row][i * 2 + 1] == ">":
                        greater_sign = True
                    elif futo_grid[row][i * 2 + 1] == "<":
                        less_sign = True
                for t in itertools.product(dom, dom):
                    if t[0] != t[1]:
                        if (not greater_sign or t[0] > t[1]) and (not less_sign or t[0] < t[1]):
                            sat_tuples.append(t)
                con.add_satisfying_tuples(sat_tuples)
                cons.append(con)
    # column inequality constraints
    for col in range(size):
        for i in range(size):
            for j in range(i + 1, size):
                con = Constraint("C(Q({1}, {0}),Q({1}, {2})".format(col + 1, i + 1, j + 1),
                                 [vars[i][col], vars[j][col]])
                sat_tuples = []
                for t in itertools.product(dom, dom):
                    if t[0] != t[1]:
                        sat_tuples.append(t)
                con.add_satisfying_tuples(sat_tuples)
                cons.append(con)


def futoshiki_csp_model_2(futo_grid):
    ##IMPLEMENT 
    pass
