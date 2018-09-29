# Exercise 17.
# Basic exercise
# Purpose: use ECC with DH key exchange: part I: ECC final point computation
#
# This exercise requires an e-mail exchange with a teaching assistant.
# Your e-mail to a teaching assistant must have been sent no later than one full day before this exercise's deadline
# (or earlier if you want to be able to send in a second attempt).
# Also, be sure to react in time to a reply from the teaching assistant
# so that the exercise is completed before its deadline.
#
# Send a teaching assistant the a, b, N, initial point's X and Y coordinates, and the final point you obtained
# after computing m * (x, y) for the provided elliptic curve,
# where m is the multiplier of your choice (so you don't send m to a teaching assistant).
# Each value must be submitted on a separate line, so you send 7 values to the assistant:
#
#     a
#     b
#     N
#     X1
#     Y1
#     Xm
#     Ym
#
# You then receive from the teaching assistant the Xn and Yn coordinate of his point
# on the elliptic curve (two values) and an encrypted text.
# The assistant's Xn and Yn coordinates are mentioned in the e-mail text,
# the encrypted message is stored in a zip, containing message.enc which is a binary file.
#
# The encrypted text is not used in this exercise,
# but is used in the next (optional) exercise: you can ignore it if you're not completing that exercise.
#
# For this exercise, compute the final (shared) point on the elliptic curve (i.e., m * (Xn, Yn))
# write it like this: '(X,Y)' (no blanks, the quotes are not part of the representation, no leading zeros).
#
# Submit the final shared point as answer to this exercise.

# Example values from slides
# a         11
# b         19
# N         167
# xy        (2, 7)
# m         15
# xy_m      (102, 88)

# Values for exercise
# a         -3
# b         7
# N         233
# xy        (2, 3)
# m         18
