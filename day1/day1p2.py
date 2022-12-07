with open("input.txt") as f:
    groups = []
    group = 0
    for line in f:
        pline = line.strip()
        if (pline == ""):
            groups.append(group)
            group = 0
        else:
            group += int(pline)
    groups.append(group)
    top3 = sorted(groups, reverse=True)[:3]
    print("Top 3: ", top3)
    print("Solution: ", sum(top3))
