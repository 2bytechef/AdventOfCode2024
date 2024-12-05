import re

regexp = r"mul\(\d{1,3},\d{1,3}\)"
regexp_groups = r"mul\((\d{1,3}),(\d{1,3})\)"

sumsy = 0
with open("./Day3/input.txt", "r") as f:
    numsearch = re.findall(regexp, f.read())
    
    for group in numsearch:
        num0, num1 = re.search(regexp_groups, group).groups()
        sumsy += int(num0) * int(num1)
            
            # sumsy += 1
    # re.search(regexp, line)
print(sumsy)