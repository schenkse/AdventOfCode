import re

bag_ncubes = {
    'red' : 12,
    'green' : 13,
    'blue' : 14
}
    
def find_color_count(string):
    colors = string.split(',')
    colors = [s.strip() for s in colors]

    # create emtpy dictionary
    color_count = {
        'red' : 0,
        'green' : 0,
        'blue' : 0
    }
    for ncubes in colors:
        count, color = ncubes.split()
        count = count.strip()
        color = color.strip()
        color_count[color] = int(count)
    
    return color_count

def find_max_colors_per_game(draw_colors):
    max_r = 0
    max_g = 0
    max_b = 0
    for draw in draw_colors:
        color_count = find_color_count(draw)
        if color_count['red'] > max_r:
            max_r = color_count['red']
        if color_count['green'] > max_g:
            max_g = color_count['green']
        if color_count['blue'] > max_b:
            max_b = color_count['blue']
    res = {
        'red' : max_r,
        'green' : max_g,
        'blue' : max_b
    }
    return res

def find_game_max_colors(string):
    game, draws = string.split(':')
    game = game.strip()
    # assume that every game has an ID
    game_id = int(re.findall(r'\d+', game)[0])
    draw_colors = draws.split(';')
    draw_colors = [x.strip() for x in draw_colors]

    max_colors = find_max_colors_per_game(draw_colors)

    return game_id, max_colors

def test_case():
    infile = open('test_input.txt', 'r')
    inlines = infile.readlines()

    sum = 0
    for line in inlines:
        # remove newline character
        line = line.strip()
        game_id, max_colors = find_game_max_colors(line)
        if (max_colors['red'] <= bag_ncubes['red']
            and max_colors['green'] <= bag_ncubes['green']
            and max_colors['blue'] <= bag_ncubes['blue']):
            sum += game_id
    
    assert sum == 8
    print('Test passed.')

def main():
    infile = open('input.txt', 'r')
    inlines = infile.readlines()

    sum = 0
    for line in inlines:
        # remove newline character
        line = line.strip()
        game_id, max_colors = find_game_max_colors(line)
        if (max_colors['red'] <= bag_ncubes['red']
            and max_colors['green'] <= bag_ncubes['green']
            and max_colors['blue'] <= bag_ncubes['blue']):
            sum += game_id

    print('The sum of possible game IDs is: ', sum)

if __name__ == '__main__':
    test_case()
    main()