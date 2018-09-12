import urllib2
import string
import sys
from collections import deque

mapping = ''

nonLettersAsIs = False
decryptArg = -1
manualInput = False

# -o option
if '-o' in str(sys.argv):
    nonLettersAsIs = True

# -d option
if '-d' in str(sys.argv):
    decryptArg = 1

# -i option is extra, for manual custom input.
if '-i' in str(sys.argv):
    manualInput = True

###
# Method that returns a mapping from an int or string.
# e.g. input 1 gives bcdefghijklmnopqrstuvwxyza
###
def shiftToMapping(arg):
    try:
        shift = int(arg)
        if shift >= 1 and shift < 26:
            mapping = deque(list(string.ascii_lowercase))
            mapping.rotate(shift * decryptArg)
            return ''.join(mapping)
        else:
            print "The shift has to be >= 1 or < 26."
            return shiftToMapping(raw_input("Enter new shift value or mapping (26 chars): "))
    except ValueError:
        if len(arg) == 26:
            return arg
        else:
            print 'The mapping does not contain 26 characters.'
            return shiftToMapping(raw_input("Enter new shift value or mapping (26 chars): "))


mapping = shiftToMapping(sys.argv[-1])

print 'mapping: '
print mapping

letters = {}
for i in range(len(mapping)):
    if decryptArg == 1:
        letters[mapping[i]] = list(string.ascii_lowercase)[i]
    else:
        letters[list(string.ascii_lowercase)[i]] = mapping[i]


def decrypt(text, letters):
    global nonLetterAsIs
    decryptedText = ''
    for c in text:
        if c.lower() in letters:
            decryptedText += letters[c.lower()].upper() if c.isupper() and nonLettersAsIs else letters[c.lower()].lower()
        else:
            decryptedText += c
    return decryptedText


def getEncryptedText():
    with open('2018.enc.txt', 'r') as content_file:
        content = content_file.read()
    return content


file = getEncryptedText()
if manualInput:
    file = sys.argv[-2]
print '---------- Original Input: ----------'
print file

if decryptArg == 1:
    print '---------- Decrypted: ----------'
else:
    print '---------- Ecrypted: ----------'    

print decrypt(file, letters)