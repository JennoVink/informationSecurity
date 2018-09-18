# 1 3 6 13 27 52 109 213 - 425 850 1701 3444 6900 13801 27555 55155
#
# -= First = -
# bin:            00000100
# 10010010
# reverse(bin):    01001001
# 00100000 = 'I '
#
# 31476 - 27555 = 3921
# 3921 - 3444 = 477
# 477 - 425 = 52
# 52 - 52 = 0

indexes = []

shouldStop = False
def getIndexesOfGreatestSubtraction(sequence, n):
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
    #             save index
                    print n
                    indexes.append(i)
                    getIndexesOfGreatestSubtraction(sequence, n - val)


seq = [1, 3,6,13, 27, 52, 109, 213, 425, 850, 1701, 3444, 6900, 13801, 27555, 55155]
getIndexesOfGreatestSubtraction(seq, 31476)
print indexes
for index in indexes:
    print seq[index]