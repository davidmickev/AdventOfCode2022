chars = []
count = 0
with open("input6.txt")as input6:
    for input in input6:
        for ch in input:
            if len(chars) < 4:
                count+=1
                chars.append(ch)
            elif len(chars) == 4:
                if (chars[0] != chars[1] and chars[1] != chars[2] and chars[2] != chars[3] and chars[0] != chars[3] and chars[1] != chars[3] and chars[0] != chars[2]):
                    print(count)
                    print(chars)
                    break
                else:
                    del chars[0]
                    chars.append(ch)
                    count+=1
                    #print(count)

# chars = ['a','b','c','d']
# del chars[0]
# print(chars)