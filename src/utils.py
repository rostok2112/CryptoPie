from typing import List, Tuple

def recognise_letter_borders(
    letter: str, 
    borders: List[Tuple[str, str]] = [('a', 'z'), ('A', 'Z')]
) -> Tuple[str, str]:
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
    shift_edges: Tuple[str, str] | None = ('a', 'z')
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
