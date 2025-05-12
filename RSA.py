from random import randint, randrange
import base64

def is_prime(n, k=10):
    def check(a, s, d, n):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return True
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                return True
        return False

    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    s = 0
    d = n - 1
    while d % 2 == 0:
        d >>= 1
        s += 1

    for _ in range(k):
        a = randrange(2, n - 1)
        if not check(a, s, d, n):
            return False
    return True

def keygen():
    key_p = randint(2**1023, 2**1024)
    while not is_prime(key_p):
        key_p = randint(2**1023, 2**1024)

    key_q = randint(2**1023, 2**1024)
    while not is_prime(key_q):
        key_q = randint(2**1023, 2**1024)

    key_n = key_p * key_q
    phi_n = (key_p - 1) * (key_q - 1)

    key_e = randint(2, phi_n - 1)
    while not is_prime(key_e):
        key_e = randint(2, phi_n - 1)

    old_r, r = key_e, phi_n
    old_s, s = 1, 0

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s

    key_d = old_s % phi_n

    return key_n, key_e, key_d

def encrypt(msg: str, key_n: int, key_e: int) -> str:
    msg_bytes = msg.encode('utf-8')
    msg_int = int.from_bytes(msg_bytes, 'big')
    if msg_int >= key_n:
        raise ValueError("Message too large for the key size.")
    cipher_int = pow(msg_int, key_e, key_n)
    cipher_bytes = cipher_int.to_bytes((cipher_int.bit_length() + 7) // 8, 'big')
    return base64.b64encode(cipher_bytes).decode('utf-8')

def decrypt(cipher_b64: str, key_n: int, key_d: int) -> str:
    cipher_bytes = base64.b64decode(cipher_b64.encode('utf-8'))
    cipher_int = int.from_bytes(cipher_bytes, 'big')
    msg_int = pow(cipher_int, key_d, key_n)
    msg_bytes = msg_int.to_bytes((msg_int.bit_length() + 7) // 8, 'big')
    return msg_bytes.decode('utf-8')

def main():
    print("Generating RSA keypair...")
    key_n, key_e, key_d = keygen()
    print("Key generation successful!")
    
    print(f"Key D: {key_d}")
    print(f"Key N: {key_n}")
    print(f"Key E: {key_e}")
    
    message = "Whatup?"
    print(f"Original Message: {message}")

    cipher_b64 = encrypt(message, key_n, key_e)
    print(f"Encrypted (base64): {cipher_b64}")

    plaintext = decrypt(cipher_b64, key_n, key_d)
    print(f"Decrypted Message: {plaintext}")

if __name__ == "__main__":
    main()
