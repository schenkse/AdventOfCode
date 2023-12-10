import re

def find_special_characters(farray):
    carray = []
    for line in farray:
        spans = [m.span() for m in re.finditer(r'[^.,a-zA-Z0-9 \n\.]', line)]
        cindices = [index for span in spans for index in range(*span)]
        carray.append(cindices)

    return carray

def find_numbers(farray):
    narray = []
    for line in farray:
        nindices = [(range(*m.span()), m.group()) for m in re.finditer(r'\d+', line)]
        narray.append(nindices)

    return narray

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

# check if surrounding array contains at least one adjacent special character
def has_adjacent_char(surrounding_array):
    for line in surrounding_array:
        if re.findall(r'[^.,a-zA-Z0-9 \n\.]', line):
            return True
    
    return False

def find_numbers_with_adjacent_chars(farray):
    numbers = []
    for line_number, line in enumerate(farray):
        for m in re.finditer(r'\d+', line):
            surround_array = find_surrounding_array(farray, m.span(), line_number)
            if has_adjacent_char(surround_array):
                numbers.append(int(m.group()))

    return numbers

def sum_numbers(fname):
    with open(fname, 'r') as fin:
        farray = fin.readlines()
    farray = [x.strip() for x in farray]

    numbers = find_numbers_with_adjacent_chars(farray)
    return sum(numbers)

def test_case():
    assert sum_numbers('test_input.txt') == 4361
    print('Test passed.')

def main():
    sum = sum_numbers('input.txt')
    print('The sum of all numbers is: ', sum)

if __name__ == '__main__':
    test_case()
    main()