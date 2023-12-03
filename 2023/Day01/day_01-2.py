valid_digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9',
                'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
valid_digits_r = [x[::-1] for x in valid_digits]
digits_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

# helper functions to extract the valid digits from a string
def find_first_digit(string, valid_strings=valid_digits):
    digit_index_min = len(string)
    for digit in valid_strings:
        digit_index_low = string.find(digit)
        if digit_index_low == 0:
            res = digit
            break
        elif digit_index_low < digit_index_min and digit_index_low != -1:
            res = digit
            digit_index_min = digit_index_low

    return res

def find_last_digit(string):
    reversed_string = string[::-1]
    digit_reversed = find_first_digit(reversed_string, valid_digits_r)
    res = digit_reversed[::-1]

    return res

def find_calibration_value(string):
    first_digit = find_first_digit(string)
    last_digit = find_last_digit(string)

    # check if string is a word or a number
    if len(first_digit) > 1:
        first_digit = digits_dict[first_digit]
    if len(last_digit) > 1:
        last_digit = digits_dict[last_digit]

    calibration_value = int(first_digit + last_digit)

    return calibration_value
        
def test_case():
    infile = open('test_input.txt', 'r')
    inlines = infile.readlines()

    sum = 0
    for line in inlines:
        # remove newline character
        line = line.strip()
        calibration_value = find_calibration_value(line)
        sum += calibration_value

    assert sum == 281
    print('Test passed.')

def main():
    # read in the document
    infile = open('input.txt', 'r')
    inlines = infile.readlines()

    sum = 0
    for line in inlines:
        # remove newline character
        line = line.strip()
        calibration_value = find_calibration_value(line)
        sum += calibration_value

    print('The sum of all calibration values is: ', sum)
    
if __name__ == '__main__':
    test_case()
    main()