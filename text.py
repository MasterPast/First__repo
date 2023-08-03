from random import randint, choice

SIZE_M = randint(5, 10)
SIZE_N = randint(5, 10)


def game_over(win, lose):
    x = False
    if win:
        print(f'You won in {turns} turns!!!!!!')
        x = True
    if lose:
        print(f'You lose in {turns} turns......')
        x = True
    return x


def generate_map(wm, x, y,
                 exx, exy, enx, eny,
                 chs, che, m=SIZE_M, n=SIZE_N):

    for j in range(m):
        row = '|'
        for i in range(n):
            if x == i and y == j:
                row += f'{chs}|'
            elif enx == i and eny == j:
                row += f'{che}|'
            elif exx == i and exy == j:
                row += '0|'
            else:
                row += ' |'

        wm += f'{row}\n'

    print()
    print(wm)

    return wm, enx, eny


def move(direction, x, y, m=SIZE_M, n=SIZE_N):

    if direction == 'u' and y != 0:
        y -= 1
    elif direction == 'd' and y != m - 1:
        y += 1
    elif direction == 'l' and x != 0:
        x -= 1
    elif direction == 'r' and x != n - 1:
        x += 1
    else:
        print('Reinput Direction. (u / d / l / r)')

    return x, y


char_x = randint(0, SIZE_N - 1)
char_y = randint(0, SIZE_M - 1)
char_sign = 'X'
win_condition = False
lose_condition = False
turns = 0
enemy_x = randint(0, SIZE_N-1)
enemy_y = randint(0, SIZE_M-1)
enemy_char_sign = 'E'
exit_x = randint(0, SIZE_N - 1)
exit_y = randint(0, SIZE_M - 1)


while True:
    world_map = ''
    win_condition = char_x == exit_x and char_y == exit_y
    lose_condition = char_x == enemy_x and char_y == enemy_y

    if win_condition:
        char_sign = 'W'

    if lose_condition:
        char_sign = '-'

    world_map = generate_map(world_map, char_x, char_y,
                             exit_x, exit_y, enemy_x, enemy_y,
                             char_sign, enemy_char_sign)

    if game_over(win_condition, lose_condition):
        break
    direction = input("Direction? (u / d / l / r)")
    char_x, char_y = move(direction, char_x, char_y)
    direction = choice('uldr')
    enemy_x, enemy_y = move(direction, enemy_x, enemy_y)

    

    turns += 1
