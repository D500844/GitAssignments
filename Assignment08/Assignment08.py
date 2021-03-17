# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# dBrady,2.22.2021,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []


class Product(object):
    def __init__(self, name, price):
        self.product_name = name
        self.product_price = price

    def info(self):
        return self.product_name, self.product_price


# Processing  ------------------------------------------------------------- #
class FileProcessor:
    pass

    # TODO: Add Code to process data from a file
    @staticmethod
    def ReadFileDataToString(file_name: str, lstOfProductObjects):
        """ reads data from file"""
        #        lstOfProductObjects = []
        try:
            f = open(file_name, 'r')
            for line in f:
                name, price = line.split(",")
                row = {"name": name.strip(), "price": price.strip()}
                lstOfProductObjects.append(row)
            f.close()
        except Exception as e:
            print("A general error occured.")
        return lstOfProductObjects

    @staticmethod
    def WriteDataToFile(file_name, lstOfProductObjects):
        """ save data to file
        :param file_name:
        :param list_objects:
        :return:
        """
        f = open(file_name, 'w')
        for row in lstOfProductObjects:
            f.write(row["name"] + ', ' + row["price"] + '\n')
        f.close()


# Presentation (Input/Output)  -------------------------------------------- #
class IO(object):
    @staticmethod
    def print_menu_Products():
        print('''
        (1) Add a new Product
        (2) Save Data to File        
        (3) Exit Program
        ''')

    @staticmethod
    def input_menu_choice():
        choice = str(input("Enter your selection: ")).strip()
        return choice

    @staticmethod
    def show_data(lstOfProductObjects):
        """ Displays data"""
        for row in lstOfProductObjects:
            print(row["name"] + " (" + row["price"] + ")")

    @staticmethod
    def input_data():
        item = str(input("Item name:  ")).strip()
        price = str(input("Item price: ")).strip()
        return item, price


# Main Body of Script  ---------------------------------------------------- #

f = FileProcessor()
lstOfProductObjects = f.ReadFileDataToString(strFileName, lstOfProductObjects)
IO.show_data(lstOfProductObjects)  # Show current data in the list/table

while (True):
    IO.print_menu_Products()
    choice = IO.input_menu_choice()
    if str(choice) == "1":
        name, price = IO.input_data()
        row = {"name": name, "price": price}
        lstOfProductObjects.append(row)
        IO.show_data(lstOfProductObjects)
        continue  # to show the menu
    elif str(choice) == "2":
        f.WriteDataToFile(strFileName, lstOfProductObjects)
    elif str(choice) == "3":
        input("\nPress Enter to Exit: ")
        break
