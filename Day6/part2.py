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
pos = defaultdict(lambda: set())
sop = set()

            
def collision(x1, y1, array):
    if not (0 <= x1 < len(array)) or not (0 <= y1 < len(array[0])):
        return None
    if array[x1][y1] == '#':
        return True
    else:
        return False
            

#..#....
#......#
#.#.....
#..^....
dirs = ['up', 'right', 'down', 'left']
nxdir = {dirs[0]: dirs[1], dirs[1]: dirs[2], dirs[2]: dirs[3], dirs[3]: dirs[0]}
def dds(x, y, dire):
    if dire == 'up':
        return x-1, y
    if dire == 'right':
        return x, y+1
    if dire == 'down':
        return x+1, y
    if dire == 'left':
        return x, y-1
            
sumsy = 0
while 0 <= i < len(array) and 0 <= j < len(array[0]):
    pos[(i, j)].add(dir)
    di, dj = dds(i, j, dir)
    
    res = collision(di, dj, array)
    if res:
        dir = nxdir[dir]
        continue
    elif res is None:
        break
    
    if len(pos[di, dj]) == 0:
        i1, j1 = dds(i, j, nxdir[dir])
        while 0 <= i1 < len(array) and 0 <= j1 < len(array[i1]) and array[i1][j1] != '#':
            i1, j1 = dds(i1, j1, nxdir[dir])
            if nxdir[dir] in pos[(i, j)]:
                sop.add((di, dj))

    i, j = di, dj
            
print(len(sop))
        