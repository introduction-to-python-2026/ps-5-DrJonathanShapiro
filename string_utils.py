def split_before_uppercases(formula):
    """Splits a chemical formula before each uppercase letter."""
    if not formula:
        return []

    parts = []
    current = ""

    for char in formula:
        if char.isupper() and current != "":
            parts.append(current)
            current = char
        else:
            current += char

    parts.append(current)
    return parts


def split_at_digit(formula):
    """Splits element string into (element_name, count)."""
    name = ""
    number = ""

    for char in formula:
        if char.isdigit():
            number += char
        else:
            name += char

    if number == "":
        number = "1"

    return name, int(number)


def count_atoms_in_molecule(molecular_formula):
    """Takes a molecular formula (string) and returns a dictionary of atom counts.
       Example: 'H2O' → {'H': 2, 'O': 1}"""

    atom_counts = {}

    for atom in split_before_uppercases(molecular_formula):
        atom_name, atom_count = split_at_digit(atom)
        atom_counts[atom_name] = atom_counts.get(atom_name, 0) + atom_count

    return atom_counts
