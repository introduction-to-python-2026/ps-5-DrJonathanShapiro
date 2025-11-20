def split_before_uppercases(formula):
    """Splits a chemical formula into parts before each uppercase letter.
       Example: 'C6H12O6' -> ['C6', 'H12', 'O6']"""
    if not formula:
        return []

    parts = []
    start = 0

    # start from index 1 so we don't split before the very first character
    for i in range(1, len(formula)):
        if formula[i].isupper():
            parts.append(formula[start:i])
            start = i

    parts.append(formula[start:])
    return parts


def split_at_digit(formula):
    """Splits 'Na2' -> ('Na', 2) and 'O' -> ('O', 1)."""
    i = 0
    # move i until we hit the first digit
    while i < len(formula) and not formula[i].isdigit():
        i += 1

    # no digits -> count is 1
    if i == len(formula):
        return formula, 1

    name = formula[:i]
    count = int(formula[i:])
    return name, count


def count_atoms_in_molecule(molecular_formula):
    """Takes a molecular formula (string) and returns a dictionary of atom counts.  
    Example: 'H2O' → {'H': 2, 'O': 1}"""

    # Step 1: Initialize an empty dictionary to store atom counts
    atom_counts = {}

    # use the *new* helper functions here
    for atom in split_before_uppercases(molecular_formula):
        atom_name, atom_count = split_at_digit(atom)

        # Step 2: Update the dictionary with the atom name and count
        atom_counts[atom_name] = atom_counts.get(atom_name, 0) + atom_count

    # Step 3: Return the completed dictionary
    return atom_counts
