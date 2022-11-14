import random as rnd
from utils import shift_string

def cesar_encrypt(text: str, key: int, borders: list[str] = ['a-z', 'A-Z'], *args) -> str:
    return shift_string(text, int(key), borders)
    
def cesar_decrypt(text: str, key: int, borders: list[str] = ['a-z', 'A-Z'], *args) -> str:
    return shift_string(text, -int(key), borders)

def cesar_generate_key(borders: list[str] = ['a-z', 'A-Z'], *args) -> int:
    max_key = max(
        map(
            lambda edges: ord(edges[1]) - ord(edges[0]),
            [border.split('-') for border in borders]
        )
    )
    return rnd.randint(1, max_key)
