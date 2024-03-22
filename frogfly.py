import matplotlib.pyplot as plt
import numpy as np
"""
Given that a frog is located at a coordinate Xi, and a fly is located on the farthest coordinate Yi. The frog has a tongue of length Si. 
The frog can only eat the fly if the fly is within the range of the frog's tongue.
Write a function that returns the number of flies the frog can eat.
The function signature is:
def frog_eat_flies(X, Y, S)
Where:
X is an array of integers representing the coordinates of the frog.
Y is an array of integers representing the coordinates of the flies.
S is an array of integers representing the length of the frog's tongue.
The function should return an array of integers representing the number of flies the frog can eat.
For example:
X = [15, 10, 12, 18, 19]
Y = [20, 15, 10, 17, 13]
S = [5, 10, 7, 3, 10]
The frog can eat 2 flies. The first fly is within the range of the frog's tongue, and the second fly is within the range of the frog's tongue.

The function should return [1, 2, 2, 0, 2]
"""
def frog_eat_flies(X, Y, S):
    result = []
    for i in range(len(X)):
        count = 0
        for j in range(len(Y)):
            if Y[j] <= X[i] + S[i] and Y[j] >= X[i] - S[i]:
                count += 1
        result.append(count)
    return result

X = [15, 10, 12, 18, 19]
Y = [20, 15, 10, 17, 13]
S = [5, 10, 7, 3, 10]
print(frog_eat_flies(X, Y, S)) # [1, 2, 2, 0, 2]
