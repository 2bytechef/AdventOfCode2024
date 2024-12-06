needle = 'A' # ['M', 'A', 'S']
others = ['M', 'S']
search_dirs = [((1, 1), (-1, -1)), ((1, -1), (-1, 1))]

with open("./Day4/input.txt", "r") as f:
    array = []
    for line in f:
        array.append(list(line.strip()))
        
# array = [
#     ['X', 'a', 'M', 'S', 'S', 'a', 'X', 'a', 'S', 'S'],
#     ['a', 'a', 'S', 'a', 'a', 'M', 'S', 'X', 'a', 'A'],
#     ['a', 'S', 'M', 'a', 'S', 'X', 'a', 'a', 'S', 'M'],
#     ['S', 'a', 'M', 'X', 'S', 'X', 'X', 'M', 'a', 'X'],
# ]
        
sumsy = 0
for i in range(len(array)):
    for j in range(len(array[i])):
        if array[i][j] == needle:
            found = True
            for (dx1, dy1), (dx2, dy2) in search_dirs:
                di, dj = i + dx1, j + dy1
                tofind = ['M', 'S']
                
                if 0 <= di < len(array) and 0 <= dj < len(array[i]) and array[di][dj] in tofind:
                    tofind.remove(array[di][dj])
                else:
                    found = False
                    break
                    
                di, dj = i + dx2, j + dy2
                
                if 0 <= di < len(array) and 0 <= dj < len(array[i]) and array[di][dj] in tofind:
                    continue
                else:
                    found = False
                    break
                
            if found:
                sumsy += 1
    
print(sumsy)
