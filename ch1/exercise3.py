import string
from collections import deque
from wordsegment import load, segment

mapping = ''

###
# Method that returns a mapping from an int
# input 1 gives bcdefghijklmnopqrstuvwxyza
###
def shiftToMapping(arg):
    shift = 0
    shift = int(arg)
    if shift >= 1 and shift < 26:
        mapping = deque(list(string.ascii_lowercase))
        mapping.rotate(shift)
        return ''.join(mapping)

# Method that creates an dict from mapping, mapping the alphabet to the mapping.
def createLetters(mappingArg):
    letters = {}    

    for i in range(len(mappingArg)):
        letters[list(string.ascii_lowercase)[i]] = mapping[i]

    return letters

def decrypt(text, shift):
    global mapping
    mapping = shiftToMapping(shift)
    global letters
    letters = createLetters(mapping)
    decryptedText = ''
    for c in text:
        if c.lower() in letters:
            decryptedText += letters[c.lower()].lower()
        else:
            decryptedText += c
    return decryptedText

file = "govmywodydromyebcoklyedsxpybwkdsyxcomebsdidrscmyebcoscklyedcomebsxqsxpybwkdsyxsxdrscmyxdohdgodrsxupybohkwzvoklyedrygdyzbofoxddroexkedrybsjonboknsxqypsxpybwkdsyxybklyedrygdyzbofoxddroexkedrybsjonwynspsmkdsyxypsxpybwkdsyxwkxioxmbizdsyxwodryncohscdcywokvboknidryeckxnciokbcyvnsxsdskvvigovvpymecyxcswzvowodryncdyoxmbizdsxpybwkdsyxpyvvygsxqdrscgovvecomrkbkmdobscdsmfkveocsnoxdspisxqsxpybwkdsyxwkusxqsdnsppsmevddywynspisxpybwkdsyxexxydspsonvkdobsxdrscmyebcogovvsxdbynemozobcyxkvoxmbizdsyxkxngovvcdenidyzsmcvsuoleppobyfobpvygohzvysdckxncmbycccsdocmbszdsxqsryzoiyevvoxtyidrscmyebcoklyedsxpybwkdsyxcomebsdi"

load()

for x in range(1, 26):
    print decrypt(file, x)

# 10 is the right mapping: qrstuvwxyzabcdefghijklmnop
# Now we will use segmentation to get the correct output with spaces.
mapping = shiftToMapping(10)
print '---------------'
print 'Using mapping:'
print mapping
decrypted = decrypt(file, 10)
print decrypted
print '---------------'
segment = segment(decrypted)
print " ".join(str(x) for x in segment)
