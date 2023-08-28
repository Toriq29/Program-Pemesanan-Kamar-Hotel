import pickle
from user import User


def main():
    # Membuat array kosong dan membuat database_user.dat
    arr = []
    file_database = "database_user.dat"
    with open(file_database, 'wb') as data:
        pickle.dump(arr, data, pickle.HIGHEST_PROTOCOL)

    with open(file_database, 'rb') as data:
        database = pickle.load(data)

    # Membuat user default
    A = User("Thoriq", "toriq.mailbox@gmail.com", "123")

    # Menambahakan user default ke dalam database
    database.append(A)

    # Menyimpan file tersebut ke dalam database
    with open(file_database, 'wb') as data:
        pickle.dump(database, data, pickle.HIGHEST_PROTOCOL)


if __name__ == '__main__':
    main()
