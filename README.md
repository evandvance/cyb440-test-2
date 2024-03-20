# CYB440 Test 2 Python tool

This tool should be able to do all the requirements to successfully complete
the SPR24 CYB440 Test 2

## Requirements

### Task 1

Create an explination of the advantages/disadvanteges of symmetric encryption

`Symmetric encryption allows for fast encryption. It is best used for 'in place' encryption. That is
encryption where the files dont need to be passed around. However, symmetric encryption requires the same
key for both encryption and decryption. This means that anyone encrypting and decrypting needs access to
the same key. Key security is paramount to the successful use of symmetric encryption.`

Really for the scenario presented in the assignment, asymmetric encryption seems better.

### Task 2

Provide an explanation of what bit-level you plan to utilize within your solution
and why it is the recommended NIST level. Provide insite into the minimum recommended bit-levels.

`This program implements a 256 bit key. This length is used since it is far past the NIST recommended
length of bits (128). This allows for some future development to occur before a change must be made for
the sake of security. This length is recommended because of the ammount of time it would take to
brute force the key. It would take so long, it is infeasable for the encryption to be cracked with
our modern computing abilities.`

### Task 3

Create a way to create a 256-bit or 32-byte key from a passphrase for encryption. Use the password "cryptography"

### Task 4

Create a way to encrypt and decrypt files to protect confidentiality.

### Task 5

Create a method for the user to create a MAC/HMAC for each file before encryption and after decryption

### Task 6

Create a solution that will allow the users to exchange messages or files but also include a MAC to provide an
extra layer of confidence in the authenticity of the file. Use the password "cryptography"

## How to Run this Code

Clone this repo then run:

`python3 main.py`

The terminal will walk you through all your processes and tell what has occured.

## Things to Note

- This program saves your key to KEY.txt and that is the key that would be shared.
- New keys are generated from the same passphrase each time since the salt is random.
- I think I am using pbkdf2 with a pbkdf since that is what is happening in the generate_key function.
- Hashes and HMACs are automated on decryption and written to a file in the files/hmacs or files/hashes folder.
