n = input()
length = int(n)
result = [1,1]


if length == 1:
    print(result[0])
elif length == 2:
    print(result[1])
elif length > 2:
    for i in range(length - 2):
        tampung = result[i] + result[i+1]
        result.append(tampung)

print(result)