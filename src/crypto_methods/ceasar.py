"""
Ceasar cipher 
"""
import random as rnd
from utils import shift_string

def ceasar_encrypt(text: str, key: int, borders: list[str] = ['a-z', 'A-Z'], *args, **kwargs) -> str:
    return shift_string(text, int(key), borders)
    
def ceasar_decrypt(text: str, key: int, borders: list[str] = ['a-z', 'A-Z'], *args, **kwargs) -> str:
    return shift_string(text, -int(key), borders)

def ceasar_generate_key(borders: list[str] = ['a-z', 'A-Z'], *args, **kwargs) -> int:
    max_key = max(
        map(
            lambda edges: ord(edges[1]) - ord(edges[0]),
            [border.split('-') for border in borders]
        )
    )
    return rnd.randint(1, max_key)

ceasar_settings = {

}