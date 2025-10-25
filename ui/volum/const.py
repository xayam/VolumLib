from volum import entity


class AssertCheckRaise(Exception):
    def __init__(self, *args):
        super().__init__(*args)


def const_get_standart() -> list:
    result = [
        s.lower()
        for s in dir(entity)
        if s.upper() == s and s.endswith("_")
    ]
    result.sort()
    return result


def const_assert_list(check: list) -> None:
    standard = const_get_standart()
    different = set(standard) - set(check)
    if different:
        raise AssertCheckRaise(f"List 'standard' and list 'check' is different: {different}")
    for index in range(len(standard)):
        if check[index] != standard[index]:
            raise AssertCheckRaise(f"'{check[index]}' not equal '{standard[index]}'")


def const_key_dict_to_list(dictionary: dict) -> list:
    result = []
    for key in dictionary:
        result.append(key)
    result.sort()
    return result


if __name__ == "__main__":
    print(const_get_standart())
