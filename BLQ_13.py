'''13.	Berapa derajat sudut terkecil yang dibentuk 2 jarum jam?
Jam 3:00  90
Jam 5:30  15
Jam 2.20  50
*detik tidak dipertimbangkan
'''


#derajat = int(360/12/5)
jam = 10
menit = 30

derajat_menit = int(menit * (30/5))
derajat_jam = int((jam * 30) + ((menit / 60) * 30))


if derajat_jam >= derajat_menit:
    sudut = derajat_jam - derajat_menit
elif derajat_menit >= derajat_jam:
    sudut = derajat_menit - derajat_jam

if sudut >= 180:
    sudut = 360 - sudut
print(sudut)