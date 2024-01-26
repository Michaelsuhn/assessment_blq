'''
7.	Tentukan mean, median, dan modus dari deret berikut. Jika ada lebih dari 2 modus, ambil angka yang nilainya paling kecil
8 7 0 2 7 1 7 6 3 0 7 1 3 4 6 1 6 4 3

'''

data = '8 7 0 2 7 1 7 6 3 0 7 1 3 4 6 1 6 4 3'
splits = data.split(' ')
length = len(splits)


#mean
sum = 0
for i in range(length):
    sum += int(splits[i])
mean = sum / length
print('Mean = ' + str(mean))


#median
for i in range(length):
    for j in range(length):
        if splits[i] < splits[j]:
            tampung = splits[i]
            splits[i] = splits[j]
            splits[j] = tampung

if length % 2 == 1:
    median = int((length / 2) + 1)
    print('Median = ' + splits[median])
elif length % 2 == 0:
    median1 = int((length / 2))
    median2 = int((length / 2) + 1)
    print('Median = ' + (splits[median1] + splits[median2]) / 2)


#modus
mylist = list( dict.fromkeys(splits) )
for i in mylist:    
    a = splits.count(str(i))
    print('Jumlah angka ' + str(i) + ' = ' + str(a))