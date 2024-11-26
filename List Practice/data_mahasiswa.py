print ("""
PENDATAAN MAHASISWA PRODI TI UINMA 2024
=======================================""")

data_mahasiswa = []

jumlah_mahasiswa = int(input("Masukan Jumlah Mahasiswa: "))
for i in range (jumlah_mahasiswa):
    print ("\nData Mahasiswa Ke-",i+1)
    nama    = input("Nama            : ")
    nim     = input("Nim             : ")
    prodi   = input("Program Studi   : ")
    
    data_mahasiswa.append([nama,nim,prodi])
    
print ("""
DATA MAHASISWA PRODI TI UINMA
=============================""")
for mahasiswa in data_mahasiswa :
    print ("\nNama            :", mahasiswa[0])
    print ("NIM             :", mahasiswa[1])
    print ("Program Studi   :", mahasiswa[2])
