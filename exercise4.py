import urllib2
import string
import sys
import argparse as ap
from collections import deque
from wordsegment import load, segment
import math

key = 'integrity'

keyInt = []
for i in key:
    keyInt.append(string.ascii_lowercase.index(i))

print keyInt

def decrypt(text, key):
    index = 0
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

file = downloadFileFromICCE()

decrypted = decrypt(file, key)
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

def getStandardDeviation(sumOfSquared, sum):
    tst = (sum / 26) * (sum / 26)
    print tst
    return math.sqrt(sumOfSquared / 26 - tst)

for i in range(5, 16):
    sumOfSquared = 0
    sum = 0
    standardDevSum = 0
    frequencyTable = getFrequencyTable(file, i)
    #print frequencyTable
    for letterIndex in frequencyTable:
        for frequency in frequencyTable[letterIndex].values():
            sumOfSquared += frequency * frequency
            sum += frequency

        standardDevSum += getStandardDeviation(sumOfSquared, sum)

    print 'sum of \t' + str(i) + ' std. devs: ' + str(standardDevSum) + ','

#decrypted = decrypt(file, key)
#print decrypted
#print '---------------------'
#load()
#segment = segment(decrypted)
# print " ".join(str(x) for x in segment)
