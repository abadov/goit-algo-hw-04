from pathlib import Path
from typing import TypedDict


class Cat(TypedDict):
    id: str
    name: str
    age: str

def get_cats_info(path: str) -> list[Cat]:
    """
    Reads file with cats and returns a list of Cat dictionaries. See definition of the Cat class.
    :param path: str
    :return: list of Cats
    """

    def get_cat(line: str) -> Cat:
        id, name, age = line.strip().split(',')
        return {
            "id": id,
            "name": name,
            "age": age
        }

    cats_info = [];

    p = Path(path)
    if not p.exists():
        print('Path does not exist')
        return cats_info

    if p.is_dir():
        print('Path is not a file')
        return cats_info

    with open(path, 'r') as fh:
        cats_info = [get_cat(line) for line in fh.readlines()]
    fh.close()

    return cats_info

print(get_cats_info('cats.txt'))
