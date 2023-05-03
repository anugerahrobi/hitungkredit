

print("Selamat Datang di Sunindo Kookmin Best Finance")
print("Dengan saya Muhammad Anugerah Nurrobi, sebelumnya dengan Bapak siapa saya bicara?")
Nama = str(input("Nama : "))
Anggunan = str(input("Mau Kredit Apa Pak ? : "))
Total = int(input("Jumlah Total Kredit : "))
print("Mau DP berapa bapak ?")
Pinjaman = int(input("Jumlah Uang Muka : "))
Kurang =  (Total-Pinjaman)
Persen = (Kurang/Total*100)
print("Maka Uang DP Kreditnya adalah", Persen, "%")
print("Dengan Jangka Waktu 1 Tahun sampai dengan 5 Tahun, mau berapa tahun pak?")
Tahun = int(input("Janga Waktu Per Tahun : "))
print("12 Bulan, 24 Bulan, 36 Bulan, 48 Bulan, 60 Bulan")
print("Bunga Pinjaman tiap bulan adalah 2,77%")
Bunga = 0.0277
Bulan = int(input("Jangka Waktu Per Bulan : "))
Setoran = 0
if Bulan == 12:
        Bunga_bulan = (Kurang*Bunga*Tahun)/Bulan
        Setoran = Kurang/Bulan+Bunga_bulan
elif Bulan == 24:
        Bunga_bulan = (Kurang*Bunga*Tahun)/Bulan
        Setoran = Kurang/Bulan+Bunga_bulan
elif Bulan == 36:
        Bunga_bulan = (Kurang*Bunga*Tahun)/Bulan
        Setoran = Kurang/Bulan+Bunga_bulan
elif Bulan == 48:
        Bunga_bulan = (Kurang*Bunga*Tahun)/Bulan
        Setoran = Kurang/Bulan+Bunga_bulan
elif Bulan == 60:
        Bunga_bulan = (Kurang*Bunga*Tahun)/Bulan
        Setoran = Kurang/Bulan+Bunga_bulan
else:
        print("operator tak diketahui")
print("Setoran biaya per Bulan :", Setoran)
Bersedia = str(input("Apakah bersedia : "))
bersedia = "bersedia"
tidak = "tidak"
if Bersedia == "bersedia":
    bersedia=print('Jika', bersedia,'Data akan diproses, data dari Bapak', Nama, "dengan anggunan", Anggunan, 'pinjamanya', Pinjaman, 'Setoran perbulan nya adalah', Setoran, 'Saya bantu proses')
elif Bersedia== "tidak":
    tidak=print('Jika', tidak, 'Data tidak di proses, Terima kasih')
else:
        print("operator tak diketahui")

