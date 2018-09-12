import urllib2
import string
import sys
import argparse as ap
from collections import deque
from wordsegment import load, segment
import math
import operator


def keyToIntShift(key):
    keyInt = []
    for i in key:
        keyInt.append(string.ascii_lowercase.index(i))
    return keyInt

def decrypt(text, key):
    index = 0
    keyInt = keyToIntShift(key)
    decryptedText = ''
    for c in text.replace("\n", ""):
        charToIndex = string.ascii_lowercase.index(c)
        decryptedText += string.ascii_lowercase[(charToIndex - keyInt[index]) % 26]
        index = (index + 1) % len(key)
            
    return decryptedText

def downloadFileFromICCE():
    username = 'Security'
    password = 'First!'
    url = 'https://www.icce.rug.nl/edu/infosec/intro/schneier.encrypted.txt'
    p = urllib2.HTTPPasswordMgrWithDefaultRealm()
    p.add_password(None, url, username, password)

    handler = urllib2.HTTPBasicAuthHandler(p)
    opener = urllib2.build_opener(handler)
    urllib2.install_opener(opener)
    return urllib2.urlopen(url).read()


# Outputs an freqency table depending on the keyLength
def getFrequencyTable(text, keylength):
    i = 0
    frequencyTable = initFrequencyTable(keylength)
    for c in text.replace("\n", ""):
        frequencyTable[i][c] += 1
        i += 1
        i %= keylength

    return frequencyTable

def initFrequencyTable(keylength):
    freqTable = {}
    for i in range (0, keylength):
        freqTable[i] = {}

        for c in string.ascii_lowercase:
            freqTable[i][c] = 0

    return freqTable

def sqr(x):
    return x * x

def getStandardDeviation(sumOfSquared, sum):
    return math.sqrt(sumOfSquared / 26 - sqr(sum / 26))

file = downloadFileFromICCE()

# std devs:
largestStdDev = 0
bestKeylength = 0
for i in range(5, 16):
    standardDevSum = 0
    frequencyTable = getFrequencyTable(file, i)
    #print frequencyTable
    for letterIndex in frequencyTable:
        sumOfSquared = 0
        sum = 0
        for frequency in frequencyTable[letterIndex].values():
            sumOfSquared += frequency * frequency
            sum += frequency          

        standardDevSum += getStandardDeviation(sumOfSquared, sum)

    if standardDevSum > largestStdDev:
        largestStdDev = standardDevSum
        bestKeylength = i
    print 'sum of \t' + str(i) + ' std. devs: ' + str(standardDevSum) + ','

print 'So that makes a keylength of ' + str(bestKeylength) + ' the most plausible'
frequencyTable = getFrequencyTable(file, 9)

key = ''
alts = {}
for i in range(0, 10):
    alts[i] = {}
    for j in range(0, 4):
        alts[i][j] = ''

for letterIndex in frequencyTable:
    mostFreqChar = sorted(frequencyTable[letterIndex].items(), key=operator.itemgetter(1), reverse=True)
    for i in range(0, 4):
        print string.ascii_lowercase.index(mostFreqChar[i][0])
        index = string.ascii_lowercase.index(mostFreqChar[i][0])
        indexOfE = string.ascii_lowercase.index('e')
        shifting = index - indexOfE
        # To get the key:
        alts[letterIndex][i] += string.ascii_lowercase[shifting]

    #print mostFreqChar + ' is the most frequent char at pos ' + str(letterIndex) + ', (shifting = ' + str(shifting) + ') ==> keychar = \t' + string.ascii_lowercase[shifting]

print 'Found the key! It must be "' + str(key) + '". Now decrypting the text:'

for letterIndex in range(0, 9):
    print '----------'
    for alternative in range(0, 3):
        print alts[letterIndex][alternative]

# decrypted = decrypt(file, key)
# print decrypted
# print '---------------------'
# load()
# segment = segment(decrypted)
# print " ".join(str(x) for x in segment)
