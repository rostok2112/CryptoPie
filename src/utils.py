import random as rnd
from math import sqrt, gcd

def recognise_letter_borders(
    letter: str, 
    borders: list[tuple[str, str]] = [('a', 'z'), ('A', 'Z')]
) -> tuple[str, str]:
    """
    Recognising tuple with edges of intervals that may contain an input letter
    ----------
    Parameters:
    + letter - letter for which to find a tuple with borders 
    + edges - list of tuples with left and right edges of intervals that may contain input letter
        Format : [('a', 'z'), ('A', 'Z')]
    """
    
    for edges_tuple in borders:
        if ord(edges_tuple[0]) <= ord(letter) <= ord(edges_tuple[1]): 
            return edges_tuple

def shift_letter(
    letter: str, 
    shift: int = 2, 
    shift_edges: tuple[str, str] | None = ('a', 'z')
) -> str:
    """
    Shifting letter by value of shift relative to the edges passed in shift edges
    ----------
    Parameters:
    + letter - letter to be shifted
    + shift - value by which letter will be shifted
    + shift_edges - tuple with left and right edges  of interval that contain input letter
        Format : ('a', 'z')
    """ 

    shifted_letter_code = ord(letter)

    if shift_edges:
        left_edge = ord(shift_edges[0])
        right_edge = ord(shift_edges[1])
        shifted_letter_code += shift

        if shifted_letter_code > right_edge:
            shifted_letter_code = shifted_letter_code - right_edge + left_edge - 1
        elif shifted_letter_code < left_edge:
            shifted_letter_code = shifted_letter_code - left_edge + right_edge + 1

    return chr(shifted_letter_code)

def shift_string(string: str, shift: int, borders: list[str] = ['a-z', 'A-Z']) -> str:
    """
    Shifting a given string by value of shift relative to the edges passed in shift edges
    ----------
    Parameters:
    + string - string to be shifted
    + shift - value by which letter will be shifted
    + borders - list with  edges pairs of intervals that may contain all letters of input string
        Format : ['a-z', 'A-Z']
    """ 

    return (
        ''
            .join([
                shift_letter(
                    letter, 
                    shift, 
                    recognise_letter_borders(
                        letter, 
                        [border.split('-') for border in borders]
                    )
                ) for letter in string
            ])
    )

def replace_by_dict(string: str, dict_: dict[str, str]) -> str:
    """
    Replacing everything is given in stringto values of dictionary dict_ by keys 
    ----------
    Parameters:
    + string - string whose letters will be replaced 
    + dict_ - dictionary for each key of which in the input string will be replaced by value by this key
    """ 

    replaced_chars = []
    for char in string:
       replaced_chars.append(dict_.get(char, char))
    return ''.join(replaced_chars)

def revert_dict(dict_ : dict[str, str]) -> dict:
    """
    Swaps keys and values of dictionary dict_  
    ----------
    Parameters:
    + dict_ - dictionary for each keys and values will be swapped
    """ 

    return dict(map(reversed, dict_.items()))

def replace_by_list(string: str, list_: list[str]) -> str:
    """
    Replacing everything is given in string to values of list list_ by corresponding index of character in list to character in string
    ----------
    Parameters:
    + string - string whose letters will be replaced 
    + list_ - list for each character of which the corresponding character of input string by index will be replaced
    """ 

    replaced_chars = []
    list_index_dict = dict(enumerate(list_))
    for i, char in enumerate(string):
       replaced_chars.append(list_index_dict.get(i, char))
    return ''.join(replaced_chars)

def shuffle_by_dict(to_shuffle: list, shuffle_indexes: dict[int, int], add_not_shuffled: bool = False) -> list:
    """
    Shuffle list. Replacing value with index is given in key of input dictionary to value with index is given by corresponding value of dictionary
    ----------
    Parameters:
    + to_shuffle - list whose elements will be shuffled 
    + shuffle_indexes - dictionary by which index is given in key a value of input list will be replaced by corresponding value by index is given in value of this dictionary
    + add_not_shuffled - boolean value that responsible for adding not affected values to output list
    """ 
    output_list = []
    for i in range(len(to_shuffle)):
        if not (index_to_replace := shuffle_indexes.get(i, None)):
            key_list = list(shuffle_indexes.keys())
            val_list = list(shuffle_indexes.values())
            try:
                position = val_list.index(i)
            except:
                position = None
            if position:
                index_to_replace = shuffle_indexes[i] = key_list[position]               
        if type(index_to_replace) == int or type(index_to_replace) == tuple or add_not_shuffled:
            if index_to_replace and type(index_to_replace) != tuple:
                if index_to_replace > i:
                    shuffle_indexes[index_to_replace] =  (i, to_shuffle[i])
                else:
                    output_list[index_to_replace or i] = to_shuffle[index_to_replace or i]
            output_list.append(tmp if type(index_to_replace) != tuple and type(tmp := to_shuffle[index_to_replace or i]) != type(None) else index_to_replace[1])

    return output_list

def shuffle_by_list(to_shuffle: list, shuffle_indexes: list[int]) -> list:
    """
    Shuffle input list by values of shuffle list
    ----------
    Parameters:
    + to_shuffle - list whose elements will be shuffled 
    + shuffle_indexes - list with where value by index - is index by which the corresponding value of input list by index will be replaced
    """ 
    return [to_shuffle[shuffle_indexes[i]] for i in range(len(shuffle_indexes))]

def rotate(to_rotate: list, rotate_by: int) -> list:
    """
    Rotating everything is given in input list by given value
    ----------
    Parameters:
    + to_rotate - list whose elements will be rotated 
    + rotate_by - value by which every element of input list will be rotated
    """ 
    return [to_rotate[(i - rotate_by) % len(to_rotate)] for i in range(len(to_rotate))]

def bits_to_int(bits: list[int]) -> int:
    """
    Converting array of bits to integer
    ----------
    Parameters:
    + bits - list of bits to convert
    """
    out = 0
    for bit in bits:
        out = (out << 1) | bit
    return out

def normalize_byte(byte: list[str], len_: int = 8) -> str:
    """
    Appending leading zeros bits to str interpetation of byte
    ----------
    Parameters:
    + byte - string to append leading zeros
    """ 
    if len(byte) < len_: # we need len_ bits in byte
            for i in range(len_ - len(byte)):
                byte = '0' + byte
    return byte

def list_chunks(list_ : list, chunk_lenght: int) -> list[list]:
    """
    Solit list to list of chunks
    ----------
    Parameters:
    + list_ - list to be splitted
    + chunk_lenght - size of 1 chunk
    """ 
    chunk_lenght = max(1, chunk_lenght)

    return [list_[i : i + chunk_lenght] for i in range(0, len(list_), chunk_lenght)]

def split_bits_to_bytes(bits_array: bytes) -> bytes:
    """
    Replace in binary string bits sequence to bytes (b'\x01\x00\x01\x01\x01\x01\x01\x00' -> b'\xbe')
    ----------
    Parameters:
    + bits_array - bits sequence to replace
    """ 
    byte_array = bytes()

    for bits_8 in list_chunks(list(bits_array), 8):
        byte_array += bytes([bits_to_int(bits_8)])

    return byte_array

def is_odd(num: int) -> bool:
    """
    Check if specified number is odd
    ----------
    Parameters:
    + num -  a number to check is odd 
    """
    return num & 1

def mod_inverse(a, m):
    if gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
   
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

def is_prime(num: int) -> bool:
    """
    Wheel factorization algorithm
    """
    # TODO: replace sieve algorithm by any faster modern algorithm for finding prime number
    if not is_odd(num):
        return False

    # The Wheel for checking
    # prime number
    arr = [7, 11, 13, 17, 19, 23, 29, 31]

    # Base Case
    if (num < 2) :
        return False
     
    # Check for the number taken
    # as basis
    if (
        num % 2 == 0
        or num % 3 == 0 
        or num % 5 == 0
    ):
        return False
     
    for i in range(0,int(sqrt(num)), 30):
        for spoke in  arr:
            if spoke > int(sqrt(num)):
                break
            # Check if num is a multiple
            # of prime number in the
            # wheel
            elif num % (spoke + i) == 0:
                return False
    return True

def get_random_prime(bit_length: int) -> int:
    """
    Returns prime number with specified length
    ----------
    Parameters:
    + bit_length -  binary length of prime number
    """ 
    while True:
        num = rnd.getrandbits(bit_length)
        if is_prime(num):
            return num