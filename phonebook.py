hasQuit = False
phonebook ={}

#Created a multi line string to input menu for project
menu = """
    Electronic Phone Book
    =====================
    1. Look up an entry
    2. Set an entry
    3. Delete an entry
    4. List all entries
    5. Quit
    """
while not(hasQuit):
    print(menu)

    #Created a folder for user to select an option
    selected_option = input ("What do you want to do (1-5)?")

    #print(selected_option)

    #Created a folder for contact name and phone number
    if selected_option == "2":
        name = input("What is the contact's name")
        phone_number = input("What is their phone number")
        phonebook[name] = phone_number
        print("Contact added SUCCESSFULLY!")
    #Created a look up entry folder that allow the user too look up entry, set and entry and quite
    elif selected_option == "1":
            name = input("What contact's number would you like")
            if phonebook.get (name) == None:
                print("there's no contact with that name... please try again") 
    else:
            print("Here's their number",phonebook[name])
    if selected_option == "5":
        hasQuit = True
    #Created a delet option to the phone book
    elif selected_option == "3":
        name = input("select what contact you would like to remove")
        if phonebook.get(name) != None:
            del phonebook [name]
            print("This contact will be removed")
        else:
            print("There not a contact with that name")


    

