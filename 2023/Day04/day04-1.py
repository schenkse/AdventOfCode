def extract_numbers_from_game(string):
    numbers = string.split(':')[-1]
    winning_numbers = numbers.split('|')[0].split()
    your_numbers = numbers.split('|')[-1].split()
    
    winning_numbers = [int(n) for n in winning_numbers]
    your_numbers = [int(n) for n in your_numbers]

    return winning_numbers, your_numbers

def compute_points_per_game(numbers, winning_numbers):
    your_winning_numbers = [number for number in numbers if number in winning_numbers]
    if len(your_winning_numbers) == 0:
        return 0
    return 2**(len(your_winning_numbers)-1)

def compute_total_points(fname):
    with open(fname, 'r') as fin:
        farray = fin.readlines()
    farray = [x.strip() for x in farray]

    total_points = 0
    for line in farray:
        winning_numbers, your_numbers = extract_numbers_from_game(line)
        total_points += compute_points_per_game(your_numbers, winning_numbers)
        
    
    return total_points

def test_case():
    assert compute_total_points('test_input.txt') == 13
    print('Test passed.')

def main():
    total_points = compute_total_points('input.txt')
    print('Your total points are: ', total_points)

if __name__ == '__main__':
    test_case()
    main()