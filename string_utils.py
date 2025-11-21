def split_before_each_uppercases(formula):
    start = 0
    end = 1
    elements_lst = []
    
    if not formula:
        return elements_lst
    
    while end < len(formula):
        if formula[end].isupper():
            elements_lst.append(formula[start:end])
            start = end
        end += 1
        
    elements_lst.append(formula[start:])
    
    return elements_lst


def split_at_first_digit(formula):
    for char_index, char in enumerate(formula):
        if char.isdigit():
            return formula[:char_index], int(formula[char_index:])
    return formula, 1
