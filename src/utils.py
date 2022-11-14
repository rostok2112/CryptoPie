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

def replace_by_dict(string: str, dict_: dict[str, str]):
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

def revert_dict(dict_ : dict[str, str]):
    """
    Swaps keys and values of dictionary dict_  
    ----------
    Parameters:
    + dict_ - dictionary for each keys and values will be swapped
    """ 

    return dict(map(reversed, dict_.items()))

def replace_by_list(string: str, list_: list[str]):
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