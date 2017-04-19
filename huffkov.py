import collections
# mydict = dict((k, v if v else '') for k, v in mydict.items())

def distribution(input):
    freq = collections.Counter(input)
    n = float(len(input))
    relfreq = dict((k, v/n) for k, v in freq.items())
    print (freq)
    return relfreq



source = open("input.txt")
input = source.read()

print('Length of text message (in 7-bit char): ', len(input))
print('Length of text message (in bits): ', 7*len(input))


# Construct probabilities using observed frequencies in given string of text
rv = distribution(input)
print(rv)