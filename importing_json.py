import json


def menu():
    print("------------ JSON DATA PROCESSOR OPERATIONS:----------")
    print("1. Read")
    print("2. Add")
    print("3. update")
    print("4. Delete")
    print("5. search")
    print("6. Exit")


def read_json():
    with open("data.json", "r") as f:
        # read = f.read()           # read as string
        # # data = json.load(read)   # convert string to Python object
        data = json.load(f)

        print(data)


def add_data():
    with open("data.json", "r") as f:
        data = json.load(f)

    user_name = input("Enter your name:")
    user_age = int(input("Enter your age:"))
    user_mail = input("Enter your email:")

    user = {"id": len(data) + 1, "name": user_name, "age": user_age, "email": user_mail}

    data.append(user)

    with open("data.json", "w") as f:
        json.dump(data, f, indent=2)


def update_data():
    with open("data.json", "r") as f:
        data = json.load(f)
        user_id = int(input("Enter id to update teh data:"))

        for user in data:
            if user["id"] == user_id:
                new_name = input("Enter new name: ")
                new_age = int(input("Enter new age: "))
                new_email = input("Enter new email: ")

                user["name"] = new_name
                user["age"] = new_age
                user["email"] = new_email
                
                break
            
            else:
                print("User ID not found!")

    with open("data.json", "w") as f:
        json.dump(data, f, indent=2)


def delete_data():
    with open("data.json", "r") as f:
        data = json.load(f)
        user_id = int(input("Enter id to delete:"))

        for user in data:
            
            if user["id"] == user_id:
                data.remove(user)
                found = True
                break
            
            else:
                print("User ID not found.")

    with open("data.json", "w") as f:
        json.dump(data, f, indent=2)


def search_data():
    with open("data.json", "r") as f:
        data = json.load(f)
        user_id = int(input("Enter id to search:"))

        for user in data:
            if user["id"] == user_id:
                print(user)
                found = True
                break
            else:
                print("User ID not found.")


def main():
    
    while True:
        
        menu()
        select = input("Enter our choice: ")
        if select == "1":
            read_json()
        elif select == "2":
            add_data()
        elif select == "3":
            update_data()
        elif select == "4":
            delete_data()
        elif select == "5":
            search_data()
        elif select == "6":
            print("Exiting")
            break
        else:
            print("Invaild input")
            break


main()