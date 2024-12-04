import heapq
from collections import defaultdict

elf_group_1 = []
elf_group_2 = defaultdict(lambda: 0)

with open("./Day1/input.txt", "r") as f:
    for line in f:
        numbers = line.split()
        elf_group_1.append(int(numbers[0]))
        elf_group_2[int(numbers[1])] += 1
        
sums = 0

for num in elf_group_1:
    sums += num * elf_group_2[num]

print(sums)