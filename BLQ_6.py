n = input()
length = len(n)
sesudah = ''


for i in range(length):
    sesudah = sesudah + n[length-i-1]
print(sesudah)


if sesudah == n:
    print('Palindrome')
else:
    print('Bukan Palindrome')
