import numpy as np
import collections
from heapq import heappush, heappop, heapify
from collections import defaultdict


matrix = np.zeros((128, 128))
matrix_dict = {}

def distribution(input):
    freq = collections.Counter(input)
    n = float(len(input))
    relfreq = dict((k, v/n) for k, v in freq.items())
    return relfreq

def buildMatrixDict(rvd):
    m = {}
    j = 0
    for key, value in rvd.iteritems():
        m[key] = j    
        j += 1
    return m
        
def populateMatrix():
    length = len(input)
    for i in range(0, length):
        current_char = input[i]
        if i != (length-1):
            next_char = input[i + 1]
            current_no = matrix_dict[current_char]
            next_no = matrix_dict[next_char]
            matrix[current_no, next_no] += 1
            

            
source = open("input.txt")
input = source.read()
rv = distribution(input)

matrix_dict = buildMatrixDict(rv)

print(matrix_dict)
populateMatrix()

# print(matrix[47, :])
# print(matrix)
