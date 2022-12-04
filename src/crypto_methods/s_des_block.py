"""
A simplified data enceryption standart block cipher cryptographic algorithm
"""
import random as rnd
from utils import rotate, shuffle_by_list, bits_to_int, normalize_byte, split_bits_to_bytes, list_chunks

KEY_BITS = 10
ROUND_KEY_BITS = 8
ROUND_KEY_COUNT = 2
BLOCK_BITS = 8

def _generate_round_subkeys(key: str):
    p10 = shuffle_by_list(key, (2, 4, 1, 6, 3, 9, 0, 8, 7, 5))
    p10_half1 = p10[:len(p10) // 2]
    p10_half2 = p10[len(p10)// 2:]

    p10_half1_1 = rotate(p10_half1, -1)
    p10_half2_1 = rotate(p10_half2, -1)
    p10_half1_2 = rotate(p10_half1_1, -2)
    p10_half2_2 = rotate(p10_half2_1, -2)

    k1 = shuffle_by_list(p10_half1_1 + p10_half2_1, (5, 2, 6, 3, 7, 4, 9, 8))
    k2 = shuffle_by_list(p10_half1_2 + p10_half2_2, (5, 2, 6, 3, 7, 4, 9, 8))

    return (k1, k2)

def _s(bits_4: list, s_matrix: list[list[int]]):
    row = bits_to_int([bits_4[0], bits_4[3]])
    column = bits_to_int([bits_4[1], bits_4[2]])

    return normalize_byte(bin(s_matrix[row][column])[2:])[6:]

def _round_function(bits_4_1: list, bits_4_2: list, round_subkey: list) -> list:
    extended_to_8_bits = shuffle_by_list(bits_4_2, (3, 0, 1, 2, 1, 2, 3, 0))
    for i in range(len(extended_to_8_bits)):
        extended_to_8_bits[i] = int(extended_to_8_bits[i]) ^ int(round_subkey[i])
    extended_to_8_bits = list_chunks(extended_to_8_bits, len(extended_to_8_bits) // 2)

    p_left = extended_to_8_bits[0]
    p_right = extended_to_8_bits[1]

    p_left = _s(
        p_left, 
        s_matrix = [
            [1, 0, 3, 2],
            [3, 2, 1, 0],
            [0, 2, 1, 3],
            [3, 1, 3, 1],
        ]
    )
    p_right = _s(
        p_right, 
        s_matrix = [
            [1, 1, 2, 3],
            [2, 0, 1, 3],
            [3, 0, 1, 0],
            [2, 1, 0, 3],
        ]
    )

    p4 = shuffle_by_list(p_left + p_right, (1, 3, 2, 0))

    return [int(bits_4_1[i]) ^ int(p4[i]) for i in range(len(bits_4_1))]

def s_des_block_encrypt(text: str, key: str, encoding: str, *args, **kwargs) -> bytearray:
    k1, k2 = _generate_round_subkeys(key)
    encrypted_bytes = bytearray() 
    
    for byte in bytearray(text, encoding):
        byte = bin(byte)[2:] # get bits array without 0b
        byte = normalize_byte(byte)

        byte = shuffle_by_list(byte, (1, 5, 2, 0, 3, 7, 4, 6)) # IP^1
        byte = list_chunks(byte, len(byte) // 2)

        left_4_bits = byte[0]
        right_4_bits = byte[1]
    
        left_4_bits = _round_function(left_4_bits, right_4_bits, k1)
        right_4_bits = _round_function(right_4_bits, left_4_bits, k2)

        encrypted_bytes += bytearray(shuffle_by_list(right_4_bits + left_4_bits, (3, 0, 2, 4, 6, 1, 7, 5))) # IP^-1

    return split_bits_to_bytes(encrypted_bytes)

def s_des_block_decrypt(text: str, key: str, encoding: str, *args, **kwargs) -> str:
    k1, k2 = _generate_round_subkeys(key)
    decrypted_bytes = bytearray() 

    for byte in bytearray(text):
        byte = bin(byte)[2:] # get bits array without 0b
        byte = normalize_byte(byte)
        
        byte = shuffle_by_list(byte, (1, 5, 2, 0, 3, 7, 4, 6))
        byte = list_chunks(byte, len(byte) // 2)

        left_4_bits = byte[0]
        right_4_bits = byte[1]

        left_4_bits = _round_function(left_4_bits, right_4_bits, k2)
        right_4_bits = _round_function(right_4_bits, left_4_bits, k1)

        decrypted_bytes += bytearray(shuffle_by_list(right_4_bits + left_4_bits, (3, 0, 2, 4, 6, 1, 7, 5)))

    return split_bits_to_bytes(decrypted_bytes).decode(encoding) 

def s_des_block_generate_key(*args, **kwargs) -> str:
    return ''.join([str(rnd.randint(0, 1)) for i in range(KEY_BITS)])

s_des_block_settings = {
    'encrypt_binary_output' : True,
    'decrypt_binary_input' : True,
}