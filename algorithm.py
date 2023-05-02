# Import Library
import random

# Strating Project

# Important Data Dictionaries
from key import *

final_encryption_dictionary =  {'0': 's', '1': 'p', '2': 'n', '3': 'd', '4': 'o', '5': '^', '6': '#', '7': '1', '8': 'V', '9': 'w'}

final_decryption_dictionary =  {'s': '0', 'p': '1', 'n': '2', 'd': '3', 'o': '4', '^': '5', '#': '6', '1': '7', 'V': '8', 'w': '9'}

# Encryption Function Get String Data From User
def encryption(data) :

    # Varibles
    first_encrypt = ''
    final_encrypt = ''

    # "Letter by Letter" Encryption Loop
    for letter in data :

        random_number = random.randint(1,9)
        letter_encryption = str(int(encryption_dictionary[str(letter)]) * random_number) + str(random_number)
        first_encrypt += letter_encryption

    # finally Encryption Loop
    for number in first_encrypt :
        final_encrypt += final_encryption_dictionary[number]

    # Final Output
    return(final_encrypt)

# Decryption Function Get String Data From User
def decryption(data) :

    # Varibles
    first_decrypt = ''
    final_decrypt = ''
    letter_number = 0

    # Convert letters to numbers
    for letter in data:
        first_decrypt += str(final_decryption_dictionary[letter])

    # Parting numbers to find letters
    while (letter_number+6) <= len(first_decrypt):

        # Parting numbers
        encrypted_letter = first_decrypt[letter_number:letter_number+6]
        multiplied_number = encrypted_letter[0:5]
        random_number = encrypted_letter[5]
        original_number = int(int(multiplied_number) / int(random_number))

        # Finding letters by check decryption dictionary
        final_decrypt += decryption_dictionary[original_number]

        # Go to next letter
        letter_number += 6

    # Final Output
    return(final_decrypt)


# Check Collision Probability of Encryption
def Collision_probability(length):

    # Varible
    Collision_probability_percent = "%"+str(100 / (9 ** length))

    return(Collision_probability_percent)
