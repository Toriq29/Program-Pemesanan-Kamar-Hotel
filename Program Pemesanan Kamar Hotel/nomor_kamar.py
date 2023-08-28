# Class NomorKamar
class NomorKamar:
    # Keterangan atribut class NomorKamar
    __nomor_kamar: int
    __keterangan_tanggal = []

    # Atribut class NomorKamar
    def __init__(self, nomor_kamar):
        self.__nomor_kamar = nomor_kamar
        self.__keterangan_tanggal = []

    # Getter atribut nomor_kamar
    @property
    def nomor_kamar(self):
        return self.__nomor_kamar

    # Setter atribut nomor_kamar
    @nomor_kamar.setter
    def nomor_kamar(self, value):
        self.__nomor_kamar = value

    # Method untuk insert keterangan tanggal pada list
    def masukkan_keterangan_tanggal(self, value):
        self.__keterangan_tanggal.append(value)

    # Method untuk mengembalikan list keterangan tanggal
    def mengeluarkan_data_tanggal(self):
        return self.__keterangan_tanggal