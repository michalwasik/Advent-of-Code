import typing


def ints(s: str) -> typing.List[int]:
    return lmap(int, re.findall(r"(?:(?<!\d)-)?\d+", s))  # thanks mserrano!


def words(s: str) -> typing.List[str]:
    return re.findall(r"[a-zA-Z]+", s)
