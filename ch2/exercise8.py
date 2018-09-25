# Exercise 8
# Basic exercise
# Purpose of this exercise: learn to work with a one-time pad
# When using a Vernam cipher, the plain text informationsecurity may be encrypted using the key vlaksjdhfgqodzmxncb.

# Note: use the xor-operator to en/decrypt;
# use the ASCII-character set, so don't design your own character set as Mark Stamp does in his book.

# Xoring characters may easily result in non-displayable characters.
# If the encrypted message or key contains at least one non-displayable character,
# display the result as a series of ASCII character numbers.

# If a key or encrypted message merely contains displayable characters then submit them as text-strings.

# Assume we're using an alternative key resulting in the same encrypted text. The alternative key is:
# tlftrffwmixor|{xbch

# Q:    What is the resulting alternative original text?
# A:    The resulting alternative plain text is `knapsackbagssecrets'

# -------------------------------------------------------------------------------------------


exercise_text = "informationsecurity"
exercise_key = "vlaksjdhfgqodzmxncb"

alternative_key = "tlftrffwmixor|{xbch"


def encrypt(plain_text, key):
    plain_text = list(plain_text)
    key = list(key)

    cipher_text = []

    for i in range(0, len(plain_text)):
        ascii_code = ord(plain_text[i]) ^ ord(key[i])
        cipher_text.append(ascii_code)

    return cipher_text


def decrypt(cipher_text, key):
    cipher_text = list(cipher_text)
    key = list(key)

    plain_text = []

    for i in range(0, len(cipher_text)):
        ascii_code = cipher_text[i] ^ ord(key[i])
        character = chr(ascii_code)
        plain_text.append(character)

    return ''.join(plain_text)


exercise_cipher = encrypt(exercise_text, exercise_key)
alternative_text = decrypt(exercise_cipher, alternative_key)

# print(exercise_cipher)
print(alternative_text)
