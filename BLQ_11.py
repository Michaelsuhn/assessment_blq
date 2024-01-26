'''11.	Input: Afrika
Output:
***a***
***k***
***i***
***r***
***f***
***A***
Input: Jeruk
Output:
**k**
**u**
**r**
**e**
**J** 
'''


input = input()
step = input.splitlines()
length = len(step[0])

for i in range(length):
    print('**' + step[0][length - 1 - i] + '**')