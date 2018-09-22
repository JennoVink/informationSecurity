# This solution involves modular exponentiation with recursive function.
# It solves C^d % n where C, d and n could be large values.
import math
import time

c = 43210
d = 23456
n = 99987

# Array with the answers of the exponentiation mod n.
# All the indexes can be seen as powers of 2: so 0: 1, 1: 2, 2: 4, 3: 8, 4: 16 etc.
exponentiation = []
exponentiation.append(c)

def calcTotalFromExponentiationTable(sequence, n):
    total = 1
    for index, bit in enumerate("{0:b}".format(d)):
        if bit == '1':
            # Reverse the sequence of exponents
            total = total * sequence[::-1][index]

    return total % n


def calcLargePowerModulo(d, n, x):
    if x * 2 > d:
        return calcTotalFromExponentiationTable(exponentiation, n)
    x = x * 2

    # Most important part: get the previous answer, raise to the power of 2. Modulo n that answer.
    # The previous answer is get via math.log(x, 2), so that another loop value wasn't necessary.
    result = (exponentiation[int(math.log(x, 2) - 1)] * exponentiation[int(math.log(x, 2) - 1)]) % n
    print x, result
    exponentiation.append(result)
    return calcLargePowerModulo(d, n, x)

start_time = time.time()
print "The answer is: " + str(calcLargePowerModulo(d, n, 1))
print("--- %s seconds ----" % (time.time() - start_time))
print exponentiation