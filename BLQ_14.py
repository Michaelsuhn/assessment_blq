'''14.	Deret: 3 9 0 7 1 2 4
N = 3	 7 1 2 4 3 9 0
N = 1	 9 0 7 1 2 4 1
'''


deret = '3 9 0 7 1 2 4'
angka = deret.split(' ')
n = 4
new = ''

for i in range(len(angka) - n):
   new = new + angka[i + n] + ' '

for i in range(n):
   new = new + angka[i] + ' '

print(new)