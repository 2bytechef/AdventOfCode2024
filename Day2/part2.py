
goodns = 0
with open("./Day2/input.txt", "r") as f:
    for line in f:
        pn = None
        las = None
        good = 1
        fail = 1
        
        for i in line.split():
            i = int(i)
            
            if las is None:
                las = i
                continue
            
            if pn is None:
                if i > las:
                    pn = 1
                elif i < las:
                    pn = -1
                else:
                    if fail == 1:
                        fail = 0
                        continue
                    else:
                        good = 0
                        break
            
            if pn == 1:
                if i <= las or i - las > 3:
                    if fail == 1:
                        fail = 0
                    else:
                        good = 0
                        break
                    
            elif pn == -1:
                if i >= las or las - i > 3:
                    if fail == 1:
                        fail = 0
                    else:
                        good = 0
                        break
                
            las = i
        
        goodns += good
        
print(goodns)
            