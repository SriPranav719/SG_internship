def process():

    while True:
        
        print("1. Read the journal")
        print("2. Write the journal")
        print("3. Exit")

        choice = input("Choose an option (1, 2, 3): ")

        if choice == "1":
            
            def read():
                try:
                    with open("my_file.txt","r") as file:
            
                        read_journal = file.read()
                        print("----Journal ----")
                        print(read_journal)
            
                except FileNotFoundError:
                    print("No journal file found")
        
 
            read()
            
        elif choice == "2":
            
                   
            def write():
                
                write_journal = input("Enter your text:")
    
                with open("my_file.txt", "a") as file:
        
                    file.write(write_journal)

                    print("The file has been written successfully")

            
            
            write()
            
        elif choice == "3":
                
            print("Exited..!")
            break
        
        else:
            
            print("Please enter a valid input")
            break
           

process()

