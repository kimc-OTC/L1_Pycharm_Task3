name_list = ["Evi", "Madeleine", "Dan", "Kelsey", "Cayden", "Hayley", "Darian"]
print(sorted(name_list))

user_name = input("What is your name?").strip().capitalize()

if user_name in name_list:
    print("WOW!! Your name is in my list of names!")
else:
    print("Sorry, {} is not in my list of names.".format(user_name))

replace_or_add = input("Would you like to replace a name in the list with your name OR would you like to just add your name into the list?").strip().capitalize()
if replace_or_add == "Replace":
    replaced_list = []
    print("Here is the replaced list: {}".format())
