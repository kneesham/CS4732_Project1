
import string
import re
from itertools import product


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
        # print("The key was larger than the plaintext. Taking appropriate action...")
        # print("The new keytext is: " + str2)

    elif len(str1) > len(str2):
        # else if the plaintext is longer than the key we need to repeat the key
        # until the length of the key is greater than the plaintext then slice off
        # any remainder.
        # print("the plaintext was longer than the key. Taking appropriate action...")

        while len(str1) >= len(str2):
            # loop until the plaintext is not longer than the keytext.
            str2 = str2 + str2

        str2 = str2[0:(len(str1) - len(str2))]
        # print("The new keytext is: " + str2)
        # un-comment to see what key is being used.
    else:
        return str1, str2

    return str1, str2


def decrypt(encrypted_text, keytext, known_part):

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

    if known_part in decrypted_text:
        print("the decrypted text is: " + decrypted_text)
        print("the key tried was: " + keytext)
        return True


def brute_force(known_plt, max_keysize, ecrypted_text):
    print("\nbrute forcing...")

    cur_key_len = 1
    did_user_continue = "y"
    possible_keys = []
    # initializing all the values

    while cur_key_len <= int(max_keysize) and did_user_continue.lower() == "y":
        possible_keys.append([''.join(letter) for letter in product(string.ascii_lowercase, repeat=cur_key_len)])
        # This will be all of the possible keys for the given key length less than the max key size.
        # It will try all the single letter keys, double, and then triple letter keys... up to the max key size.
        # the possible keys array will always be an array of all permutations of the key given a size.

        for possible_key in possible_keys[cur_key_len - 1]:
            if decrypt(ecrypted_text, possible_key, known_plt):
                did_user_continue = raw_input("Would you like to continue to brute force?:  ")
                if not did_user_continue.lower() == "y":
                    break

        if not did_user_continue.lower() == "y":
            break

        print("Finished trying keys of length: " + str(cur_key_len))
        did_user_continue = raw_input("Would you like to continue to brute force?:  ")

        cur_key_len = cur_key_len + 1

    print("End of brute forcing.")


encrypted_input = raw_input("\nPlease enter a encoded string that used the Vignere Cipher: ")
known_part_of_plaintext = raw_input("Please enter the part of the plain text you know: ")
max_key_size = raw_input("Please enter the max key size: (1 - 10)")

brute_force(known_part_of_plaintext, max_key_size, encrypted_input)