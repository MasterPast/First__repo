from random import randint

SIZE_M = 5
SIZE_N = 5

char_x = randint(0, SIZE_N - 1)
char_y = randint(0, SIZE_M - 1)
char_sign = 'X'
win_condition = False
turns = 0

exit_x = randint(0, SIZE_N - 1)
exit_y = randint(0, SIZE_M - 1)

while True:
    world_map = ''
    win_condition = char_x == exit_x and char_y == exit_y
    if win_condition:
        char_sign = 'W'

    for j in range(SIZE_M):
        row = '|'

        for i in range(SIZE_N):

            if char_x == i and char_y == j:
                row += f'{char_sign}|'
            elif exit_x == i and exit_y == j:
                row += '0|'
            else:
                row += ' |'

        world_map += f'{row}\n'
    
    print()
    print(world_map)

    if win_condition:
        print(f'You won in {turns} turns!!!!!!')
        break
    
    direction = input("Direction? (u / d / l / r)")
    
    if direction == 'u' and char_y != 0:
        char_y -= 1
    elif direction == 'd' and char_y != SIZE_M-1:
        char_y += 1
    elif direction == 'l' and char_x != 0:
        char_x -= 1
    elif direction == 'r' and char_x != SIZE_N-1:
        char_x += 1
    else:
        print('Reinput Direction. (u / d / l / r)') 
    turns += 1