import string_utils as su
import equation_utils as eu


def balance_reaction(reaction):
    """
    Given a chemical reaction as a string, return a list of coefficients
    (reactants then products), with the last product's coefficient fixed to 1.

    Examples (what the tests expect):
        "Fe2O3 + H2 -> Fe + H2O"  -> [1/3, 1, 2/3, 1]
        "CH4 + O2 -> CO2 + H2O"   -> [1/2, 1, 1/2, 1]
        "C3H8 + O2 -> CO2 + H2O"  -> [1/4, 5/4, 3/4, 1]
        "H2 + O2 -> H2O"          -> [1, 1/2, 1]
        "N2 + H2 -> NH3"          -> [1/2, 3/2, 1]
    """

    # 1. parse reaction into lists of formulas
    reactants, products = su.parse_chemical_reaction(reaction)

    # 2. count atoms in each formula
    reactant_atoms = su.count_atoms_in_reaction(reactants)
    product_atoms = su.count_atoms_in_reaction(products)

    # 3. build and solve the system of equations
    equations, coefficients = eu.build_equations(reactant_atoms, product_atoms)

    # coefficients is only for:
    # - all reactants
    # - all products EXCEPT the last (which is fixed to 1 inside equation_utils)
    solution_coeffs = eu.my_solve(equations, coefficients)

    # append the last product coefficient (fixed to 1 by convention)
    return solution_coeffs + [1]
