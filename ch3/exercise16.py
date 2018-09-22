# Note, please install sympy: pip install sympy
import os
import time

from sympy.ntheory import factorint

script_dir = os.path.dirname(__file__)
rel_path = "first1000primes.txt"
abs_file_path = os.path.join(script_dir, rel_path)
f = open(abs_file_path, "r")

primes = []
for line in f.readlines():
    [primes.append(x.strip()) for x in line.split(' ')]
    primes = filter(len, primes)


def calcGenerators(p, prevGeneratorList):
    primeFactors = factorint(p - 1)
    generators = prevGeneratorList

    # The + 2 behind len(x) is because g ranges from 2 to p - 1
    for g in range(len(prevGeneratorList) + 2, p-1):
        results = []
        for x in primeFactors:
            result = g ** ((p-1) / x) % p
            # print result
            if result == 1:
                break
            results.append(result)
        # print g, results
        generators.append(g)

    return generators

def calcGeneratorInefficient(p):
    primeFactors = factorint(p - 1)
    generators = []

    for g in range (2, p-1):
        results = []
        for x in primeFactors:
            result = g ** ((p-1) / x) % p
            if result == 1:
                break
            results.append(result)
        # print g, results
        generators.append(g)

    return generators


AMOUNT_TO_TEST = 1000
start = time.time()
prevGeneratorList = []
index = 990
for prime in primes[989:AMOUNT_TO_TEST]:
    listOfGenerators = calcGenerators(int(prime), prevGeneratorList)
    print str(index) + ' & ' + str(prime) + ' & ' + str(listOfGenerators[-10:]) + ' & ' + ' \\\\ '
    prevGeneratorList = listOfGenerators
    index = index + 1
end = time.time()
print 'Time needed', (end - start)

# start = time.time()
# for prime in primes[:AMOUNT_TO_TEST]:
#     listOfGenerators = calcGeneratorInefficient(int(prime))
#     # print listOfGenerators
#     prevGeneratorList = listOfGenerators
# end = time.time()
# print 'Time needed', (end - start)