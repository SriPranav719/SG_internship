my_dict = {}

while True:
    
    contacts_menu = ["----Menu----", "1. Show all contacts", "2. Add a contact", "3. search for a contact", "4. delete a contact", "5. Exit"]
    
    for choose in contacts_menu:
        print(choose)
        
    serial_num = input("Choose a number from the above menu :")
    
    if serial_num == "1":
        if my_dict == {}:
            
            print("No contacts are added !")
        
        else:
            print(my_dict)
            
            
    elif serial_num == "2":
        add_contact_name = (input("Enter the contact name :"))
        add_contact_number = int(input("Enter the phone number : "))
        
        if add_contact_name not in my_dict.keys():
            my_dict[add_contact_name] = add_contact_number
            print(my_dict)
        
        else:
            print("Contact already exists")
            
            
    elif serial_num == "3":
        search_contact = input("Enter the contact name :")
        
        for key, value in my_dict.items():
            
            if search_contact == key:
                
                print(my_dict[key]) 
                
            else:
                print("The contact do not exists")     
                
                
                
    elif serial_num == "4":
        
        delete_contact = input("Enter the contact name to remove the contact :")
        
        if delete_contact in my_dict:
            
            my_dict.pop(delete_contact)
            print(f"Contact '{delete_contact}' removed.")
            
        else:
            
            print(f"Contact not found.")
        
        
    elif serial_num == "5":
        break
    
    else:
        print("invalid input")
        
        break
