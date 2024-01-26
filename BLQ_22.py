'''
22.	Sederet lilin memiliki perbandingan laju meleleh mengikuti deret Fibonacci.
Diketahui deret Fibonacci adalah sebagai berikut:
1	1	2	3	5	8	13
Sehingga dapat dikatakan
-	Lilin 1 dan 2 meleleh sepanjang 1 per detik
-	Lilin ke-3 meleleh sepanjang 2 per detik
-	Lilin ke-6 meleleh sepanjang 8 per detik
-	Dan seterusnya…
Jika diberikan panjang lilin awal masing-masing adalah
3	3	9	6	7	8	23
Tentukan lilin mana yang paling pertama habis meleleh.

'''

fibo = [1,1,2,3,5,8,13]
deret = [3,3,9,6,7,8,23]
length = len(fibo)
result = []
record = 100


for i in range(length):
    result.append(deret[i] / fibo[i])
    if result[i] < record:
        record = result[i]

print(result)
print('Lilin mana yang paling pertama habis meleleh = lilin ke ' + str(result.index(record)+1))

