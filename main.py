# Author: Ted Nesham
# Date Created: 06/24/2020
# Class: CS_4732
# Professor: Mark Hauschild

import re
import string


def string_checker(str1, str2):

    regex = re.compile('[^a-zA-Z]')
    str1 = regex.sub('', str1).lower()
    # Removing all if any non-alphabetic characters and converting to lowercase

    str2 = regex.sub('', str2).lower()
    # doing the same to the key as the plaintext just for safety for inputs

    if len(str1) < len(str2):
        # no action taken if equal
        # if less than we nee to slice the keytext accordingly
        # action: slice key text to be length of plaintext.
        str2 = str2[0:(len(str1) - len(str2))]
        print("The new keytext is: " + str2)
        print("The key was larger than the plaintext. Taking appropriate action...")

    elif len(str1) > len(str2):
        # else if the plaintext is longer than the key we need to repeat the key
        # until the length of the key is greater than the plaintext then slice off
        # any remainder.
        print("the plaintext was longer than the key. Taking appropriate action...")

        while len(str1) >= len(str2):
            # loop until the plaintext is not longer than the keytext.
            str2 = str2 + str2

        str2 = str2[0:(len(str1) - len(str2))]
        print("The new keytext is: " + str2)
    else:
        print("keytext is: " + str2)

    return str1, str2


def encrypt(plaintext, keytext):

    plaintext, keytext = string_checker(plaintext, keytext)

    i = 0
    encrypted_text = ''
    # initializing the index and the encrypted text. Since Python strings are
    # immutable we need to build a new string rather than just replace the characters.

    while i < len(plaintext):

        plt_pos = string.ascii_lowercase.index(plaintext[i])
        key_pos = string.ascii_lowercase.index(keytext[i])
        # get both positions to add together to make the encrypted letter

        encrypted_letter = string.ascii_lowercase[(plt_pos + key_pos) % 26]
        # encrypted letter is the letter position in alphabet for the plt + position in the alphabet
        # of the keytext letter all mod 26 to ensure it will wrap back around.
        encrypted_text = encrypted_text + encrypted_letter
        # building the encrypted string.
        i = i + 1

    print("Your encrypted message is: " + encrypted_text)
    return encrypted_text


def decrypt(encrypted_text, keytext):

    encrypted_text, keytext = string_checker(encrypted_text, keytext)

    i = 0
    decrypted_text = ""
    # initializing the index and the encrypted text. Since Python strings are
    # immutable we need to build a new string rather than just replace the characters.

    while i < len(encrypted_text):

        enc_pos = string.ascii_lowercase.index(encrypted_text[i])
        key_pos = string.ascii_lowercase.index(keytext[i])
        # get both positions to add together to make the encrypted letter

        decrypted_letter = string.ascii_lowercase[(enc_pos - key_pos) % 26]
        # encrypted letter is the letter position in alphabet for the plt + position in the alphabet
        # of the keytext letter all mod 26 to ensure it will wrap back around.
        decrypted_text = decrypted_text + decrypted_letter
        # building the encrypted string.
        i = i + 1

    print("the decrypted text is: " + decrypted_text)


def task_one(plaintext, keytext):

    print("doing task one...\n")
    encrypted_string = encrypt(plaintext, keytext)

    print("\ndecrypting string... ")
    decrypt(encrypted_string, keytext)


user_input_str = raw_input("Please enter a string to encode: ")
user_input_key = raw_input("Please enter the key in which the string will be encoded with: ")
task_one(user_input_str, user_input_key)



