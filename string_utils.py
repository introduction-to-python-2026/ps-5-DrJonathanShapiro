def split_before_uppercases(formula):
    """Split a formula before each uppercase letter.
       Example: 'C6H12O6' -> ['C6', 'H12', 'O6']"""
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
    """Split 'Na2' -> ('Na', 2), 'O' -> ('O', 1)."""
    idx = 0
    while idx < len(formula) and not formula[idx].isdigit():
        idx += 1

    # no digits → count = 1
    if idx == len(formula):
        return formula, 1

    name = formula[:idx]
    num = int(formula[idx:])
    return name, num


def count_atoms_in_molecule(molecular_formula):
    """Takes a molecular formula (string) and returns a dictionary of atom counts.
       Example: 'H2O' → {'H': 2, 'O': 1}"""

    atom_counts = {}    # Step 1: empty dict

    # IMPORTANT: use the new function names here:
    for atom in split_before_uppercases(molecular_formula):
        atom_name, atom_count = split_at_digit(atom)

        # Step 2: update the dict
        atom_counts[atom_name] = atom_counts.get(atom_name, 0) + atom_count

    # Step 3: return the dict
    return atom_counts
