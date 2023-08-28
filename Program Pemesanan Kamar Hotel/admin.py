import pickle
from copy import deepcopy
from nomor_kamar import NomorKamar
from tahun_bulan_tanggal import TahunBulanTanggal
from hotel import Hotel
from admin_interface import AdminInterface

## Kelas Admin
class Admin(AdminInterface):
    ## Method untuk print data hotel
    def print_data_hotel(self):
        # Membuka database hotel
        database_hotel = "database_hotel.dat"
        with open(database_hotel, 'rb') as data:
                b = pickle.load(data)

        # Print data hotel dari database
        for datas in b:
            print("=======================================================")
            print("Nama Hotel: ", datas.nama_hotel)
            for nokar in datas.mengeluarkan_data_nomor_kamar():
                print("-------------------------------------------------------")
                print("Nomor kamar: ", nokar.nomor_kamar)
                for tanggall in nokar.mengeluarkan_data_tanggal():
                    if(tanggall.keterangan != "kosong"):
                        print("Tahun: ", tanggall.tahun, " | Bulan: ", tanggall.bulan, " | Tanggal :", tanggall.tanggal, " | Keterangan: ", tanggall.keterangan)

    ## Method untuk print data hotel
    def print_data_user(self):
        # Membuka database user
        database_user = "database_user.dat"
        with open(database_user, 'rb') as file:
                a = pickle.load(file)

        # Print data user dari database
        for user in a:
            print("-----------")
            print("nama : ", user.name)
            print("email : ", user.email)
            print("password : ", user.password)
            print("wallet : ", user.wallet)
            print("Riwayat transaksi: ")
            # Jika riwayat transaksi kosong
            if(user.mengeluarkan_data_riwayat_transaksi() == []):
                print("tidak ada riwayat transaksi")
            # Jika riwayat transaksi tidak kosong
            else:
                for i in user.mengeluarkan_data_riwayat_transaksi():
                    print("Nama Hotel: ", i.nama_hotel," | Nomor kamar: ", i.nomor_kamar, " | Tahun: ", i.tahun, " | Bulan: ", i.bulan, " | Tanggal :", i.tanggal)
            print("-----------")

    def menambah_hotel(self, nama_hotel, harga):
            # Membuat 5 nomor kamar
            a = NomorKamar(1)
            b = NomorKamar(2)
            c = NomorKamar(3)
            d = NomorKamar(4)
            e = NomorKamar(5)
            # Memasukan keterangan tanggal kosong untuk kamar di bulan Januari
            for i in range(1,32):
                tanggal = TahunBulanTanggal("2023" ,"Januari", i, "kosong")
                a.masukkan_keterangan_tanggal(deepcopy(tanggal))
                b.masukkan_keterangan_tanggal(deepcopy(tanggal))
                c.masukkan_keterangan_tanggal(deepcopy(tanggal))
                d.masukkan_keterangan_tanggal(deepcopy(tanggal))
                e.masukkan_keterangan_tanggal(deepcopy(tanggal))
            # Memasukan keterangan tanggal kosong untuk kamar di bulan Februari
            for i in range(1,29):
                tanggal = TahunBulanTanggal("2023" ,"Februari", i, "kosong")
                a.masukkan_keterangan_tanggal(deepcopy(tanggal))
                b.masukkan_keterangan_tanggal(deepcopy(tanggal))
                c.masukkan_keterangan_tanggal(deepcopy(tanggal))
                d.masukkan_keterangan_tanggal(deepcopy(tanggal))
                e.masukkan_keterangan_tanggal(deepcopy(tanggal))
            # Memasukan keterangan tanggal kosong untuk kamar di bulan Maret
            for i in range(1,32):
                tanggal = TahunBulanTanggal("2023" ,"Maret", i, "kosong")
                a.masukkan_keterangan_tanggal(deepcopy(tanggal))
                b.masukkan_keterangan_tanggal(deepcopy(tanggal))
                c.masukkan_keterangan_tanggal(deepcopy(tanggal))
                d.masukkan_keterangan_tanggal(deepcopy(tanggal))
                e.masukkan_keterangan_tanggal(deepcopy(tanggal))
            # Memasukan keterangan tanggal kosong untuk kamar di bulan April
            for i in range(1,31):
                tanggal = TahunBulanTanggal("2023" ,"April", i, "kosong")
                a.masukkan_keterangan_tanggal(deepcopy(tanggal))
                b.masukkan_keterangan_tanggal(deepcopy(tanggal))
                c.masukkan_keterangan_tanggal(deepcopy(tanggal))
                d.masukkan_keterangan_tanggal(deepcopy(tanggal))
                e.masukkan_keterangan_tanggal(deepcopy(tanggal))
            # Memasukan keterangan tanggal kosong untuk kamar di bulan Mei
            for i in range(1,32):
                tanggal = TahunBulanTanggal("2023" ,"Mei", i, "kosong")
                a.masukkan_keterangan_tanggal(deepcopy(tanggal))
                b.masukkan_keterangan_tanggal(deepcopy(tanggal))
                c.masukkan_keterangan_tanggal(deepcopy(tanggal))
                d.masukkan_keterangan_tanggal(deepcopy(tanggal))
                e.masukkan_keterangan_tanggal(deepcopy(tanggal))
            # Memasukan keterangan tanggal kosong untuk kamar di bulan Juni
            for i in range(1,31):
                tanggal = TahunBulanTanggal("2023" ,"Juni", i, "kosong")
                a.masukkan_keterangan_tanggal(deepcopy(tanggal))
                b.masukkan_keterangan_tanggal(deepcopy(tanggal))
                c.masukkan_keterangan_tanggal(deepcopy(tanggal))
                d.masukkan_keterangan_tanggal(deepcopy(tanggal))
                e.masukkan_keterangan_tanggal(deepcopy(tanggal))
            # Memasukan keterangan tanggal kosong untuk kamar di bulan Juli
            for i in range(1,32):
                tanggal = TahunBulanTanggal("2023" ,"Juli", i, "kosong")
                a.masukkan_keterangan_tanggal(deepcopy(tanggal))
                b.masukkan_keterangan_tanggal(deepcopy(tanggal))
                c.masukkan_keterangan_tanggal(deepcopy(tanggal))
                d.masukkan_keterangan_tanggal(deepcopy(tanggal))
                e.masukkan_keterangan_tanggal(deepcopy(tanggal))
            # Memasukan keterangan tanggal kosong untuk kamar di bulan Agustus
            for i in range(1,32):
                tanggal = TahunBulanTanggal("2023" ,"Agustus", i, "kosong")
                a.masukkan_keterangan_tanggal(deepcopy(tanggal))
                b.masukkan_keterangan_tanggal(deepcopy(tanggal))
                c.masukkan_keterangan_tanggal(deepcopy(tanggal))
                d.masukkan_keterangan_tanggal(deepcopy(tanggal))
                e.masukkan_keterangan_tanggal(deepcopy(tanggal))
            # Memasukan keterangan tanggal kosong untuk kamar di bulan September
            for i in range(1,31):
                tanggal = TahunBulanTanggal("2023" ,"September", i, "kosong")
                a.masukkan_keterangan_tanggal(deepcopy(tanggal))
                b.masukkan_keterangan_tanggal(deepcopy(tanggal))
                c.masukkan_keterangan_tanggal(deepcopy(tanggal))
                d.masukkan_keterangan_tanggal(deepcopy(tanggal))
                e.masukkan_keterangan_tanggal(deepcopy(tanggal))
            # Memasukan keterangan tanggal kosong untuk kamar di bulan Oktober
            for i in range(1,32):
                tanggal = TahunBulanTanggal("2023" ,"Oktober", i, "kosong")
                a.masukkan_keterangan_tanggal(deepcopy(tanggal))
                b.masukkan_keterangan_tanggal(deepcopy(tanggal))
                c.masukkan_keterangan_tanggal(deepcopy(tanggal))
                d.masukkan_keterangan_tanggal(deepcopy(tanggal))
                e.masukkan_keterangan_tanggal(deepcopy(tanggal))
            # Memasukan keterangan tanggal kosong untuk kamar di bulan November
            for i in range(1,31):
                tanggal = TahunBulanTanggal("2023" ,"November", i, "kosong")
                a.masukkan_keterangan_tanggal(deepcopy(tanggal))
                b.masukkan_keterangan_tanggal(deepcopy(tanggal))
                c.masukkan_keterangan_tanggal(deepcopy(tanggal))
                d.masukkan_keterangan_tanggal(deepcopy(tanggal))
                e.masukkan_keterangan_tanggal(deepcopy(tanggal))
            # Memasukan keterangan tanggal kosong untuk kamar di bulan Desember
            for i in range(1,32):
                tanggal = TahunBulanTanggal("2023" ,"Desember", i, "kosong")
                a.masukkan_keterangan_tanggal(deepcopy(tanggal))
                b.masukkan_keterangan_tanggal(deepcopy(tanggal))
                c.masukkan_keterangan_tanggal(deepcopy(tanggal))
                d.masukkan_keterangan_tanggal(deepcopy(tanggal))
                e.masukkan_keterangan_tanggal(deepcopy(tanggal))
            # Membuat hotel serta harga kamar
            hotel = Hotel(nama_hotel, harga)
            # Memasukan keterangan nomor kamar dalam hotel
            hotel.masukkan_keterangan_nomor_kamar(deepcopy(a))
            hotel.masukkan_keterangan_nomor_kamar(deepcopy(b))
            hotel.masukkan_keterangan_nomor_kamar(deepcopy(c))
            hotel.masukkan_keterangan_nomor_kamar(deepcopy(d))
            hotel.masukkan_keterangan_nomor_kamar(deepcopy(e))

            database_hotel = "database_hotel.dat"
            # Menambahkan hotel ke dalam database
            with open(database_hotel, 'rb') as data:
                database = pickle.load(data)
                database.append(deepcopy(hotel))

            with open(database_hotel, 'wb') as data:
                pickle.dump(database, data, pickle.HIGHEST_PROTOCOL)