# Class RiwayatTransaksi
class RiwayatTransaksi:
    # Keterangan atribut class RiwayatTransaksi
    __nama_hotel: str
    __nomor_kamar: int
    __tahun: str
    __bulan: str
    __tanggal: int

    # Atribut class RiwayatTransaksi
    def __init__(self, nama_hotel,nomor_kamar , tahun, bulan, tanggal):
        self.__nama_hotel = nama_hotel
        self.__nomor_kamar = nomor_kamar
        self.__tahun = tahun
        self.__bulan = bulan
        self.__tanggal = tanggal

    # Getter atribut nama_hotel
    @property
    def nama_hotel(self):
        return self.__nama_hotel

    # Setter atribut nama_hotel
    @nama_hotel.setter
    def nama_hotel(self, value):
        self.__nama_hotel = value

    # Getter atribut nomor_kamar
    @property
    def nomor_kamar(self):
        return self.__nomor_kamar

    # Setter atribut nomor_kamar
    @nomor_kamar.setter
    def nomor_kamar(self, value):
        self.__nomor_kamar = value

    # Getter atribut tahun
    @property
    def tahun(self):
        return self.__tahun

    # Setter atribut tahun
    @tahun.setter
    def tahun(self, value):
        self.__tahun = value

    # Getter atribut bulan
    @property
    def bulan(self):
        return self.__bulan

    # Setter atribut bulan
    @bulan.setter
    def bulan(self, value):
        self.__bulan = value

    # Getter atribut tanggal
    @property
    def tanggal(self):
        return self.__tanggal

    # Setter atribut tanggal
    @tanggal.setter
    def tanggal(self, value):
        self.__tanggal = value