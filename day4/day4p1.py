


def check_list(list1, list2):
    #check if list1 is within list2
    for i in range(len(list1)):
        if list1[i] not in list2:
            return False
    return True

count = 0

with open("day4\input.txt", "r") as f:
    for rline in f:
        line = rline.strip()
        data = line.split(",")
        first_range = data[0].split("-")
        second_range = data[1].split("-")
        range1 = list(range(int(first_range[0]),int(first_range[1])+1))
        range2 = list(range(int(second_range[0]),int(second_range[1])+1))
        # print(f"range1: {range1} , range2: {range2}")
        ret1 = check_list(range1, range2)
        ret2 = check_list(range2, range1)
        if ret1 or ret2:
            count += 1

print(count)
