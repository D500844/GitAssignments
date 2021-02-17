# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# dBrady,2/16/2020,Added code to complete assignment 5, edited some existing variable names/comment locations.
# ------------------------------------------------------------------------ #

# -*- Data -*- #

# Declaring Variables
to_do = "F:\\_PythonClass\\Assignment05\\ToDoList.txt"   # An object that represents a file
strData = ""                                             # A row of text data from the file
dic_row = {}                                             # A row of data separated into elements of a dictionary {Task,Priority}
list_table = []                                          # A list that acts as a 'table' of rows
user_choice = None                                       # A Capture the user option selection
please_press = "\nPlease press Enter to Continue."       # A prompt to reduce code clutter

# -*- Processing -*- #

# Step 1 - When the program starts, we will load data from our file TodoList.
obj_file = open(to_do)
for row in obj_file:
    list_data = row.split(",")
    dic_row = {"Task": list_data[0], "Priority": list_data[1].strip()}
    list_table.append(dic_row)
obj_file.close()


# -*- Input/Output -*- #

# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item
    3) Remove an existing item
    4) Save data to file
    5) Exit program
    """)
    user_choice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()

    # Step 3 - Show the current items in the table
    if user_choice.strip() == '1':
        for row in list_table:
            print(row["Task"] + " | " + row["Priority"])
        input(please_press)
        continue

    # Step 4 - Add a new item to the list/Table
    elif user_choice.strip() == '2':
        input_task = input("Please Enter a task: ")
        input_priority = input("Please Enter a Priority: ")
        input_collection = {"Task": input_task, "Priority": input_priority}
        list_table.append(input_collection)
        input(please_press)
        continue

    # Step 5 - Remove an item from the list/Table based on its name
    elif user_choice.strip() == '3':
        removed_item = str(input("Please enter the Task you would like removed: "))
        table_range = len(list_table) - 1
        i = 0
        while i <= table_range:
            if removed_item in str(list(dict(list_table[i]).values())[0]):
                del list_table[i]
                print("Removed")
                break
            else:
                print("Task can not be found.")
                i = i + 1
        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif user_choice.strip() == '4':
        obj_file = open(to_do, "w")
        for row in list_table:
            obj_file.write(row["Task"] + "," + row["Priority"] + "\n")
            print("Saved")
            input(please_press)
        continue

    # Step 7 - Exit program
    elif user_choice.strip() == '5':
        print("Thank you, good luck with your Tasks.")
        break
