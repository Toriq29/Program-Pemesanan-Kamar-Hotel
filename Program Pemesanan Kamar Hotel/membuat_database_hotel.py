import pickle
from copy import deepcopy
from user import User
from tahun_bulan_tanggal import TahunBulanTanggal
from nomor_kamar import NomorKamar
from hotel import Hotel


def main():
    # Membuat array kosong dan membuat database_hotel.dat
    arr = []
    database_hotel = "database_hotel.dat"
    with open(database_hotel, 'wb') as data:
        pickle.dump(arr, data, pickle.HIGHEST_PROTOCOL)

    # Membuat 5 nomor kamar
    a = NomorKamar(1)
    b = NomorKamar(2)
    c = NomorKamar(3)
    d = NomorKamar(4)
    e = NomorKamar(5)

    # Memasukan keterangan tanggal kosong untuk kamar di bulan Januari
    for i in range(1, 32):
        tanggal = TahunBulanTanggal("2023", "Januari", i, "kosong")
        a.masukkan_keterangan_tanggal(deepcopy(tanggal))
        b.masukkan_keterangan_tanggal(deepcopy(tanggal))
        c.masukkan_keterangan_tanggal(deepcopy(tanggal))
        d.masukkan_keterangan_tanggal(deepcopy(tanggal))
        e.masukkan_keterangan_tanggal(deepcopy(tanggal))

    # Memasukan keterangan tanggal kosong untuk kamar di bulan Februari
    for i in range(1, 29):
        tanggal = TahunBulanTanggal("2023", "Februari", i, "kosong")
        a.masukkan_keterangan_tanggal(deepcopy(tanggal))
        b.masukkan_keterangan_tanggal(deepcopy(tanggal))
        c.masukkan_keterangan_tanggal(deepcopy(tanggal))
        d.masukkan_keterangan_tanggal(deepcopy(tanggal))
        e.masukkan_keterangan_tanggal(deepcopy(tanggal))

    # Memasukan keterangan tanggal kosong untuk kamar di bulan Maret
    for i in range(1, 32):
        tanggal = TahunBulanTanggal("2023", "Maret", i, "kosong")
        a.masukkan_keterangan_tanggal(deepcopy(tanggal))
        b.masukkan_keterangan_tanggal(deepcopy(tanggal))
        c.masukkan_keterangan_tanggal(deepcopy(tanggal))
        d.masukkan_keterangan_tanggal(deepcopy(tanggal))
        e.masukkan_keterangan_tanggal(deepcopy(tanggal))

    # Memasukan keterangan tanggal kosong untuk kamar di bulan April
    for i in range(1, 31):
        tanggal = TahunBulanTanggal("2023", "April", i, "kosong")
        a.masukkan_keterangan_tanggal(deepcopy(tanggal))
        b.masukkan_keterangan_tanggal(deepcopy(tanggal))
        c.masukkan_keterangan_tanggal(deepcopy(tanggal))
        d.masukkan_keterangan_tanggal(deepcopy(tanggal))
        e.masukkan_keterangan_tanggal(deepcopy(tanggal))

    # Memasukan keterangan tanggal kosong untuk kamar di bulan Mei
    for i in range(1, 32):
        tanggal = TahunBulanTanggal("2023", "Mei", i, "kosong")
        a.masukkan_keterangan_tanggal(deepcopy(tanggal))
        b.masukkan_keterangan_tanggal(deepcopy(tanggal))
        c.masukkan_keterangan_tanggal(deepcopy(tanggal))
        d.masukkan_keterangan_tanggal(deepcopy(tanggal))
        e.masukkan_keterangan_tanggal(deepcopy(tanggal))

    # Memasukan keterangan tanggal kosong untuk kamar di bulan Juni
    for i in range(1, 31):
        tanggal = TahunBulanTanggal("2023", "Juni", i, "kosong")
        a.masukkan_keterangan_tanggal(deepcopy(tanggal))
        b.masukkan_keterangan_tanggal(deepcopy(tanggal))
        c.masukkan_keterangan_tanggal(deepcopy(tanggal))
        d.masukkan_keterangan_tanggal(deepcopy(tanggal))
        e.masukkan_keterangan_tanggal(deepcopy(tanggal))

    # Memasukan keterangan tanggal kosong untuk kamar di bulan Juli
    for i in range(1, 32):
        tanggal = TahunBulanTanggal("2023", "Juli", i, "kosong")
        a.masukkan_keterangan_tanggal(deepcopy(tanggal))
        b.masukkan_keterangan_tanggal(deepcopy(tanggal))
        c.masukkan_keterangan_tanggal(deepcopy(tanggal))
        d.masukkan_keterangan_tanggal(deepcopy(tanggal))
        e.masukkan_keterangan_tanggal(deepcopy(tanggal))

    # Memasukan keterangan tanggal kosong untuk kamar di bulan Agustus
    for i in range(1, 32):
        tanggal = TahunBulanTanggal("2023", "Agustus", i, "kosong")
        a.masukkan_keterangan_tanggal(deepcopy(tanggal))
        b.masukkan_keterangan_tanggal(deepcopy(tanggal))
        c.masukkan_keterangan_tanggal(deepcopy(tanggal))
        d.masukkan_keterangan_tanggal(deepcopy(tanggal))
        e.masukkan_keterangan_tanggal(deepcopy(tanggal))

    # Memasukan keterangan tanggal kosong untuk kamar di bulan September
    for i in range(1, 31):
        tanggal = TahunBulanTanggal("2023", "September", i, "kosong")
        a.masukkan_keterangan_tanggal(deepcopy(tanggal))
        b.masukkan_keterangan_tanggal(deepcopy(tanggal))
        c.masukkan_keterangan_tanggal(deepcopy(tanggal))
        d.masukkan_keterangan_tanggal(deepcopy(tanggal))
        e.masukkan_keterangan_tanggal(deepcopy(tanggal))

    # Memasukan keterangan tanggal kosong untuk kamar di bulan Oktober
    for i in range(1, 32):
        tanggal = TahunBulanTanggal("2023", "Oktober", i, "kosong")
        a.masukkan_keterangan_tanggal(deepcopy(tanggal))
        b.masukkan_keterangan_tanggal(deepcopy(tanggal))
        c.masukkan_keterangan_tanggal(deepcopy(tanggal))
        d.masukkan_keterangan_tanggal(deepcopy(tanggal))
        e.masukkan_keterangan_tanggal(deepcopy(tanggal))

    # Memasukan keterangan tanggal kosong untuk kamar di bulan November
    for i in range(1, 31):
        tanggal = TahunBulanTanggal("2023", "November", i, "kosong")
        a.masukkan_keterangan_tanggal(deepcopy(tanggal))
        b.masukkan_keterangan_tanggal(deepcopy(tanggal))
        c.masukkan_keterangan_tanggal(deepcopy(tanggal))
        d.masukkan_keterangan_tanggal(deepcopy(tanggal))
        e.masukkan_keterangan_tanggal(deepcopy(tanggal))

    # Memasukan keterangan tanggal kosong untuk kamar di bulan Desember
    for i in range(1, 32):
        tanggal = TahunBulanTanggal("2023", "Desember", i, "kosong")
        a.masukkan_keterangan_tanggal(deepcopy(tanggal))
        b.masukkan_keterangan_tanggal(deepcopy(tanggal))
        c.masukkan_keterangan_tanggal(deepcopy(tanggal))
        d.masukkan_keterangan_tanggal(deepcopy(tanggal))
        e.masukkan_keterangan_tanggal(deepcopy(tanggal))

    # Membuat 5 macam hotel (default)
    hotelA = Hotel("Pullman", 2000000)
    hotelB = Hotel("InterContinental", 1900000)
    hotelC = Hotel("Hilton", 1100000)
    hotelD = Hotel("The Trans", 1700000)
    hotelE = Hotel("Sheraton", 1750000)

    # Memasukan keterangan nomor kamar untuk hotel A
    hotelA.masukkan_keterangan_nomor_kamar(deepcopy(a))
    hotelA.masukkan_keterangan_nomor_kamar(deepcopy(b))
    hotelA.masukkan_keterangan_nomor_kamar(deepcopy(c))
    hotelA.masukkan_keterangan_nomor_kamar(deepcopy(d))
    hotelA.masukkan_keterangan_nomor_kamar(deepcopy(e))

    # Memasukan keterangan nomor kamar untuk hotel B
    hotelB.masukkan_keterangan_nomor_kamar(deepcopy(a))
    hotelB.masukkan_keterangan_nomor_kamar(deepcopy(b))
    hotelB.masukkan_keterangan_nomor_kamar(deepcopy(c))
    hotelB.masukkan_keterangan_nomor_kamar(deepcopy(d))
    hotelB.masukkan_keterangan_nomor_kamar(deepcopy(e))

    # Memasukan keterangan nomor kamar untuk hotel C
    hotelC.masukkan_keterangan_nomor_kamar(deepcopy(a))
    hotelC.masukkan_keterangan_nomor_kamar(deepcopy(b))
    hotelC.masukkan_keterangan_nomor_kamar(deepcopy(c))
    hotelC.masukkan_keterangan_nomor_kamar(deepcopy(d))
    hotelC.masukkan_keterangan_nomor_kamar(deepcopy(e))

    # Memasukan keterangan nomor kamar untuk hotel D
    hotelD.masukkan_keterangan_nomor_kamar(deepcopy(a))
    hotelD.masukkan_keterangan_nomor_kamar(deepcopy(b))
    hotelD.masukkan_keterangan_nomor_kamar(deepcopy(c))
    hotelD.masukkan_keterangan_nomor_kamar(deepcopy(d))
    hotelD.masukkan_keterangan_nomor_kamar(deepcopy(e))

    # Memasukan keterangan nomor kamar untuk hotel E
    hotelE.masukkan_keterangan_nomor_kamar(deepcopy(a))
    hotelE.masukkan_keterangan_nomor_kamar(deepcopy(b))
    hotelE.masukkan_keterangan_nomor_kamar(deepcopy(c))
    hotelE.masukkan_keterangan_nomor_kamar(deepcopy(d))
    hotelE.masukkan_keterangan_nomor_kamar(deepcopy(e))

    # Membaca database_hotel.dat kemudian menambahkan 5 macam hotel default tersebut ke dalam database
    database_hotel = "database_hotel.dat"
    with open(database_hotel, 'rb') as data:
        database = pickle.load(data)
        database.append(deepcopy(hotelA))
        database.append(deepcopy(hotelB))
        database.append(deepcopy(hotelC))
        database.append(deepcopy(hotelD))
        database.append(deepcopy(hotelE))

    with open(database_hotel, 'wb') as data:
        pickle.dump(database, data, pickle.HIGHEST_PROTOCOL)


if __name__ == '__main__':
    main()
