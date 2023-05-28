s = input()
left_sign = [i for i in range(len(s)) if s[i] == "<"]
right_sign = [i for i in range(len(s)) if s[i] == ">"]

for pair in zip(left_sign, right_sign):
    start_index, last_index = pair
    substring = s[start_index : last_index + 1]
