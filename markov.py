import numpy as np
import collections
from heapq import heappush, heappop, heapify
from collections import defaultdict


matrix = np.zeros((128, 128))
matrix_dict = {}
matrix_dict_num = {}

def encode(symb2freq):
    heap = [[wt, [sym, ""]] for sym, wt in symb2freq.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

def encode_decode(dictionary, text):
    res = ""
    while text:
        for k in dictionary:
            if text.startswith(k):
                res += dictionary[k]
                text = text[len(k):]
    return(res)

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
        row = matrix[k, :]
        ent = entropy(row)
        row_char = matrix_dict_num[k]
        miu = rv[row_char]
        sumo += ent * miu
    return sumo
 
def huffman_markov():
    sumo = 0.0;
    helper = {}
#     for k in range(0, len(matrix_dict_num)):
    row = matrix[0, :]
    k = 0
    for m in range(k, len(matrix_dict_num)):
        if matrix[k, m] != 0.0:
            c = matrix_dict_num[m]
            helper[c] = matrix[k, m]
    code = encode(helper)
    return code
    
def codewordlength(rv, huffman):
    cwlList =[]
    for k, v in rv.items():
        for code in huffman:
            if code[1]:
                bits = code[1]
                bitlength = len(bits)
                if (code[0] == k):
                    cwlList.append(v*bitlength)
    return sum(cwlList)

def huffman_code_first_dict(huffman):
    data = []
    code = []
    for item in huffman:
        data.append(item[0])
        code.append(item[1])

    return dict(zip(code,data))

def huffman_data_first_dict(huffman):
    data = []
    code = []
    for item in huffman:
        data.append(item[0])
        code.append(item[1])

    return dict(zip(data,code))
def encode_decode(dictionary, text):
    res = ""
    while text:
        for k in dictionary:
            if text.startswith(k):
                res += dictionary[k]
                text = text[len(k):]
    return(res)
   
source = open("input.txt")
input = source.read()

print('Markov chain representation ...')

rv = distribution(input)


matrix_dict = buildMatrixDictChar(rv)
matrix_dict_num = buildMatrixDictNum(rv)

populateMatrix()
normalise_matrix()

rate = entropy_rate()
print('Entropy of Markov chain (in bits) = ', rate)


huffman = encode(rv)

huff_kov = huffman_markov()


print('Huffman L(C) for Markov chain (in bits) = ', codewordlength(rv,huff_kov))

print('Test 1 - Small sample (with no unique sequence pair,  eg 'u' is only char following 'q') ...')

sample = input[0:30]
print('Length of source message (in bits) = ', len(sample) * 7)

# encoded_markov

print('Length of encoded message (in bits) = ', len(encoded_markov))

# decoded_markov


# huffman_encoded = encode_decode(data_first_dict, short_text)
# huffman_decoded = encode_decode(code_first_dict, huffman_encoded) 


# if (len(sample) < 50):
#   print(sample)
#   print(huffman_encoded)
#   print(huffman_decoded)


# if (sample == decoded_markov):
#   print('YES !! decoded(endoded(message)) == message')
# else:
#   print('ERROR !! decoded(endoded(message)) != message')
#   length = len(decoded_markov)
#   for i in range(0, length):
#       print(sample[k], decoded_markov[k])


# sample = input



# if (sample == decoded_markov):
#   print('YES !! decoded(endoded(message)) == message')
# else:
#   print('ERROR !! decoded(endoded(message)) != message')
#   length = len(decoded_markov)
#   for i in range(0, length):
#       print(sample[k], decoded_markov[k])
