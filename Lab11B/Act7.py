# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: ABDULLAH AHMAD
# Section: 518
# Assignment: LAB11B-Act7
# Date: 8 11 2018
import numpy as np

def solution_vector(coeff_mat,sol_vec):
    inverse = np.linalg.inv(coeff_mat)
    solution = inverse @ sol_vec
    print(solution)
    return
