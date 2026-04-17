def pangkat(A, B):
    if B == 0:
        return 1
    else:
        return A * pangkat(A, B - 1)

def deret(N):
    if N <= 0:
        return 0
    if N == 1:
        return 1
    elif N == 2:
        return 1 - 2/3
    else:
        return 0 

while True:
    print("Pilih Menu:")
    print("1. A pangkat B")
    print("2. Hitung 1-2/3+5/8-13/21+")
    print("0. Keluar")
    pilihan = input("Masukkan Pilihan Menu: ")

    if pilihan == '1':
        try:
            bilangan = int(input("Masukan suatu bilangan bulat: "))
            pangkat_val = int(input("Masukan pangkat yang diinginkan: "))
            hasil = pangkat(bilangan, pangkat_val)
            print(f"hasil {bilangan} pangkat {pangkat_val} adalah {hasil}")
        except ValueError:
            print("Masukan tidak valid")
    elif pilihan == '2':
        try:
            jumlah_n = int(input("Masukkan jumlah N: "))
            hasil_deret = deret(jumlah_n)
            print(hasil_deret)
        except ValueError:
            print("Masukan tidak valid")
    elif pilihan == '0':
        break
    else:
        print("Pilihan tidak valid")