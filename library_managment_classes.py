class Library:
    books = [] 

    def add_a_book(self):
        
        book_title = input("Enter book title: ")
        book_author = input("Enter book author: ")
        book_quantity = int(input("Enter the quantity: "))

        if book_title and book_author:
            
            Library.books.append({
                
                "title": book_title,
                "author": book_author,
                "quantity": book_quantity
                
            })
            
            return("Book added successfully.")
            
        else:
            return("Error: Title and author are required to add a book.")


class Student(Library):

    def show_books(self):
        
        if not Library.books:
            
            return("No books available.")
            
        else:
            for book in Library.books:
                
                return(f"Title: {book['title']}, Author: {book['author']}, Quantity: {book['quantity']}")
                
                
    def borrow_book(self):
        search_book = input("Enter name of the book or author to borrow: ").lower()

        for book in Library.books:
            if (search_book in book["title"].lower()) or (search_book in book["author"].lower()):
                if book["quantity"] > 0:
                    book["quantity"] -= 1
                    return f"You borrowed: {book['title']}"
                else:
                    return "Sorry, this book is out of stock."

    
        return "Book not found"

    

    def return_a_book(self):
        
        return_title = input("Enter the name of the book you want to return: ")
        
        for book in Library.books:
            
            if return_title.lower() == book["title"].lower():
                
                book["quantity"] += 1
                
                return (f"The book is returned: {book['title']}")


def main():
    
    student = Student()
    
    while True:
        print("\n------Library Menu-------")
        print("1. Show all books")
        print("2. Add a book")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Exit")

        choice = input("Choose one of these options: ")

        if choice == "1":
            print(student.show_books())
            
        elif choice == "2":
            print(student.add_a_book())
            
        elif choice == "3":
            
            print(student.borrow_book())
        
        elif choice == "4":
            
            print(student.return_a_book())
            
        elif choice == "5":
            print("Thank you !")
            
            break
        
        else:
            print("Invalid option. Please choose 1-5.")

main()





