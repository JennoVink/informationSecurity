######
# Encrypt een zelfverzonnen file met het volgende ww: Feistel
# Vervolgens daar de sha256 voor pakken:
# 184b4d16bbe3200c5a5f500cc09efa68cddd42cbda27c1e49fa7a0f2e2735007
# Daarna daar weer de sha256 van pakken:
# bd11fd28eabd0b87f2ff4595a50041bfb882bbf8ae058ea5d677c7da07d43786
# dit zorgt voor een key. Klein dingetje:
# de key wordt: 0x18 (1e byte van de key), 0x4b etc. Totaal 64 bytes omdat de 'characters of the sha256sum must be interpreted as hexadecimal values'
# Een block bestaat uit 8 bytes. Er zijn keys van 4 bytes nodig voor elke ronde.
# De twee sha's regelen dit: 16 keys (1 per ronde) van 4 bytes each, in total 64 bytes.
#
# Dus een ronde nestaat hieruit:
# 1. plaintextBlock opdelen
# 2. over de rechterkant een F(R, K) doen.
# 3. Resultaat daarvan XOR ^ met de linkerkant
# 4. daarna links en rechts omdraaien
#
import hashlib
import os


script_dir = os.path.dirname(__file__)
rel_path = "fileToEncrypt.txt"
abs_file_path = os.path.join(script_dir, rel_path)
file = open(abs_file_path, 'r')

feistelHash = hashlib.sha256(b'Feistel')
KEY = feistelHash.hexdigest() + hashlib.sha256(feistelHash.hexdigest()).hexdigest()
print KEY

ROUNDS = 16
BLOCK_SIZE = 8

##
# Receive the next two blocks from the file to encrypt.
# The function read(size) reads the next blocks
def getBlockparts():
    text = file.read()
    print 'input: ', text
    return [text[i:i + BLOCK_SIZE] for i in range(0, len(text), BLOCK_SIZE)]

##
# Method that extracts the roundkey from a global key variable, depending on the roundNumber.
def getRoundKey(roundNumer):
    return '0x' + [KEY[i:i + 2] for i in range(0, len(KEY), 2)][roundNumer]

##
# As a convention, the roundfunction with two params are implemented so it can be changed later.
def roundFunction(right, roundKey):
    return roundKey


def xor(a, b):
    print a, b
    return ''.join(chr(ord(aa) ^ ord(bb)) for aa, bb in zip(a, b))


##
# encrypt one block with ROUNDS rounds, the left part, right part and the roundKey.
def encryptBlock(l, r):
    for i in range(0, ROUNDS):
        print 'L: ' + str(l)
        print 'R: ' + str(r)
        roundKey = getRoundKey(i)
        print 'the roundkey is: ' + roundKey

        if len(l) == 0 or len(r) == 0:
            print "Can't en/decrypt anymore, L or R is empty"
        else:
            tempR = r
            r = xor(l, roundFunction(r, roundKey))
            l = tempR

    print 'result: ' + l + '' + r
    return l + '' + r


encrypted = ''
for block in getBlockparts():
    l, r = block[:BLOCK_SIZE/2], block[BLOCK_SIZE/2:]
    encrypted += encryptBlock(l, r)

print 'encrypted text: ', encrypted