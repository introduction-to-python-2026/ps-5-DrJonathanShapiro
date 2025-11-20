def split_before_uppercases(formula):
    if not formula:
        return []

    parts = []
    start = 0

    for i in range(1, len(formula)):
        if formula[i].isupper():
            parts.append(formula[start:i])
            start = i

    parts.append(formula[start:])
    return parts


def split_at_digit(formula):
    i = 0
    # move i until we hit the first digit
    while i < len(formula) and not formula[i].isdigit():
        i += 1

    if i == len(formula):
        return formula, 1

    name = formula[:i]
    count = int(formula[i:])
    return name, count


def count_atoms_in_molecule(molecular_formula):

    atom_counts = {}

    for atom in split_before_uppercases(molecular_formula):
        atom_name, atom_count = split_at_digit(atom)

        atom_counts[atom_name] = atom_counts.get(atom_name, 0) + atom_count

    return atom_counts
