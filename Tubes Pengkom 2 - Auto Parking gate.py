#~~~ AUTO GATE PARKIR ~~~#
import math

slot_mobil = 200
slot_motor = 300

arr_slot_motor = [0 for i in range (3)]
arr_slot_mobil = [0 for i in range (6)]

arr_slot_motor[1] = 100 #basement
arr_slot_motor[2] = 200 #luar

arr_slot_mobil[1] = 25 #basement
arr_slot_mobil[2] = 50 #lantai 1
arr_slot_mobil[3] = 50 #lantai 2
arr_slot_mobil[4] = 50 #lantai 3
arr_slot_mobil[5] = 25 #luar

tarif_motor = 2000
tarif_mobil = 4000

revenue_motor = 0
revenue_mobil = 0
total_motor = 0
total_mobil = 0

ID = [[0 for i in range (3)] for j in range (3000)]

print(" ===============SELAMAT DATANG===============")

def stat_harian():
    print("==============JUMLAH KENDARAAN===============\n1. Motor : " + str(total_motor) + "\n2. Mobil : " + str(total_mobil))
    print("==============JUMLAH PENDAPATAN==============\n1. Motor : " + str(revenue_motor) + "\n2. Mobil : " + str(revenue_mobil))
    print("   Total : Rp" + str(revenue_mobil + revenue_motor))

def ubah_slot_motor (n, tempat):
    global arr_slot_motor

    if(tempat == 1):
        arr_slot_motor[1] += n
    elif(tempat == 2):
        arr_slot_motor[2] += n

def ubah_slot_mobil (n, tempat):
    global arr_slot_mobil

    if(tempat == 1):
        arr_slot_mobil[1] += n
    elif(tempat == 2):
        arr_slot_mobil[2] += n
    elif(tempat == 3):
        arr_slot_mobil[3] += n
    elif(tempat == 4):
        arr_slot_mobil[4] += n
    elif(tempat == 4):
        arr_slot_mobil[4] += n

def motor_masuk():
    global ID
    cek = False
    i = 1000
    if(sum(arr_slot_motor) > 0):
        print("Tempat parkir yang tersedia \n1. Basement : " + str(arr_slot_motor[1]) + "\n2. Luar : " + str(arr_slot_motor[2]))
        tempat = int(input("Pilih tempat parkir : "))
        waktu_masuk = float(input("Waktu masuk : "))
        ubah_slot_motor(-1, tempat)

        while(i<1300 and cek == False):
            if(ID[i][1] == 0):
                ID[i][1] = waktu_masuk
                ID[i][2] = tempat
                print("=============================================")
                print("\nID parkir anda : " + str(i))
                cek = True
            i += 1
        print("Silakan masuk")
    else:
        print("\nParkir motor tidak tersedia! Silakan pulang.")
        
def mobil_masuk():
    global ID
    cek = False
    i = 1500
    if(sum(arr_slot_mobil) > 0):
        print("Tempat parkir yang tersedia\n1. Basement : " + str(arr_slot_mobil[1]) + "\n2. Lantai_1 : " + str(arr_slot_mobil[2]))
        print("3. Lantai_2 : " + str(arr_slot_mobil[3]) + "\n4. Lantai_3 : " + str(arr_slot_mobil[4]) + "\n5. Luar : " + str(arr_slot_mobil[5]))
        tempat = int(input("Pilih tempat parkir : "))
        waktu_masuk = float(input("Waktu masuk : "))
        ubah_slot_mobil(-1, tempat)

        while(i<1700 and cek == False):
            if(ID[i][1] == 0):
                ID[i][1] = waktu_masuk
                ID[i][2] = tempat
                print("=============================================")
                print("\nID parkir anda : " + str(i))
                cek = True
            i += 1
        print("Silakan masuk")  
    else:
        print("\nParkir mobil tidak tersedia! Silakan pulang.")            

def mobil_keluar(n):
    global ID, revenue_mobil, total_mobil
    waktu_keluar = float(input("Waktu keluar : "))
    saldo = int(input("Masukkan nominal saldo anda : Rp"))
    total_harga = math.ceil(waktu_keluar-ID[n][1]) * tarif_mobil

    if(saldo < total_harga):
        while(saldo < total_harga): 
            #jika saldo tidak mencukupi, pengendara harus top up saldo terlebih dahulu, sehingga akan diinput saldo baru
            print("Saldo tidak mencukupi.")
            print("Harga yang harus dibayar adalah: Rp" + str(total_harga))
            saldo = int(input("Masukkan nominal saldo baru : Rp"))
    if(saldo >= total_harga):
        print("=============================================")
        print("\nHati-hati di jalan!")
        print("Sisa saldo anda Rp" + str(saldo - total_harga))

    revenue_mobil += total_harga
    total_mobil += 1
    ID[n][1] = 0
    ubah_slot_mobil (1, ID[n][2])
    ID[n][2] = '0'

def motor_keluar(n):
    global ID, revenue_motor, total_motor
    waktu_keluar = float(input("Waktu keluar : "))
    saldo = int(input("Masukkan nominal saldo anda : Rp"))
    total_harga = math.ceil(waktu_keluar-ID[n][1]) * tarif_motor

    if(saldo < total_harga):
        while(saldo < total_harga): 
            #jika saldo tidak mencukupi, pengendara harus top up saldo terlebih dahulu, sehingga akan diinput saldo baru
            print("Saldo tidak mencukupi.")
            print("Harga yang harus dibayar adalah: Rp" + str(total_harga))
            saldo = int(input("Masukkan nominal saldo baru : Rp"))
    if(saldo >= total_harga):
        print("=============================================")
        print("\nHati-hati di jalan!")
        print("Sisa saldo anda Rp" + str(saldo - total_harga))

    revenue_motor += total_harga
    total_motor += 1
    ID[n][1] = 0
    ubah_slot_motor (1, ID[n][2])
    ID[n][2] = '0'
    
status = True
pilih = '0'
while(status == True):
    masukkeluar = input("Masuk atau Keluar? ")
    motormobil = int(input("Pilih jenis kendaraan \n1. Motor \n2. Mobil \n"))

    if (masukkeluar == "Masuk"):
        if (motormobil == 1):
            motor_masuk()
            pilih = input("\nLanjut atau Tidak? ")
            if(pilih == "Tidak"):
                status = False
        elif(motormobil == 2):
            mobil_masuk()
            pilih = input("\nLanjut atau Tidak? ")
            if(pilih == "Tidak"):
                status = False

    elif (masukkeluar == "Keluar"):
        ID_sementara = int(input("Masukkan ID parkir : "))
        if (motormobil == 1):
            motor_keluar(ID_sementara)
            pilih = input("\nLanjut atau Tidak? ")
            if(pilih == "Tidak"):
                status = False
        elif(motormobil == 2):
            mobil_keluar(ID_sementara)
            pilih = input("\nLanjut atau Tidak? ")
            if(pilih == "Tidak"):
                status = False

pilih = input("Ingin melihat data statistik harian? ")
if(pilih == "Ya"):
    pilih = input("Masukkan kode admin : ")
    if(pilih == "A12345"):
        stat_harian()
    else:
        print("Kode salah")

print("===============PROGRAM SELESAI===============")
