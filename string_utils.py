def split_before_each_uppercases(formula):
    if not formula:
        return []
    start = 0
    split_formula = []
    for i in range(1, len(formula)):
        if formula[i].isupper():
            split_formula.append(formula[start:i])
            start = i
    split_formula.append(formula[start:])
    return split_formula


def split_at_first_digit(formula):
    for i in range(1, len(formula)):
        if formula[i].isdigit():
            prefix = formula[:i]
            num = int(formula[i:])
            return prefix, num
            break

    return formula, 1


def count_atoms_in_molecule(molecular_formula):
    atom_counts = {}
    for atom in split_before_uppercases(molecular_formula):
        atom_name, atom_count = split_at_digit(atom)
        atom_counts[atom_name] = atom_count
    return atom_counts


def parse_chemical_reaction(reaction_equation):
    reaction_equation = reaction_equation.replace(" ", "")
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")


def count_atoms_in_reaction(molecules_list):
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count

