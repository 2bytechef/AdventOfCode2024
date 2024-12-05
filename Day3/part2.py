import re

regexp = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)"
regexp_groups = r"mul\((\d{1,3}),(\d{1,3})\)"

sumsy = 0
with open("./Day3/input.txt", "r") as f:
    numsearch = re.findall(regexp, f.read())
    do = True
    
    for group in numsearch:
        if group == "do()":
            do = True
            continue
        elif group == "don't()":
            do = False
            continue
        
        if not do:
            continue
        num0, num1 = re.search(regexp_groups, group).groups()
        sumsy += int(num0) * int(num1)
            
            # sumsy += 1
    # re.search(regexp, line)
print(sumsy)