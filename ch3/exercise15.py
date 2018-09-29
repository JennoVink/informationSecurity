def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def generate_keypair(p=31, q=41):
    # Public encryption key (N, e)
    N = p * q
    e = 7

    # Phi is the totient of N
    phi = (p - 1) * (q - 1)

    # Private decryption key (d)
    d = modinv(e, phi)

    return (N, e), (N, d)


(N, e), (N, d) = generate_keypair()
print("Public key is:\t\t" + str(N) + " " + str(e))
print("Private key is:\t\t" + str(d))


def encrypt(public_key, k):
    N, e = public_key
    cipher = (k ** e) % N
    return cipher


encrypted = encrypt((N, e), 42)
print("Encrypted is:\t\t" + str(encrypted))


def decrypt(private_key, c):
    N, d = private_key
    plain = (c ** d) % N
    return plain


decrypted = decrypt((N, d), encrypted)
print("Decrypted is:\t\t" + str(decrypted))
