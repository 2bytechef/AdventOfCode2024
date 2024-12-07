from collections import defaultdict

needle = ['X', 'M', 'A', 'S']
search_dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

with open("./Day6/input.txt", "r") as f:
    array = []
    for line in f:
        array.append(list(line.strip()))
        

i, j = 0, 0
dir = 'up'

for x, xar in enumerate(array):
    for y, val in enumerate(xar):
        if val == '^':
            i, j = x, y
            
# print(f"{i} - {j}")
pos = set()

            
def collision(x1, y1, array):
    if not (0 <= x1 < len(array)) or not (0 <= y1 < len(array[0])):
        return False
    if array[x1][y1] == '#':
        return True
    else:
        return False
            
sumsy = 0
while 0 <= i < len(array) and 0 <= j < len(array[0]):
    if dir == 'up':
        if collision(i - 1, j, array):
            dir = 'right'
            continue
        else:
            if (i, j) not in pos:
                sumsy += 1
            pos.add((i, j))
            i -= 1
    if dir == 'right':
        if collision(i, j + 1, array):
            dir = 'down'
            continue
        else:
            if (i, j) not in pos:
                sumsy += 1
            pos.add((i, j))
            j += 1
    if dir == 'down':
        if collision(i + 1, j, array):
            dir = 'left'
            continue
        else:
            if (i, j) not in pos:
                sumsy += 1
            pos.add((i, j))
            i += 1
    if dir == 'left':
        if collision(i, j - 1, array):
            dir = 'up'
            continue
        else:
            if (i, j) not in pos:
                sumsy += 1
            pos.add((i, j))
            j -= 1
            
print(sumsy)
        