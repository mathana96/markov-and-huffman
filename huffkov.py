# https://rosettacode.org/wiki/Huffman_coding#Python
import numpy as np
import collections
from heapq import heappush, heappop, heapify
from collections import defaultdict
 
def encode(symb2freq):
    """Huffman encode the given dict mapping symbols to weights"""
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
 


def distribution(input):
    freq = collections.Counter(input)
    n = float(len(input))
    relfreq = dict((k, v/n) for k, v in freq.items())
    print (freq)
    return relfreq

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


	# cwl = np.multiply(rv,len(huffman))
	# print(cwl)





source = open("input.txt")
input = source.read()

print('Length of text message (in 7-bit char): ', len(input))
print('Length of text message (in bits): ', 7*len(input))


# Construct probabilities using observed frequencies in given string of text
rv = distribution(input)
print(rv)

huffman = encode(rv)
print(huffman)

print('Entropy of RV (in bits) = ', entropy(rv.values()))
print('Huffman L(C) (in bits) = ', codewordlength(rv, huffman))


