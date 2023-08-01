SIZE_N = 5
SIZE_M = 5

char_x = 1
char_y = 1

world_map = ''

for j in range(SIZE_M):
    row = "|"
    for i in range(SIZE_N):

        if char_x == i and char_y == j:
            row += 'X|'
        else:
            row += ' |'
    
    world_map += f'{row}\n'
print(world_map)