def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi / e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi


def generate_keypair(p=31, q=41):
    # Public encryption key (N, e)
    N = p * q
    e = 7

    # Phi is the totient of N
    phi = (p - 1) * (q - 1)

    # Private decryption key (d)
    d = multiplicative_inverse(e, phi)

    return (N, e), (N, d)


(N, e), (N, d) = generate_keypair()
print "Public key is:  " + str(N) + " " + str(e)
print "Private key is: " + str(d)


def encrypt(public_key, k):
    N, e = public_key
    cipher = (k ** e) % N
    return cipher


encrypted = encrypt((N, e), 42)
print encrypted


def decrypt(private_key, c):
    N, d = private_key
    plain = (c ** d) % N
    return plain


decrypted = decrypt((N, d), encrypted)
print decrypted
