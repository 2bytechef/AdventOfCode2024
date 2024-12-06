needle = ['X', 'M', 'A', 'S']
search_dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

with open("./Day4/input.txt", "r") as f:
    array = []
    for line in f:
        array.append(list(line.strip()))
        
# array = [
#     ['X', 'A', 'A', 'S', 'A', 'A', 'X', 'A', 'S', 'S'],
#     ['A', 'A', 'S', 'A', 'A', 'M', 'S', 'X', 'A', 'A'],
#     ['A', 'S', 'M', 'A', 'S', 'X', 'A', 'A', 'S', 'M'],
#     ['S', 'A', 'M', 'X', 'S', 'X', 'X', 'M', 'A', 'X'],
# ]
        
sumsy = 0
for i in range(len(array)):
    for j in range(len(array[i])):
        if array[i][j] == needle[0]:
            for dx, dy in search_dirs:
                found = True
                di, dj = i, j
                for noodle in needle[1:]:
                    di, dj = di + dx, dj + dy
                    if 0 <= di < len(array) and 0 <= dj < len(array[i]):
                        if array[di][dj] != noodle:
                            found = False
                            break
                    else:
                        found = False
                        break
                
                if found:
                    sumsy += 1
    # else:
    #     continue
    # break
    
print(sumsy)
