import pickle
from user import User
from riwayar_transaksi import RiwayatTransaksi
from admin import Admin


def memesan_hotel(account, data_user):
    database_user = "database_user.dat"
    database_hotel = "database_hotel.dat"
    print("List Nama Hotel: ")
    # membuka database hotel
    with open(database_hotel, 'rb') as data:
        databasehotel = pickle.load(data)

    ihotel = 0
    # print hotel yang tersedia
    for data_hotel in databasehotel:
        print("------------------")
        print("Nama hotel: ", data_hotel.nama_hotel,
              " | Harga: ", data_hotel.harga)
        ihotel += 1
    print("------------------")

    # input memilih hotel
    askhotel = str(input("Pilih hotel: "))
    checkhotel = 0
    while (checkhotel < ihotel):
        for data_hotel in databasehotel:
            # jika hotel yang di input ada atau sesuai
            if (askhotel == data_hotel.nama_hotel):
                hotel = data_hotel
                checkhotel = ihotel + 1
                break
            else:
                checkhotel += 1

        # jika hotel yang di input tidak ada atau tidak sesuai
        if (checkhotel == ihotel):
            print(
                "Hotel yang anda masukkan tidak dapat diidentifikasi mohon masukkan ulang")
            askhotel = str(input("Pilih hotel: "))
            checkhotel = 0

    # jika wallet lebih banyak dari harga hotel
    if (account.wallet > hotel.harga):
        hotel_array = hotel.mengeluarkan_data_nomor_kamar()

        ikamar = 0
        # menghitung jumlah nomor kamar
        for data_kamar in hotel_array:
            ikamar += 1

        # print nomor kamar
        print("Kamar nomor 1 -", ikamar)

        # input nomor kamar
        asknomorkamar = int(input("Pilih nomor kamar: "))
        checkkamar = 0
        while (checkkamar < ikamar):
            for data_kamar in hotel.mengeluarkan_data_nomor_kamar():
                # jika input kamar ada atau sesua
                if (asknomorkamar == data_kamar.nomor_kamar):
                    nomor_kamar = data_kamar
                    checkkamar = ikamar + 1
                    break
                else:
                    checkkamar += 1

            # jika input kamar tidak ada atau tidak sesua
            if (checkkamar == ikamar):
                print(
                    "Nomor kamar yang anda masukkan tidak dapat diidentifikasi mohon masukkan ulang")
                print("Kamar nomor 1 -", ikamar)
                asknomorkamar = int(input("Pilih nomor kamar: "))
                checkkamar = 0
        # input bulan dan tanggal
        print("Contoh bulan: Januari")
        check_tanggal_bulan = False
        askbulan = str(input("Pilih bulan: "))
        asktanggal = int(input("Pilih tanggal: "))
        # mengecheck tanggal dan bulan
        while (check_tanggal_bulan == False):
            if (askbulan == "Januari" or askbulan == "Maret" or askbulan == "Mei" or askbulan == "Juli" or askbulan == "Agustus" or askbulan == "Oktober" or askbulan == "Desember"):
                if (0 < asktanggal < 32):
                    check_tanggal_bulan = True
                else:
                    print("Tanggal yang anda masukkan tidak dapat diidentifikasi")
            elif (askbulan == "Februari"):
                if (0 < asktanggal < 29):
                    check_tanggal_bulan = True
                else:
                    print("Tanggal yang anda masukkan tidak dapat diidentifikasi")
            elif (askbulan == "April" or askbulan == "Juni" or askbulan == "September" or askbulan == "November"):
                if (0 < asktanggal < 31):
                    check_tanggal_bulan = True
                else:
                    print("Tanggal yang anda masukkan tidak dapat diidentifikasi")
            else:
                print("Bulan yang anda masukkan tidak bisa diidentifikasi ")
            if (check_tanggal_bulan == False):
                print("Contoh bulan: Januari")
                askbulan = str(input("Pilih bulan: "))
                asktanggal = int(input("Pilih tanggal: "))

        tahunbulantanggal = nomor_kamar.mengeluarkan_data_tanggal()
        for data_tahunbulantanggal in tahunbulantanggal:
            # jika bulan input bulan ada atau sesuai
            if (askbulan == data_tahunbulantanggal.bulan):
                # jika input tanggal ada atau sesuai
                if (asktanggal == data_tahunbulantanggal.tanggal):
                    data_keterangan = data_tahunbulantanggal
                    # keterangan diganti nama akun yang membooking
                    break
        # jika keterangan adalah kosong
        if (data_keterangan.keterangan == "kosong"):
            data_keterangan.keterangan = account.name
            # wallet dikurang harga hotel
            account.wallet -= hotel.harga
            # menyimpan riwayat transaksi
            riwayat = RiwayatTransaksi(hotel.nama_hotel, nomor_kamar.nomor_kamar, data_tahunbulantanggal.tahun,
                                       data_tahunbulantanggal.bulan, data_tahunbulantanggal.tanggal)
            account.memasukkan_data_riwayat_transaksi(riwayat)
            print("Hotel sudah di booking")
            # menyimpan ke dalam database
            with open(database_user, 'wb') as data:
                pickle.dump(data_user, data, pickle.HIGHEST_PROTOCOL)
            with open(database_hotel, 'wb') as data:
                pickle.dump(databasehotel, data, pickle.HIGHEST_PROTOCOL)
        # jika keterangan tidak kosong
        else:
            print("Tanggal yang anda booking sudah tidak tersedia")

    # jika wallet kurang dari harga hotel
    else:
        print("Wallet yang anda punya tidak cukup untuk booking hotel ini")


def wallet(account, data_user):
    database_user = "database_user.dat"
    print("--Wallet--")
    print("1. Cek saldo")
    print("2. Top up")
    print("0. Keluar")
    # memilih pilihan wallet
    pil = int(input("Pilihan: "))
    while (pil != 0):
        # jika ingin melihat saldo
        if (pil == 1):
            print("Wallet: ", account.wallet)
        # jika ingin top up
        elif (pil == 2):
            uang = int(input("Masukkan nominal :"))
            account.wallet += uang
            with open(database_user, 'wb') as data:
                pickle.dump(data_user, data, pickle.HIGHEST_PROTOCOL)
        print("--Wallet--")
        print("1. Cek saldo")
        print("2. Top up")
        print("0. Keluar")
        # memilih pilihan wallet
        pil = int(input("Pilihan: "))


def editprofile(account, data_user):
    database_user = "database_user.dat"
    database_hotel = "database_hotel.dat"
    print("--Edit Profile--")
    print("1. Ganti Nama")
    print("2. Ganti Email")
    print("3. Ganti Password")
    print("0. Keluar")
    # memilih pilihan edit profile
    pilihan = int(input("Pilihan: "))
    while (pilihan != 0):
        # jika ingin mengganti nama
        if (pilihan == 1):
            print("--Ganti Nama--")
            namasebelum = account.name
            # input nama baru
            gantinama = str(input("Masukkan nama: "))
            account.name = gantinama

            # membuka database
            with open(database_hotel, 'rb') as data:
                data_hotel = pickle.load(data)

            # mencari database keterangan dengan nama sebelumnya dan mengganti dengan nama baru
            for datas in data_hotel:
                for nokar in datas.mengeluarkan_data_nomor_kamar():
                    for tanggall in nokar.mengeluarkan_data_tanggal():
                        if (tanggall.keterangan == namasebelum):
                            tanggall.keterangan = gantinama

            # menyimpan database
            with open(database_hotel, 'wb') as data:
                pickle.dump(data_hotel, data, pickle.HIGHEST_PROTOCOL)

        # jika ingin mengganti email
        elif (pilihan == 2):

            print("--Ganti Email--")
            gantiemail = str(input("Masukkan email: "))
            account.email = gantiemail

        # jika ingin mengganti password
        elif (pilihan == 3):
            print("--Ganti Password--")
            gantipass = str(input("Masukkan password: "))
            account.password = gantipass

        with open(database_user, 'wb') as data:
            pickle.dump(data_user, data, pickle.HIGHEST_PROTOCOL)

        print("--Edit Profile--")
        print("1. Ganti Nama")
        print("2. Ganti Email")
        print("3. Ganti Password")
        print("0. Keluar")
        pilihan = int(input("Pilihan: "))


def main():
    # export file database user dan hotel
    database_user = "database_user.dat"

    # pilihan dalam aplikasi
    print("1. Register")
    print("2. Login")
    print("3. admin")
    print("0. exit")
    choise = int(input("Pilihan: "))
    while (choise != 0):
        # jika memilih registrasi
        if (choise == 1):
            check = True
            while (check != False):

                # membuka database user
                with open(database_user, 'rb') as data:
                    data_user = pickle.load(data)
                # input nama, email, dan password
                name = str(input("Masukkan nama: "))
                email = str(input("Masukkan email: "))
                password = str(input("Masukkan password: "))

                account = User(name, email, password)
                # check apakah yang di input sudah ada di database atau tidak
                for databases in data_user:
                    if (account.email == databases.email):
                        check = True
                        print("Email sudah digunakan")
                        break
                    else:
                        check = False
                # jika tidak masuk masuk ke dalam main menu
                if (check == False):

                    # menyimpan database user
                    data_user.append(account)
                    with open(database_user, 'wb') as data:
                        pickle.dump(data_user, data, pickle.HIGHEST_PROTOCOL)
                    print("---------------------")
                    print("Selamat datang")
                    print("---------------------")
                    print("1. Memesan Hotel")
                    print("2. Wallet")
                    print("3. Edit Profile")
                    print("0. Log out")
                    x = int(input("Pilihan :"))
                    while (x != 0):
                        # jika ingin memesan hotel
                        if (x == 1):
                            memesan_hotel(account, data_user)
                        # jika ingin memasuki halaman wallet
                        elif (x == 2):
                            wallet(account, data_user)
                        # jika ingin  memasuki halaman edit profile
                        elif (x == 3):
                            editprofile(account, data_user)
                        print("---------------------")
                        print("Selamat datang")
                        print("---------------------")
                        print("1. Memesan Hotel")
                        print("2. Wallet")
                        print("3. Edit Profile")
                        print("0. Log out")
                        x = int(input("Pilihan :"))
        # jika memilih login
        elif (choise == 2):
            check_email = False
            pass_check = False
            # memasukkan email dan password
            while (check_email != True):
                email = str(input("Masukkan email: "))
                password = str(input("Masukkan password: "))

                # membuka database user
                with open(database_user, 'rb') as file:
                    data_user = pickle.load(file)

                # pengecekan email dan password apakah sudah ada atau tidak
                for data in data_user:
                    if (data.email == email):
                        check_email = True
                        if (data.password == password):
                            pass_check = True
                            account = data
                            break

                # jika email tidak terdaftar
                if (check_email == False):
                    print("Email tidak terdaftar")
                    ask = str(input("Ingin kembali ke menu? (ya/tidak): "))
                    if (ask == "ya"):
                        check_email = True
                        choise = 4

                # jika email terdaftar tetapi password salah
                elif (check_email == True and pass_check == False):
                    check_email = False
                    print("Password yang anda masukkan salah")

                # jika email dan password benar masuk ke main menu
                elif (check_email == True and pass_check == True):
                    print("---------------------")
                    print("Selamat datang")
                    print("---------------------")
                    print("1. Memesan Hotel")
                    print("2. Wallet")
                    print("3. Edit Profile")
                    print("0. Log out")
                    x = int(input("Pilihan :"))
                    while (x != 0):
                        # jika memilih memesan hotel
                        if (x == 1):
                            memesan_hotel(account, data_user)
                        # jika ingin memasuki halaman wallet
                        elif (x == 2):
                            wallet(account, data_user)
                        # jika ingin  memasuki halaman edit profile
                        elif (x == 3):
                            editprofile(account, data_user)
                        print("---------------------")
                        print("Selamat datang")
                        print("---------------------")
                        print("1. Memesan Hotel")
                        print("2. Wallet")
                        print("3. Edit Profile")
                        print("0. Log out")
                        x = int(input("Pilihan :"))

        elif (choise == 3):
            admin = Admin()
            # memasukan email password khusus untuk admin
            email = str(input("Masukkan email: "))
            password = str(input("Masukkan password: "))
            # jika email dan password benar
            if (email == "admin" and password == "admin123"):
                print("Home Page Admin")
                print("1. Database Account")
                print("2. Database Hotel")
                print("3. Menambah hotel")
                print("0. Keluar")
                # memasukan pilihan
                pilihan = int(input("Pilihan: "))
                while (pilihan != 0):
                    if (pilihan == 1):
                        # print data user
                        admin.print_data_user()
                    elif (pilihan == 2):
                        # print data hotel
                        admin.print_data_hotel()
                    elif (pilihan == 3):
                        # memasukan nama hotel dan harga lalu menyimpan ke database
                        nama_hotel = str(input("Masukkan nama hotel: "))
                        harga = int(input("Masukan harga: "))
                        admin.menambah_hotel(nama_hotel, harga)
                        print("Hotel sudah ditambahkan")
                    print("-----------")
                    print("Home Page Admin")
                    print("1. Database Account")
                    print("2. Database Hotel")
                    print("3. Menambah hotel")
                    print("0. Keluar")
                    # memasukan pilihan lagi
                    pilihan = int(input("Pilihan: "))
            else:
                print("Email admin dan Password admin yang anda masukkan salah")

        print("1. Register")
        print("2. Login")
        print("3. admin")
        print("0. exit")
        # memasukan pilihan lagi
        choise = int(input("Pilihan: "))


if __name__ == '__main__':
    main()
