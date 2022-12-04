"""
A Base64 encoding/decoding algorithm
"""
from utils import bits_to_int, list_chunks, normalize_byte

DICTIONARY = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/" # RFC 4648
ZERO_6BITS = '='

def b64_encode(text: str, encoding: str, *args, **kwargs) -> str:
    encrypted_text = ""

    bytes_ = [normalize_byte(bin(byte)[2:]) for byte in bytearray(text, encoding)] # list with chunks divided by 8 bits
    
    while len(bytes_) % 3: # append zero bytes for dividing by 6 
        bytes_.append("00000000")

    for bit_6 in list_chunks("".join(bytes_), 6): #  get flat bit sequence and divide it to chunks by 6 bits and iterate over of them
        index_in_dict = bits_to_int(list(map(lambda x: int(x), bit_6)))
        if index_in_dict:
            encrypted_text += DICTIONARY[index_in_dict]
        else:
            encrypted_text += ZERO_6BITS

    return encrypted_text

def b64_decode(text: str, encoding: str, *args, **kwargs) -> str:
    decrypted_bytes = bytearray()
    bits = "" 
    for char in text: # get flat bit sequence
        try:
            bits += normalize_byte(bin(DICTIONARY.index(char))[2:], 6)
        except:
            bits += "000000"
    for byte in list_chunks(bits, 8):
        decrypted_bytes += bytearray([bits_to_int(list(map(lambda x: int(x), byte)))])

    return decrypted_bytes.decode(encoding)

b64_settings = {

}
