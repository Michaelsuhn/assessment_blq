"""Hattori sedang berlatih untuk menjadi ninja yang baik dengan berlari melewati gunung dan lembah. Yang didefinisikan sebagai gunung dan lembah adalah:
-	Gunung: urutan Naik dan Turun yang bermula di 0 mdpl dan berakhir di 0 mdpl
-	Lembah: urutan Turun dan Naik yang bermula di 0 mdpl dan berakhir di 0 mdpl
Hattori mencatat perjalanannya dengan simbol N saat ia menanjak dan T saat ia turun dalam sebuah urutan seperti berikut
N N T N N N T T T T T N T T T N T N
Berapa Gunung dan Lembah yang sudah dilewati Hattori? """



rute = "N N T N N N T T T T T N T T T N T N"
steps = rute.split(' ')
counter = 0
save = 0
result = []

for sign in steps:
    if sign == 'N':
        counter += 1
    elif sign == 'T':
        counter -= 1
    print(counter,end=' ')

    if counter == 0 and save > 0:
        result.append('Gunung')
    elif counter == 0 and save < 0:
        result.append('Lembah')

    save = counter

print()
print(result)