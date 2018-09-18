# 1 3 6 13 27 52 109 213 - 425 850 1701 3444 6900 13801 27555 55155
#
# -= First = -
# bin:            00000100 10010010
#                 00000100 10010010
# reverse(bin):   01001001 00100000 = 'I '
#                 01001001 00100000
# 31476 - 27555 = 3921
# 3921 - 3444 = 477
# 477 - 425 = 52
# 52 - 52 = 0
import binascii
import os

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def text_from_bits(bits, encoding='utf-8', errors='ignore'):
    n = int(bits, 2)
    return int2bytes(n).decode(encoding, errors)

def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))

shouldStop = False
def getIndexesOfGreatestSubtraction(sequence, n, indexes=[]):
    global shouldStop
    # get biggest subtraction, see example
    for i, val in reversed(list(enumerate(sequence))):
        if val <= n:
            # print indexes
            if not shouldStop:
                if n - val == 0:
                    indexes.append(i)
                    shouldStop = True
                    return indexes
                else:
                    #print n
                    indexes.append(i)
                    getIndexesOfGreatestSubtraction(sequence, n - val, indexes)

    return indexes


def indexesToChar(indexes):
    bits = ''
    for i in range(0, len(seq)):
        # print i
        if i in indexes:
            bits += '1'
        else:
            bits += '0'
    return text_from_bits(bits[::-1])


seq = [1, 3,6,13, 27, 52, 109, 213, 425, 850, 1701, 3444, 6900, 13801, 27555, 55155]

script_dir = os.path.dirname(__file__)
rel_path = "boersma_ex6_ciphertext.txt"
abs_file_path = os.path.join(script_dir, rel_path)
f = open(abs_file_path, "r")

decrypted = ''
q = 133332
r = 5

supposedLength = 0
for line in f.readlines():
    global shouldStop
    if line is not '':
        input = int(line)
        mod_inv = (input * (modinv(r, q)))
        decryptedNumber = (mod_inv % q)
        shouldStop = False
        test = getIndexesOfGreatestSubtraction(seq, decryptedNumber, [])
        decrypted += indexesToChar(test)
        supposedLength += 1

print decrypted


