data = '1 2 1 3 4 7 1 1 5 6 1 8'
splits = data.split(' ')
length = len(splits)

for i in range(length):
    for j in range(length):
        if splits[i] < splits[j]:
            tampung = splits[i]
            splits[i] = splits[j]
            splits[j] = tampung

print(splits)