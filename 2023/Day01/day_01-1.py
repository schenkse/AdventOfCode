# read in the document
infile = open('input.txt', 'r')
inlines = infile.readlines()

# helper function to extract the digits from a string
def find_digits(string):
    # split string into characters
    split_string = [*string]
    digits = [int(i) for i in split_string if i.isdigit()]
    return digits

sum = 0
for line in inlines:
    # remove newline character
    line = line.strip()
    digits_in_line = find_digits(line)
    # add the first and the last digit and convert to integer
    calibration_value = int(str(digits_in_line[0]) + str(digits_in_line[-1]))
    sum += calibration_value

print('The sum of all calibration values is: ', sum)