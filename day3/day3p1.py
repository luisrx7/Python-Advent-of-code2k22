
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

with open('day3/input.txt', 'r') as f:
    for rline in f:
        line = rline.strip()
        lenght = len(line)
        half_length = int(lenght/2)
        #print(line[:half_length], line[half_length:])
        diff = difference(line[:half_length], line[half_length:])
        print("difference: ", diff) 
        chars.append(diff)
        if diff in lowercase_chars_priority[0]:
            points.append(lowercase_chars_priority[1][lowercase_chars_priority[0].index(diff)])
        else:# diff in uppercase_chars_priority[0]:
            points.append(uppercase_chars_priority[1][uppercase_chars_priority[0].index(diff)])

print("points ", sum(points))
    