def to_int_list(inp: str, seperator=",") -> [int]:
    splits = inp.split(seperator)
    splits = filter(lambda x: x, splits)
    return list(map(lambda x: int(x), splits))
