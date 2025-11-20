def split_before_uppercases(formula: str) -> list:
    parts = []
    current = ""

    for char in formula:
        if char.isupper() and current != "":
            parts.append(current)
            current = char
        else:
            current += char

    if current:
        parts.append(current)

    return parts


def split_at_digit(element: str) -> tuple:
    name = ""
    number = ""

    for char in element:
        if char.isdigit():
            number += char
        else:
            name += char

    if number == "":
        number = "1"

    return name, int(number)
