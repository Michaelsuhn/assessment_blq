n = input()
length = int(n)
result = [2,3,5,7]
p = 2
print('\n')

if length <= 4:
    for i in range(length):
        print(result[i])
else:
    for i in range(length-4):
        status = True
        while status:
            p += 1
            if (p % 2 != 0) and (p % 3 != 0) and (p % 5 != 0) and (p % 7 != 0):
                result.append(p)
                status = False

    print(result)