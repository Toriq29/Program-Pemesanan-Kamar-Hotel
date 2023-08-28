## Class Hotel
class Hotel:
    # Keterangan atribut pada class Hotel
    __nama_hotel: str
    __harga: int
    __keterangan_nomor_kamar = []

    # Atribut pada class Hotel
    def __init__(self, nama_hotel, harga):
        self.__nama_hotel = nama_hotel
        self.__harga = harga
        self.__keterangan_nomor_kamar = []

    # Getter atribut nama_hotel
    @property
    def nama_hotel(self):
        return self.__nama_hotel

    # Setter atribut nama_hotel
    @nama_hotel.setter
    def nama_hotel(self, value):
        self.__nama_hotel = value

    # Getter atribut harga
    @property
    def harga(self):
        return self.__harga

    # Setter atribut harga
    @harga.setter
    def harga(self, value):
        self.__harga = value

    # Method untuk insert ket. no kamar pada list
    def masukkan_keterangan_nomor_kamar(self, value):
        self.__keterangan_nomor_kamar.append(value)

    # Method untuk mengembalikan list keterangan_nomor_kamar
    def mengeluarkan_data_nomor_kamar(self):
        return self.__keterangan_nomor_kamar