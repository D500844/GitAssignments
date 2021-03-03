#-------------------------#
# Title: Pickling and Error Handling
# Summ: Module Assignment07: Demonstrate Try-Exception
# Dev: dBrady
# Date: March 1st, 2020
# ChangeLog: (who,what,when)
#  dBrady,3/1/2020, Added code
#-------------------------#

class PizzaTime:
    def __init__(self, pizza_in_the_oven):
        self.__pizza_in_the_oven = pizza_in_the_oven

    def digiornos(self):
        if self.__pizza_in_the_oven > 85: #minutes
            #print(Pizza is burnt)
            raise Exception
        elif self.__pizza_in_the_oven < 70:
            #print("Pizza is not ready")
            raise Exception
        else:
            print("It's Pizza Time")

slice = PizzaTime(99)
slice.digiornos()