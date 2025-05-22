import csv

FILENAME = "students.csv"

def menu():
    print("\n--- Student Marks CLI ---")
    print("1. Read")
    print("2. Add")
    print("3. Search")
    print("4. Exit")

def read_csv():
    with open(FILENAME, "r") as f:
        
        reader = csv.reader(f)
        for row in reader:
            print(row)

def add_record():
    
    student_id = input("Enter ID: ")
    name = input("Enter name: ")
    subject = input("Enter subject: ")
    marks = input("Enter marks: ")

    with open(FILENAME, "a", newline="") as f:
        
        writer = csv.writer(f)
        
        writer.writerow([student_id, name, subject, marks])
        
        print("Record added.")

def search_record():
    
    student_id = input("Enter ID to search: ")
    with open(FILENAME, "r") as f:
        
        reader = csv.reader(f)
        found = False
        
        for row in reader:
            if row[0] == student_id:
                print(row)
                found = True
                
        if not found:
            print(" Record not found.")

def main():
    
    while True:
        
        menu()
        choice = input("Choose: ")
        
        if choice == "1":
            read_csv()
            
        elif choice == "2":
            add_record()
            
        elif choice == "3":
            search_record()
            
        elif choice == "4":
            print("Bye!")
            break
        
        else:
            print("Invalid choice!")
            break

main()
