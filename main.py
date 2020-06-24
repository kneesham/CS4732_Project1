# Author: Ted Nesham
# Date Created: 06/24/2020
# Class: CS_4732
# Professor: Mark Hauschild

import re


def task_one(plaintext, keytext):

    print("doing task one...")

    regex = re.compile('[^a-zA-Z]')
    plaintext = regex.sub('', plaintext).lower()
    # Removing all if any non-alphabetic characters and converting to lowercase

    keytext = regex.sub('', keytext).lower()
    # doing the same to the key as the plaintext just for safety for inputs

    if len(plaintext) < len(keytext):
        # no action taken if equal
        # if less than we nee to slice the keytext accordingly
        # action: slice key text to be length of plaintext.
        keytext = keytext[0:(len(keytext) - len(plaintext) + 1)]
        print(keytext)
        print("The key was larger than the plaintext")
    else:
        # else if the plaintext is longer than the key we need to repeat the key
        # until the length of the key is greater than the plaintext then slice off
        # any remainder.
        print("the plaintext was longer than the key.")

        while len(plaintext) > len(keytext):
            # loop until the plaintext is not longer than the keytext.
            keytext = keytext + keytext

        keytext = keytext[0:(len(plaintext) - len(keytext))]
        # slice off the any extra letters off the keytext.

        print("new key text: " + keytext)
        print("the plaintext is: " + plaintext)

    i = 0
    encrypted_text = ""
    # initializing the index and the encrypted text. Since Python strings are
    # immutable we need to build a new string rather than just replace the characters.

    while i < len(plaintext):
        encrypted_letter = chr(ord(plaintext[i]) + (ord(keytext[i]) - 97))
        # subtract 97 since the ascii value of 'a' is 97.
        encrypted_text = encrypted_text + encrypted_letter
        # building the encrypted string.
        i = i + 1

    print("Your encrypted message is: " + encrypted_text)


task_one('DOGSAREGOOD', 'abc')