from abc import abstractmethod

# Class interface untuk method pada admin


class AdminInterface:

    # abstract method untuk print data hotel
    @abstractmethod
    def print_data_hotel(self):
        pass

    # abstract method untuk print data user
    @abstractmethod
    def print_data_user(self):
        pass
