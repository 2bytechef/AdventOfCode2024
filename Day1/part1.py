import heapq

elf_group_1 = []
elf_group_2 = []

with open("./Day1/input.txt", "r") as f:
    for line in f:
        numbers = line.split()
        heapq.heappush(elf_group_1, int(numbers[0]))
        heapq.heappush(elf_group_2, int(numbers[1]))
        
sum = 0

while len(elf_group_1) > 0:
    sum += abs(heapq.heappop(elf_group_1) - heapq.heappop(elf_group_2))

print(sum)