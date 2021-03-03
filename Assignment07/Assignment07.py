#-------------------------#
# Title: Pickling and Error Handling
# Summ: Module Assignment07: Present a basic data log to pickle
# Dev: dBrady
# Date: March 1st, 2020
# ChangeLog: (who,what,when)
#  dBrady,3/1/2020, Added code
#-------------------------#

import pickle

my_dictionary = {
    "name" : "Dave",
    "Age" : 33,
    "Gender" : "manBearPig"
}

with open("my_dictionary.pickle", "wb") as my_dictionary_file:
    pickle.dump(my_dictionary, my_dictionary_file, pickle.HIGHEST_PROTOCOL)


input("Press Enter to Exit when you are done.")

