name_list = ["Evi", "Madeleine", "Dan", "Kelsey", "Cayden", "Hayley", "Darian"]
print(sorted(name_list))

user_name = input("What is your name?").strip().capitalize()

if user_name in name_list:
    print("WOW!! Your name is in my list of names!")
else:
    print("Sorry, {} is not in my list of names.".format(user_name))

repeat = True

while repeat == True:
    replace_or_add = input("Would you like to 'replace' a name in the list with your name OR would you like to just 'add' your name to the list?").strip().capitalize()
    if replace_or_add == "Replace":
        replacement_name = input("Type in a name that you want to replace it with: \n"
                                 "{}".format(name_list)).strip().capitalize()
        name_position = name_list.index(replacement_name)
        name_list[name_position] = user_name
        print("Here is the replaced list: {}".format(name_list))
        repeat = False
    elif replace_or_add == "Add":
        name_list.append(user_name)
        print("Here is the added list: {}".format(name_list))
        repeat = False
    else:
        print("Please type in either 'replace' OR 'add'.")




