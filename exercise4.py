import urllib2
import string
import sys
import argparse as ap
from collections import deque
from wordsegment import load, segment

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
print decrypted
print '---------------------'
load()
segment = segment(decrypted)
print " ".join(str(x) for x in segment)
