# EnDe
A Fast Encryption-Style Algorithm — **NOT Secure**, use for learning only


## Introduction
**EnDe** Algorithm or **Encryption and Decryption** Algorithm is a program that write in python(v3) programming language.

It uses a simple substitution method which is fast and easy to understand.

**Warning:** this is not a real secure encryption, it can be break without the key file, see the Security Testing section below for detail. Don't use it to protect anything real, use a proper library instead.

This version of EnDe doesn't support text file encryption yet, But this feature may be added latter.

## How to use it?

### Encryption
To Encrypt 'Hello world!' -> **ende.py -e "Hello world!"**

### Decryption
To Decrypt '^sdps^psVnwp' -> **ende.py -d "^sdps^psVnwp"**

### Help message
**run "ende.py -h" to see Help message**

## Security Testing

**EnDe is not secure.** The random number that get use during Encryption get leak inside the ciphertext itself, so anyone can recover the values without ever having `key.py`, than break it like a normal substitution cipher using letter frequency.

This repo also include `break_ende_cipher.py`, a script that test how easy the ciphertext can be break without the key file.

It doesn't need `key.py`, it only need the digit dictionary from `algorithm.py` which is same on every install.

### Break Test
To test a ciphertext -> **python3 break_ende_cipher.py "^sdps^psVnwp"**

It will print the recovered values and a frequency table, so you can compare it with normal letter frequency and see how much information get expose without any key.
