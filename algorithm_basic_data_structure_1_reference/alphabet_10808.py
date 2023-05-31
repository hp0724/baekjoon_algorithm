alphabet = input()
alphabet_array = [0] * 26
for i in alphabet:
    if i == "a":
        alphabet_array[0] += 1
    elif i == "b":
        alphabet_array[1] += 1
    elif i == "c":
        alphabet_array[2] += 1
    elif i == "d":
        alphabet_array[3] += 1
    elif i == "e":
        alphabet_array[4] += 1
    elif i == "f":
        alphabet_array[5] += 1
    elif i == "g":
        alphabet_array[6] += 1
    elif i == "h":
        alphabet_array[7] += 1
    elif i == "i":
        alphabet_array[8] += 1
    elif i == "j":
        alphabet_array[9] += 1
    elif i == "k":
        alphabet_array[10] += 1
    elif i == "l":
        alphabet_array[11] += 1
    elif i == "m":
        alphabet_array[12] += 1
    elif i == "n":
        alphabet_array[13] += 1
    elif i == "o":
        alphabet_array[14] += 1
    elif i == "p":
        alphabet_array[15] += 1
    elif i == "q":
        alphabet_array[16] += 1
    elif i == "r":
        alphabet_array[17] += 1
    elif i == "s":
        alphabet_array[18] += 1
    elif i == "t":
        alphabet_array[19] += 1
    elif i == "u":
        alphabet_array[20] += 1
    elif i == "v":
        alphabet_array[21] += 1
    elif i == "w":
        alphabet_array[22] += 1
    elif i == "x":
        alphabet_array[23] += 1
    elif i == "y":
        alphabet_array[24] += 1
    elif i == "z":
        alphabet_array[25] += 1


print(" ".join(map(str, alphabet_array)))
