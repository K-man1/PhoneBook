def startMessage ():
    entry = input("""Your phonebook:
                  Please press:
                  1 ~ Display your existing contacts.
                  2 ~ Create a new contact.
                  3 ~ Find an existing contact.
                  4 ~ To delete an existing contact.
                  5 ~ Exit your phonebook.\n""")
    return entry
def phonebook ():
    
    contacts = {}
    while True:
        entry = startMessage()

#if statements!

        if entry == "1":
            if bool(contacts) == True:
                for name, number in contacts.items():
                    print(name,": ",number)
            else:
                print("You have no contacts")

        elif entry == "2":
            name = input("What is the name of the person you want to add?\n")
            number = input("What is "+name+"'s phone number?\n")
            if number not in contacts.items():
                contacts.update({name: number})
                print("Your contact has been saved. Here is your list:")
                for name, number in contacts.items():
                    print(name,": ",number)
            else:
                print("Hmm... that contact seems to already exist!")

        elif entry == "3":
            name = input("Enter name you would like to search.\n")
            if name in contacts:
                print(name + ": " + contacts[name])
            else:
                print("That contact does not exist.")
    
        elif entry == "4":
            name = input("Enter name you would like to delete.\n")
            if name in contacts:
                contacts.pop(name, None)
                for name, number in contacts.items():
                    print(name,": ",number)
            else:
                print("That contact does not exist.")
        
        elif entry == "5":
            print("Goodbye!")
            break
    
        else:
            print("That's not an option! Try again.")
phonebook()