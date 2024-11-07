#~~~AUTO GATE TOL~~~#

''' 
Deskripsi : Sistem tol yang digunakan adalah sistem tol tertutup. Pengguna tidak perlu membayar ketika
tap e-Toll di gerbang masuk. Pengguna membayar tol di gerbang keluar, dengan tarif yang dihitung per kilometer 
dan golongan kendaraan yang dimiliki. 

Algoritma ini dibuat semirip mungkin dengan gerbang tol yang sebenarnya, yang bisa dilalui oleh banyak kendaraan.
Sehingga algoritma ini bisa menginput sebanyak mungkin data kendaraan yang masuk, dan menyimpan data tersebut 
agak kendaraan bisa keluar di gerbang keluar
'''
#~~~~~~~KAMUS~~~~~~~#
'''
id_eToll : array integer
in_gerbang_masuk : array string
in_gerbang_keluar : string
data_gerbang
golongan_kendaraan

*~~~Variabel Simpan~~~*
data_id_eToll
id_eToll
save_masuk
data_gerbang
km_gerbang
tarif_per_km
tarif_golongan

*~~Variabel Sementara~~*
km_masuk
km_keluar
saldo
golongan
count
indeks 
masui
keluar
status

*~~Variabel Bantu~~*


'''

#~~~~DATABASE~~~~#

data_gerbang = [ '0' for i in range (5) ]
km_gerbang = [ '0' for i in range (5) ]
tarif_golongan = [ 0 for i in range (6) ]

data_gerbang[0] = 'A'
data_gerbang[1] = 'B'
data_gerbang[2] = 'C'
data_gerbang[3] = 'D'
data_gerbang[4] = 'E'

km_gerbang[0] = 0
km_gerbang[1] = 70
km_gerbang[2] = 150
km_gerbang[3] = 200
km_gerbang[4] = 300

tarif_golongan[1] = 1
tarif_golongan[2] = 1.2
tarif_golongan[3] = 1.5
tarif_golongan[4] = 1.7
tarif_golongan[5] = 2

tarif_per_km = 700

#~~~~Initialize~~~~#

data_id_eToll = [0]
save_masuk = ['0']
saldo = 0
count = 0
indeks = 0
golongan = 0
total_harga = 0
lanjut = True

while (lanjut == True):
    status = input("Mau masuk/keluar tol? ")

    if(status == 'masuk'):
        #~~Gerbang Masuk~~#
        id_eToll = int(input("Masukkan 5 digit ID e-Toll : "))
        masuk = input("Dari gerbang mana? : ")
        cek = False
        i = 0

        while (i<=count and cek == False):
            if(data_id_eToll[i]== 0):
                data_id_eToll[i] = id_eToll
                save_masuk[i] = masuk
                cek = True
            i += 1
        if(cek == False):
            data_id_eToll.append(id_eToll)
            save_masuk.append(masuk)
            count += 1
        tanya = str(input("Mau lanjut/tidak? "))
        if(tanya == "tidak"):
            lanjut = False
            
    elif(status == 'keluar'):
        #~~Gerbang Keluar~~#
        id_eToll = int(input("Masukkan 5 digit ID e-Toll : "))
        i = 0
        cek = False
        while (i<=count and cek == False):
            if(data_id_eToll[i] == id_eToll):
                indeks = i
                saldo = int(input("Masukkan nominal saldo anda : "))
                keluar = input("Keluar di gerbang mana? : ")
                golongan = int(input("Masukkan golongan kendaraan : "))
                for j in range(5):
                    if(data_gerbang[j] == save_masuk[indeks]):
                        km_masuk = km_gerbang[j]
                        break
                for j in range(5):
                    if(data_gerbang[j] == keluar):
                        km_keluar = km_gerbang[j]
                        break
                cek = True
            i += 1    
            if(i>count and cek == False):
                print("Kartu tidak bisa digunakan")
                id_eToll = int(input("Masukkan 5 digit ID e-Toll : "))            
                i = 0
        total_harga = tarif_per_km * abs(km_keluar-km_masuk) * tarif_golongan[golongan]

        if(saldo < total_harga):
            while(saldo < total_harga):
                print("Saldo tidak mencukupi")
                print("Harga yang harus dibayar adalah: Rp" + str(total_harga))
                saldo = int(input("Masukkan nominal saldo baru: "))
        if(saldo >= total_harga):
            print("Silakan melanjutkan perjalanan :D")
            print("Sisa saldo anda Rp" + str(saldo - total_harga))
            #~~~~hapus data id dan gerbang yang tersimpan~~~~#
            data_id_eToll[indeks] = 0
            save_masuk[indeks] = '0'
        
        tanya = str(input("Mau lanjut/tidak? "))
        if(tanya == "tidak"):
            lanjut = False
