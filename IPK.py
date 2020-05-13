tot = 0 #point * sks
totn=0 #total nilai
ipk=0
jums=0 #jum sks
jumn=0 #jum nilai
nama = input("Nama Lengkap : ")
nim = input("NIM : ")
n = int(input("Jumlah Matakuliah Yang Diambil : "))
print("")
for i in range (n):
    print("Data ke - ",i) #data mulai dari 0->arrray dimulai dari 0
    mk = input("Masukan Nama Makul :")
    sks = int(input("Masukan SKS Makul :"))
    nil = int(input("Masukan Nilai : "))

    if (nil >= 85):
        p = "A"
        po = 4
    elif (nil >= 80):
        p = "AB"
        po = 3.5
    elif (nil >= 70):
        p = "B"
        po = 3
    elif (nil >= 65):
        p = "BC"
        po = 2.5
    elif (nil >= 60):
        p = "C"
        po = 2
    elif (nil >= 50):
        p = "D"
        po = 2
    else:
        p = "E"
        po = 1

    print("Prediat : ",p)
    tot = po*sks #point * sks
    print("Point : ",tot)
    print("")
    totn+=tot #total point A=4,B=3 dst dikalikan sks
    jumn+=nil #jumlah nilai
    jums+=sks #jumlah dari seluruh sks

print("-----------------------")
print("Nama Lengkap : ",nama)
print("NIM : ",nim)
print("Total Makul : ",n)
print("Total SKS : ",jums)
print("Total Nilai : ",jumn)
print("Total Point : ",totn)
ipk = totn/jums #jumlah dari point*sks dibagi jumlah dari seluruh sks
print("IPK : ",ipk)
print("-----------------------")

