#RSA From Scratch (No Crypto Libraries)

This project implements RSA public-key cryptography **from scratch** in Python, using byte-wise encryption, and manual modular inverse calculation.

##Features

- Pure Python — No external dependencies
- Base64-encoded ciphertext output
- Full encryption/decryption loop
- Educational, readable, and hackable

!!Not Production-Safe!!

This code is built for **education and transparency**, not for secure deployment. Avoid using it for real cryptographic workloads.

##Why Use This?

Unlike most RSA libraries, this project **shows you everything**:
- How prime numbers are tested
- How the public/private keys are calculated
- How plaintext becomes ciphertext
- How decryption works, byte by byte

##Usage

```bash
python3 RSA.py
