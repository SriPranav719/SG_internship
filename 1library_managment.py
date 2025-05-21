library = []

while True:
    print("=== Library Menu ===")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter choice (1-6): ")
    print()

    if choice == '1':
        title = input("Enter book title: ")
        author = input("Enter author: ")
        isbn = input("Enter ISBN: ")
        quantity = int(input("Enter quantity: "))
        
        library.append({"title": title, "author": author, "isbn": isbn, "quantity": quantity})
        print("Book added successfully.")

    elif choice == '2':
        
        if not library:
            
            print("No books available")
        else:
            
            for book in library:
                
                print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}, Quantity: {book['quantity']}")

    elif choice == '3':
        
        search_book = input("Enter title or author to search: ").lower()

        for book in library:
            
            if search_book in book['title'].lower() :
                
                print(f"Found: Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}, Quantity: {book['quantity']}")
               
            else:
                
                print("Book not found")
                break
      

    elif choice == '4':
        
        isbn = input("Enter ISBN of the book to issue: ")
        
        for book in library:
            
            if book['isbn'] == isbn:
                
                if book['quantity'] > 0:
                    book['quantity'] -= 1
                    print("Book issued successfully.\n")
                    
                else:
                    print("Book not available.\n")
                    break
            else:
                print("Book not found")
                break
            

    elif choice == '5':
        
        isbn = input("Enter ISBN of the book to return: ")
        
        for book in library:
            
            if book['isbn'] == isbn:
                
                book['quantity'] += 1
                print("Book returned successfully.\n")
                
                break
        else:
            print("Book not found in library.\n")

    elif choice == '6':
        
        print("Exiting Library System.")
        break

    else:
        print("Invalid choice")
