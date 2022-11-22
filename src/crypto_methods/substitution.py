import random as rnd
from utils import replace_by_dict, revert_dict

def substitution_encrypt(text: str, key: str, *args, **kwargs) -> str:
    return (
        replace_by_dict(
            text,
            dict([key_value.split(':') for  key_value in key.split(',')]),
        ) 
    )

def substitution_decrypt(text: str, key: str, *args, **kwargs) -> str:
    return (
        replace_by_dict(
            text, 
            revert_dict(dict([key_value.split(':') for  key_value in key.split(',')])),
        ) 
    )

def substitution_generate_key(borders: list[str] = ['a-z', 'A-Z'], *args, **kwargs) -> str:
    if len(borders):
        replacement_map = {}
        for edges in (border.split('-') for border in borders):
            interval_range = range(ord(edges[0]), ord(edges[1]) + 1)
            rnd.shuffle(random_replacements := list(interval_range))
            replacement_map |= {
                chr(letter) : chr(random_replacements[letter - ord(edges[0])])
                    for letter in interval_range
            }
        return ','.join([f"{key}:{value}" for key, value in replacement_map.items()])
