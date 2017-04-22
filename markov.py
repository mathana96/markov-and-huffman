import numpy as np
import collections
from heapq import heappush, heappop, heapify
from collections import defaultdict

# def markov():
    
# def huffman_markov:


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

def entropy(data):
    cleanData=[x for x in data if x!=0]
    sumData=sum(cleanData)
    probs=np.array(cleanData)/sumData
    return(-sum(probs*np.log2(probs)))

def codewordlength(rv, huffman):
	cwlList =[]
	for k, v in rv.items():
		for code in huffman:
			bits = code[1]
			bitlength = len(bits)
			if (code[0] == k):
				cwlList.append(v*bitlength)
	return sum(cwlList)


source = open("input.txt")
input = source.read()

print('Markov chain representation ...')

# markov()

print('Entropy of Markov chain (in bits) = ', entropy())

# huffman_markov()

# print('Huffman L(C) for Markov chain (in bits) = ', codewordlength(?,?))

print('Test 1 - Small sample (with no unique sequence pair,  eg 'u' is only char following 'q') ...')
sample = input[0:30]

print('Length of source message (in bits) = ', len(sample) * 7)

# encoded_markov

print('Length of encoded message (in bits) = ', len(encoded_markov))

# decoded_markov

if (len(sample) < 50):
	print(sample)
	print(encoded_markov)
	print(decoded_markov)


if (sample == decoded_markov):
	print('YES !! decoded(endoded(message)) == message')
else:
	print('ERROR !! decoded(endoded(message)) != message')
	length = len(decoded_markov)
	for i in range(0, length):
		print(sample[k], decoded_markov[k])

print('Test 1 - Small sample (with no unique sequence pair,  eg 'u' is only char following 'q') ...')
sample = input

print('Length of source message (in bits) = ', len(sample) * 7)

# encoded_markov

print('Length of encoded message (in bits) = ', len(encoded_markov))

# decoded_markov

if (sample == decoded_markov):
	print('YES !! decoded(endoded(message)) == message')
else:
	print('ERROR !! decoded(endoded(message)) != message')
	length = len(decoded_markov)
	for i in range(0, length):
		print(sample[k], decoded_markov[k])
