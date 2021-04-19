# print alphabetically sorted name list
name_list = ["Evi", "Madeleine", "Dan", "Kelsey", "Cayden", "Hayley", "Darian"]
print(sorted(name_list))

# ask the user for their name
user_name = input("What is your name?").strip().capitalize()

# if the user's name is in the name list, print line 10 else, print line 12
if user_name in name_list:
    print("WOW!! Your name is in my list of names!")
else:
    print("Sorry, {} is not in my list of names.".format(user_name))

repeat = True

# while repeat is True, ask the user whether if they want to replace a name in the list with their name or simply just add it to the list
while True:
    replace_or_add = input("Would you like to 'replace' a name in the list with your name OR would you like to just 'add' your name to the list?").strip().capitalize()
    # if the user types in "Replace", ask for a name that they want to replace it with
    if replace_or_add == "Replace":
        replacement_name = input("Type in a name that you want to replace it with: \n"
                                 "{}".format(name_list)).strip().capitalize()
        # find the position of the replacement_name then replace the selected name with the user's name
        name_position = name_list.index(replacement_name)
        name_list[name_position] = user_name
        # print the replaced list and set repeat to False(finishes the while loop)
        print("Here is the replaced list: {}".format(name_list))
        repeat = False
    # if the user types in "Add", add the user's to the list
    elif replace_or_add == "Add":
        name_list.append(user_name)
        # print the added list and set repeat to False(finishes the while loop)
        print("Here is the added list: {}".format(name_list))
        repeat = False
    # if the user types in something else, continuously ask the user to type in either "Replace" or "Add"
    else:
        print("Please type in either 'replace' OR 'add'.")




