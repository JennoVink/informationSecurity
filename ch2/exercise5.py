import hashlib
import os

# Open file to encrypt.
script_dir = os.path.dirname(__file__)
rel_path = "fileToEncrypt.txt"
abs_file_path = os.path.join(script_dir, rel_path)
file = open(abs_file_path, 'r')

feistelHash = hashlib.sha256(b'Feistel').hexdigest()
KEY = feistelHash + hashlib.sha256(feistelHash).hexdigest()
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
    return [KEY[i:i + BLOCK_SIZE].decode('HEX') for i in range(0, len(KEY), BLOCK_SIZE)][roundNumer]

##
# As a convention, the roundfunction with two params are implemented so it can be changed later on.
def roundFunction(right, roundKey):
    return roundKey


def xor(a, b):
    return ''.join(chr(ord(aa) ^ ord(bb)) for aa, bb in zip(a, b))

##
# Encrypt one block with ROUNDS rounds, the left part, right part and the roundKey.
def encryptBlock(l, r):
    for i in range(0, ROUNDS):
        roundKey = getRoundKey(i)

        if len(l) == 0 or len(r) == 0:
            raise Exception("Can't en/decrypt anymore, L or R is empty!")
        else:
            tempR = r
            r = xor(l, roundFunction(r, roundKey))
            l = tempR

    return l + '' + r


# Encrypt each block:
encrypted = ''
for block in getBlockparts():
    l, r = block[:BLOCK_SIZE/2], block[BLOCK_SIZE/2:]
    encrypted += encryptBlock(l, r)

# Save the file for decryption.
rel_path = "encryptedText.txt"
abs_file_path = os.path.join(script_dir, rel_path)
f = open(abs_file_path, "w+")
f.write(encrypted)
f.close()

print 'encrypted text: ', encrypted