
def difference(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        for char in str1:
            if char in str2:
                return char

# Character range function
def range_char(*args):
    return [chr(i) for a in args for i in range(ord(a[0]), ord(a[1])+1)]


# def init_priority_dict():
#     priority_dict = {}
#     start = 'a'

#     for i in range(1, 27):

#         priority_dict[] = i
#     for i in range(1, 27):
#         priority_dict[range_char('A')[i-1]] = i+26
#     return priority_dict

lowercase_chars_priority =  [ range_char('az'), list(range(1, 27))]
uppercase_chars_priority =  [ range_char('AZ'), list(range(27, 53))]

print(lowercase_chars_priority[1][1])


chars = []
points = []

def char_priority(lowercase_chars_priority, uppercase_chars_priority, char):
    if char in lowercase_chars_priority[0]:
        return (lowercase_chars_priority[1][lowercase_chars_priority[0].index(char)])
    else:
        return (uppercase_chars_priority[1][uppercase_chars_priority[0].index(char)])

def find_badge(line1,line2,line3):
    for char in line1:
        if char in line2 and char in line3:
            return char


with open('day3/input.txt', 'r') as f:
    lines = f.readlines()
    #group by 3 lines
    for line in zip(*[iter(lines)]*3):
        line1 = line[0].strip()
        line2 = line[1].strip()
        line3 = line[2].strip()
        #print(line1, line2, line3)
        diff = find_badge(line1, line2, line3)
        print("difference: ", diff) 
        chars.append(diff)
        points.append(char_priority(lowercase_chars_priority, uppercase_chars_priority, diff))

print("points ", sum(points))
