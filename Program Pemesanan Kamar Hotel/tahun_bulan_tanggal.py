# Class TahunBulanTanggal
class TahunBulanTanggal:
    # Keterangan atribut class TahunBulanTanggal
    __tahun: str
    __bulan: str
    __tanggal: int
    __keterangan: str

    # Atribut class TahunBulanTanggal
    def __init__(self,tahun , bulan, tanggal, keterangan):
        self.__tahun = tahun
        self.__bulan = bulan
        self.__tanggal = tanggal
        self.__keterangan = keterangan

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

    # getter atribut tanggal
    @property
    def tanggal(self):
        return self.__tanggal

    # Setter atribut tanggal
    @tanggal.setter
    def tanggal(self, value):
        self.__tanggal = value

    # Getter atribut keterangan
    @property
    def keterangan(self):
        return self.__keterangan

    # Setter atribut keterangan
    @keterangan.setter
    def keterangan(self, value):
        self.__keterangan = value

