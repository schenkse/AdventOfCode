import numpy as np
import re

def find_gear_indices(farray):
    gear_indices = []
    for line_number, line in enumerate(farray):
        column_number = line.find('*')
        if column_number != -1:
            gear_array = find_surrounding_array(farray, range(column_number, column_number+2), line_number)
            if is_gear(gear_array):
                gear_indices.append((line_number, column_number))

    return gear_indices

def is_gear(surrounding_array):
    digits = []
    for line in surrounding_array:
        digits_search = re.findall(r'\d+', line)
        if digits_search:
            for digit in digits_search:
                digits.append(digit)

    if len(digits) == 2:
        return True
    else:
        return False

def find_surrounding_array(farray, number_range, line_number):
    # define index range for lines and columns
    if line_number == 0:
        line_start = line_number
        line_end = line_number + 1
    elif line_number == len(farray)-1:
        line_start = line_number - 1
        line_end = line_number
    else:
        line_start = line_number - 1
        line_end = line_number + 1
    line_range = range(line_start, line_end+1)
    column_start = number_range[0]
    column_end = number_range[-1]
    if column_start != 0:
        column_start -= 1
    # WARNING: assume array here
    if column_end != len(farray[0]):
        column_end += 1

    surrounding_array = [farray[line][column_start:column_end] for line in line_range]

    return surrounding_array

# construct surrounding array around gear
def find_gear_numbers(farray, gear_index):
    gear_line, gear_column = gear_index
    # define index range for lines and columns
    if gear_line == 0:
        line_start = gear_line
        line_end = gear_line + 1
    elif gear_line == len(farray)-1:
        line_start = gear_line - 1
        line_end = gear_line
    else:
        line_start = gear_line - 1
        line_end = gear_line + 1

    gear_numbers = []
    for line in farray[line_start:line_end+1]:
        for m in re.finditer(r'\d+', line):
            if gear_column in range(*m.span()) or gear_column-1 in range(*m.span()) or gear_column+1 in range(*m.span()):
                gear_numbers.append(int(m.group()))
    
    return gear_numbers


def find_all_gear_ratios(farray):
    gear_indices = find_gear_indices(farray)
    gear_ratios = [np.prod(find_gear_numbers(farray, gear_index)) for gear_index in gear_indices]

    return gear_ratios

def sum_all_gear_ratios(fname):
    with open(fname, 'r') as fin:
        farray = fin.readlines()
    farray = [x.strip() for x in farray]

    gear_ratios = find_all_gear_ratios(farray)
    return sum(gear_ratios)

def test_case():
    assert sum_all_gear_ratios('test_input.txt') == 467835
    print('Test passed.')

def main():
    sum = sum_all_gear_ratios('input.txt')
    print('The sum of all gear ratios is: ', sum)

if __name__ == '__main__':
    test_case()
    main()