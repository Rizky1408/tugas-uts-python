#list
import math
list_no = 0
list_nama = []
list_nilai = []
total = 0
grade = []

#input nama dan nilai
print("="*40)
print("="*39)
batas = 5
for n in range(batas):
    list_nama.append(input("Masukkan nama  : "))
    list_nilai.append(int(input("Masukkan nilai : ")))
    print()
    jml = n + 1
    total += list_nilai[n]
    rata = total / jml
    if list_nilai[n] >= 60:
        grade.append('lulus')
    else:
        grade.append('tidak lulus')

#output
print("--------------------------------------------")
print("No      Nama             Nilai   Keterangan")
print("--------------------------------------------")
for i in range(batas):
    list_no += 1
    print(list_no,"\t",list_nama[i],"\t\t",list_nilai[i],"\t",grade[i])
print("---------------------------------------")
print("Jumlah Mahasiswa =",jml)
print("Rata-rata        =",rata)
print("Nilai tertinggi  =",max(list_nilai))
print("Nilai tertinggi  =",min(list_nilai))






# bilangan = []

# banyak = int(input("Masukan banyak bilangan :"))

# for i in range(banyak):
#     masukan = int(input("Masukan bilangan :"))
#     bilangan.append(masukan)
 
# print("\nbilangan genap :")    
# for i in bilangan:
#     if i % 2 == 0:
#         print(i)



# bilangan = []
# maksimal = []

# banyak = int(input("Masukan banyak bilangan :"))

# for i in range(banyak):
#     masukan = int(input("Masukan bilangan :"))
#     bilangan.append(masukan)
    
# max_number = max(bilangan)
# print("max number :", max_number)

# bilangan = []

# banyak = int(input("Masukan :"))

# for i in range(banyak):
#     masukan = int(input("masukan bilangan :"))
#     bilangan.append(masukan)
    
# for i in bilangan:
#     if i % 2 == 0:
#         print("genap :", i)
    
#     if i > 0 :
#         print("bilangan positif :",i)
        
#     if i % 2 == 1 and i % 3 == 0:
#         print(i)
    
#     if i % 3 == 1 or i % 3 == 2:
#         print(i)

#     if i % 5 == 0:
#         print(i)

