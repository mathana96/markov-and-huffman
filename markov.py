import numpy as np
import collections
from heapq import heappush, heappop, heapify
from collections import defaultdict


matrix = np.zeros((128, 128))
matrix_dict = {}
matrix_dict_num = {}

def entropy(data):
    cleanData=[x for x in data if x!=0]
    sumData=sum(cleanData)
    probs=np.array(cleanData)/sumData
    return(-sum(probs*np.log2(probs)))

def distribution(input):
    freq = collections.Counter(input)
    n = float(len(input))
    relfreq = dict((k, v/n) for k, v in freq.items())
    return relfreq

def buildMatrixDictChar(rvd):
    m = {}
    j = 0
    for key, value in rvd.iteritems():
        m[key] = j    
        j += 1
    return m

def buildMatrixDictNum(rvd):
    m = {}
    j = 0
    for key, value in rvd.iteritems():
        m[j] = key   
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

def normalise_matrix():
    for k in range(0, 127):
        row = matrix[k, :]
        summ = float(sum(row))
        for m in range(0, 127):
            if matrix[k, m] != 0:
                matrix[k, m] /= summ


def entropy_rate():
    sumo = 0.0;
    for k in range(0, len(matrix_dict_num)):
#         print(k)
        row = matrix[k, :]
        ent = entropy(row)
        row_char = matrix_dict_num[k]
        miu = rv[row_char]
        sumo += ent * miu
    return sumo
    
    
    
source = open("input.txt")
input = source.read()

print('Markov chain representation ...')

rv = distribution(input)

# print(rv)

matrix_dict = buildMatrixDictChar(rv)
matrix_dict_num = buildMatrixDictNum(rv)

# print(matrix_dict_num)
populateMatrix()
normalise_matrix()

rate = entropy_rate()
print('Entropy of Markov chain (in bits) = ', rate)