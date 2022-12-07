with open("input.txt") as f:
    lines = f.readlines()
    max = 0
    sum = 0
    for line in lines:
        pline = line.strip()
        if (pline == ""):
            if int(sum) > max:
                max = int(sum)
            sum = 0
        else:
            sum += int(pline)
    print("Solution: ", max)
