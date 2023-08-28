import pickle

# Class User

class User:
    # Keterangan atribut pada class User
    __name: str
    __email: str
    __password: str
    __wallet: int
    __data_riwayat_transaksi = []

    # Atribut pada class User
    def __init__(self, name, email, password):
        self.__name = name
        self.__email = email
        self.__password = password
        self.__wallet = 0
        self.__data_riwayat_transaksi = []

    # Getter atribut name
    @property
    def name(self):
        return self.__name

    # Setter atribut name
    @name.setter
    def name(self, value):
        self.__name = value

    # Getter atribut email
    @property
    def email(self):
        return self.__email

    # Setter atribut email
    @email.setter
    def email(self, value):
        self.__email = value

    # Getter atribut password
    @property
    def password(self):
        return self.__password

    # Setter atribut password
    @password.setter
    def password(self, value):
        self.__password = value

    # Getter atribut wallet
    @property
    def wallet(self):
        return self.__wallet

    # Setter atribut wallet
    @wallet.setter
    def wallet(self, value):
        self.__wallet = value

    # Method untuk insert data riwayat transaksi pada list
    def memasukkan_data_riwayat_transaksi(self, value):
        self.__data_riwayat_transaksi.append(value)

    # Method untuk mengembalikan list data riwayat transaksi
    def mengeluarkan_data_riwayat_transaksi(self):
        return self.__data_riwayat_transaksi
