"""
Additive stream cipher with simplified key
"""
import random as rnd
from utils import recognise_letter_borders

def _generate_gamming_sequence(text: str, key: str) -> dict[tuple[str, str], list[int]]:
    interval_keys_dict = {}
    for interval_key_pair in key.split(';'):
        interval, interval_key = interval_key_pair.split(':')
        interval_keys_dict[tuple(interval.split('-'))] = [int(key_) for key_ in interval_key.split(',')]
    
    for interval in interval_keys_dict.keys(): # appending key  sequence to length of text
        interval_keys_arr = interval_keys_dict[interval]
        interval_keys_length = len(interval_keys_arr)
        interval_length = ord(interval[1]) - ord(interval[0]) + 1
        for i in range(len(text) - interval_keys_length + 1):
            interval_keys_arr.append(
                (interval_keys_arr[i] + interval_keys_arr[i + interval_keys_length - 1]) 
                % 
                interval_length
            )

    intervals_gamming_sequenses = {}
    for interval in interval_keys_dict.keys():
        interval_keys_length = len(interval_keys_dict[interval])
        interval_length = ord(interval[1]) - ord(interval[0]) + 1
        interval_keys_arr = interval_keys_dict[interval]
        intervals_gamming_sequenses[interval] = [
            (interval_keys_arr[i] + interval_keys_arr[i + 1])
            %
            interval_length

            for i in range(len(interval_keys_arr) - 1)
        ]

    return intervals_gamming_sequenses

def additive_stream_encrypt(text: str, key: str, borders: list[str] = ['a-z', 'A-Z'], *args, **kwargs) -> str:
    intervals_gamming_sequenses = _generate_gamming_sequence(text, key)
    edges = [tuple(edges.split('-')) for edges in borders]
    encrypted_characters = []

    for i, char in enumerate(text):
        interval = recognise_letter_borders(char, edges)
        if interval:
            gamming_sequence = intervals_gamming_sequenses.get(interval)
            if gamming_sequence:
                interval_length = ord(interval[1] ) - ord(interval[0]) + 1
                serial_number = ord(char) - ord(interval[0]) # serial number inside interval 
                encrypted_characters.append(
                    chr(
                        (
                            (serial_number + gamming_sequence[i])
                            %
                            interval_length
                        )
                        +
                        ord(interval[0])
                    )
                )
            else:
                encrypted_characters.append(char)
        else:
            encrypted_characters.append(char)

    return "".join(encrypted_characters)

def additive_stream_decrypt(text: str, key: str, borders: list[str] = ['a-z', 'A-Z'], *args, **kwargs) -> str:
    intervals_gamming_sequenses = _generate_gamming_sequence(text, key)
    edges = [tuple(edges.split('-')) for edges in borders]
    decrypted_characters = []

    for i, char in enumerate(text):
        interval = recognise_letter_borders(char, edges)
        if interval:
            gamming_sequence = intervals_gamming_sequenses.get(interval)
            if gamming_sequence:
                interval_length = ord(interval[1] ) - ord(interval[0]) + 1
                
                serial_number = ord(char) - ord(interval[0]) # serial number inside interval 
                decrypted_characters.append(
                    chr(
                        (
                            (serial_number + (interval_length - gamming_sequence[i]))
                            %
                            interval_length
                        )
                        +
                        ord(interval[0]) 
                    )
                )
            else:
                decrypted_characters.append(char)
        else:
            decrypted_characters.append(char)
    return "".join(decrypted_characters)

def additive_stream_generate_key(borders: list[str] = ['a-z', 'A-Z'], key_length: int = 3, *args, **kwargs) -> str:
    if len(borders):
        key_parts = []
        for i, edges in enumerate(border.split('-') for border in borders):
            interval_length = ord(edges[1]) - ord(edges[0]) + 1
            key_parts.append(f"{borders[i]}:{','.join([str(rnd.randint(0, interval_length - 1)) for i_ in range(key_length)])}") 

        return ';'.join(key_parts)

additive_stream_settings = {

}