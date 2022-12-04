"""
The RSA asymetric cipher
"""
from math import gcd
import random as rnd
from utils import get_random_prime, mod_inverse
import re
PRIME_NUMBER_LENGHT = 11

DELIMITER = 1

def rsa_encrypt(text: str, key: str, encoding: str, *args, **kwargs) -> str:
    e = int(match[0].split(':')[1]) if (match:= re.search(r"e:\d+", key)) else None
    n = int(match[0].split(':')[1]) if (match := re.search(r"n:\d+", key)) else None

    if not n or not e:
        return None

    encrypted_bytes = bytearray() 

    for byte in bytearray(text, encoding):
        byte = (byte ** e) % n
        bytes_ = byte.to_bytes((byte.bit_length() + 7) // 8, "big")
        bytes__ = bytearray()
        print("EEE", bytes_)
        for byte_ in bytes_: # offseting everything
            bytes__ += (byte_ + DELIMITER + 1).to_bytes(1, 'big')
        encrypted_bytes += bytes__ #byte.to_bytes((byte.bit_length() + 7) // 8, 'big')
        encrypted_bytes += (DELIMITER).to_bytes(1, 'big') # delimiter of  encrypted integers
    print('EEEEE', encrypted_bytes)
    return encrypted_bytes

def rsa_decrypt(text: str, key: str, encoding: str, *args, **kwargs) -> str:
    n = int(match[0].split(':')[1]) if (match:= re.search(r"n:\d+", key)) else None
    d = int(match[0].split(':')[1]) if (match := re.search(r"d:\d+", key)) else None
    if not n or not d:
        return None

    decrypted_bytes = bytearray()

    encrypted_ints_bytes = []
    encrypted_int_bytes = [] 
    for byte in bytearray(text):
        if byte == DELIMITER:
            encrypted_ints_bytes.append(encrypted_int_bytes)
            encrypted_int_bytes = []
        else:
            encrypted_int_bytes.append(byte - DELIMITER - 1)

    encrypted_ints_int = []
    for encrypted_int_bytes_ in encrypted_ints_bytes:
        encrypted_ints_int.append(int.from_bytes(encrypted_int_bytes_, "big"))

    for encrypted_int in encrypted_ints_int:
        decrypted_int = (encrypted_int ** d) % n
        decrypted_bytes += decrypted_int.to_bytes((decrypted_int.bit_length() + 7) // 8, "big")
    
    return decrypted_bytes.decode(encoding)

def rsa_generate_key(*args, **kwargs) -> str:
    p = get_random_prime(PRIME_NUMBER_LENGHT)
    while (q:= get_random_prime(PRIME_NUMBER_LENGHT)) == p: pass # find q

    n = p*q
    phi_n = (p - 1) * (q - 1)
    while gcd(e := rnd.randint(3, phi_n - 1), phi_n) != 1: pass  # find e

    d = mod_inverse(e, phi_n)

    return f"e:{e};n:{n};d:{d}"


rsa_settings = {
    'encrypt_binary_output' : True,
    'decrypt_binary_input' : True,
}