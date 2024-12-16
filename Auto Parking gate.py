#~~~ AUTO GATE PARKIR ~~~#
import math

# motor atau mobil
# sub motor atau mobil
# cek slot
# jam masuk, simpan, dpt id motor/mobil
# parkir luar atau dalam
# cek slot, tampilkan slot kosong untuk parkiran dalam (basement-lantai 3)
# parkiran dalam motor hanya di basement
# pilih tempat
# kurangi slot, simpan lantai

# keluar, masukkan id, dpt jam dan lantai
# masukkan jam keluar (v sementara)
# hitung nominal
# masukkan saldo
# tampilkan sisa saldo
# hapus data jam dan lantai, slot lantai +1, id bisa dipakai selanjutnya

slot_mobil = 200
slot_motor = 300

basement_mobil = 25
basement_motor = 100
lantai1 = 50
lantai2 = 50
lantai3 = 50
luar_mobil = 25
luar_motor = 200

tarif_motor = 2000
tarif_mobil = 4000

waktu = 0

ID = [[0 for i in range (3)] for j in range (3000)]

def ubah_slot_motor (n, tempat, bm, lm):
    if(tempat == "Basement"):
        basement_motor = bm + n
    elif(tempat == "Luar"):
        luar_motor = lm + n


def ubah_slot_mobil (n, tempat):
    if(tempat == "Basement"):
        basement_mobil = basement_mobil + n
    elif(tempat == "Luar"):
        luar_mobil = luar_mobil + n
    elif(tempat == "Lantai_1"):
        lantai1 = lantai1 + n
    elif(tempat == "Lantai_2"):
        lantai2 = lantai2 + n
    elif(tempat == "Lantai_3"):
        lantai3 = lantai3 + n

def motor_masuk():
    cek = False
    i = 1000
    if(luar_motor + basement_motor > 0):
        print("Tempat parkir yang tersedia : \n1. Basement : " + str(basement_motor) + "\n2. Luar : " + str(luar_motor))
        tempat = input("Tempat parkir : ")
        waktu_masuk = float(input("Waktu masuk : "))
        ubah_slot_motor(-1, tempat, basement_motor, luar_motor)

        while(i<1300 and cek == False):
            if(ID[i][1] == 0):
                ID[i][1] == waktu_masuk
                ID[i][2] == tempat
                print("ID parkir anda : " + str(i))
                cek = True
            i += 1
        print("Silakan masuk")

    else:
        print("Parkir motor tidak tersedia! Silakan pulang.")
        
def mobil_masuk():
    cek = False
    i = 1500
    if(luar_mobil + basement_mobil + lantai1 + lantai2 + lantai3 > 0):
        print("Tempat parkir yang tersedia : \n1. Basement : " + str(basement_mobil) + "\n2. Lantai_1 : " + str(lantai1) + "\n3. Lantai_2 : " + str(lantai2) + "\n4. Lantai_3 : " + str(lantai3) + "\n5. Luar : " + str(luar_mobil))
        tempat = input("Tempat parkir : ")
        waktu_masuk = float(input("Waktu masuk : "))
        ubah_slot_mobil(-1, tempat)

        while(i<1700 and cek == False):
            if(ID[i][1] == 0):
                ID[i][1] == waktu_masuk
                ID[i][2] == tempat
                print("ID parkir anda : " + str(i))
                cek = True
            i += 1
        print("Silakan masuk")
        
    else:
        print("Parkir mobil tidak tersedia! Silakan pulang.")            

def mobil_keluar(n):
    waktu_keluar = float(input("Waktu keluar : "))
    saldo = int(input("Masukkan nominal saldo anda : "))
    total_harga = math.ceil(waktu_keluar-ID[n][1]) * tarif_mobil

    if(saldo < total_harga):
        while(saldo < total_harga): 
            #jika saldo tidak mencukupi, pengendara harus top up saldo terlebih dahulu, sehingga akan diinput saldo baru
            print("Saldo tidak mencukupi")
            print("Harga yang harus dibayar adalah: Rp" + str(total_harga))
            saldo = int(input("Masukkan nominal saldo baru: "))
    if(saldo >= total_harga):
        print("Silakan melanjutkan perjalanan :D")
        print("Sisa saldo anda Rp" + str(saldo - total_harga))
    ID[n][1] = 0
    ubah_slot_motor (1, ID[n][2])
    ID[n][2] = '0'

def motor_keluar(n):
    waktu_keluar = float(input("Waktu keluar : "))
    saldo = int(input("Masukkan nominal saldo anda : "))
    total_harga = math.ceil(waktu_keluar-ID[n][1]) * tarif_motor

    if(saldo < total_harga):
        while(saldo < total_harga): 
            #jika saldo tidak mencukupi, pengendara harus top up saldo terlebih dahulu, sehingga akan diinput saldo baru
            print("Saldo tidak mencukupi")
            print("Harga yang harus dibayar adalah: Rp" + str(total_harga))
            saldo = int(input("Masukkan nominal saldo baru: "))
    if(saldo >= total_harga):
        print("Silakan melanjutkan perjalanan :D")
        print("Sisa saldo anda Rp" + str(saldo - total_harga))
    ID[n][1] = 0
    ubah_slot_motor (1, ID[n][2])
    ID[n][2] = '0'
    

masukkeluar = input("Masuk atau Keluar? ")
motormobil = input("Motor atau Mobil? ")

if (masukkeluar == "Masuk"):
    if (motormobil == "Motor"):
        motor_masuk()
    elif(motormobil == "Mobil"):
        mobil_masuk()

elif (masukkeluar == "Keluar"):
    ID_sementara = int(input("Masukkan ID parkir : "))
    if (motormobil == "Motor"):
        motor_keluar(ID_sementara)
    elif(motormobil == "Mobil"):
        mobil_keluar(ID_sementara)


print(luar_motor, basement_motor)
