'''
Input	                    Output
Susilo Bambang Yudhoyono	S***o B***g Y***o
Rani Tiara	                R***i T***a
'''


input = input()
words = input.split(' ')

for name in words:
    length = len(name)
    print(name[0] + '***' + name[length - 1])
