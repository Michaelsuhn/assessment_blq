'''15.	Ubah format waktu "03:40:44 PM" menjadi format 24 jam (15:40:44)'''




sample = '09:20:54 PM'
time = sample.split(' ')
time24h = time[0].split(':')


if time[1] == 'PM':
    time24h[0] = str(int(time24h[0]) + 12)

new = time24h[0] + ':' + time24h[1] + ':' + time24h[2]
print(new)