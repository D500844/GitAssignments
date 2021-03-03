#-------------------------#
# Title: Pickling and Error Handling
# Summ: Module Assignment07: Present a basic data log to pickle
# Dev: dBrady
# Date: March 1st, 2020
# ChangeLog: (who,what,when)
#  dBrady,3/1/2020, Added code
#-------------------------#

import pickle

with open("my_dictionary.pickle", "rb") as my_dictionary_file:
    pickled_list = pickle.load(my_dictionary_file)

input("Press Enter to Exit when you are done.")