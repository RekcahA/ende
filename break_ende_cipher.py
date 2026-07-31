#!/usr/bin/env python3

# Import Library
import sys
from collections import Counter

# Starting Project

# This code breaks EnDe ciphertext without needing key.py
# It only needs the final decryption dictionary from algorithm.py
# because the random number is leaked inside the ciphertext itself

# Final Decryption Dictionary (copied from algorithm.py, same on every install)
final_decryption_dictionary =  {'s': '0', 'p': '1', 'n': '2', 'd': '3', 'o': '4', '^': '5', '#': '6', '1': '7', 'V': '8', 'w': '9'}


# Recover Value Function Get Ciphertext Data From User
def recover_value_sequence(data) :

    # Varibles
    raw_digits = ''
    values = []
    letter_number = 0

    # Convert letters to numbers
    for letter in data :
        raw_digits += final_decryption_dictionary[letter]

    if len(raw_digits) % 6 != 0 :
        print("[ERROR] Ciphertext length is not a multiple of 6, not valid EnDe output.")
        sys.exit(1)

    # Parting numbers to find original values
    while (letter_number+6) <= len(raw_digits) :

        # Parting numbers
        encrypted_letter = raw_digits[letter_number:letter_number+6]
        multiplied_number = encrypted_letter[0:5]
        random_number = encrypted_letter[5]

        # Finding value by removing the leaked random number
        original_value = int(int(multiplied_number) / int(random_number))
        values.append(original_value)

        # Go to next letter
        letter_number += 6

    # Final Output
    return(values)


# Frequency Function Get Values List From User
def frequency_report(values) :

    # Count how many times each value shows up
    # Same value always means same plaintext character
    counted = Counter(values)

    return(counted.most_common())


# Main Program
if len(sys.argv) != 2 :
    print("Usage: python3 break_ende.py \"<ciphertext>\"")
    sys.exit(1)

ciphertext = sys.argv[1]
value_sequence = recover_value_sequence(ciphertext)

print("[+]", len(value_sequence), "characters recovered, zero brute force, zero key.py needed.")
print("[+] Recovered value sequence (same as a classic substitution ciphertext) :")
print("   ", value_sequence)
print('\n')

print("[+] Frequency table (value : count), match this against normal letter frequency :")
for value, count in frequency_report(value_sequence) :
    print("   ", value, ":", count)
print('\n')

print("[!] If you also have a known or leaked key.py (like the default one on github),")
print("    plaintext is recovered directly with no analysis needed at all.")
