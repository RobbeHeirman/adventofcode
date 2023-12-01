from core.matrix import Matrix


def parse_int_lst(in_str: str, seperator="\n") -> [int]:
    """
    Takes strings like
    '
    1
    2
    4
    5
    ...
    And converts this to [1, 2, 4, 5]
    '
    """
    return list(map(lambda x: int(x), in_str.split(seperator)))


def parse_matrices(in_str: str) -> [Matrix]:
    """
    Takes strings like
    '
    86 46 47 61 57
    44 74 17  5 87
    78  8 54 55 97
    11 90  7 75 70
    81 50 84 10 60

    47 28 64 52 44
    73 48 30 15 53
    57 21 78 75 26
    51 39 72 18 25
    29 76 83 54 82
    ...
    '
    and converts to = [Matrix, Matrix]
    """
    m_string_lst = in_str.split("\n\n")
    valids = filter(lambda m_str: m_str, m_string_lst)
    return list(map(lambda l_str: Matrix.create_matrix(l_str), valids))


