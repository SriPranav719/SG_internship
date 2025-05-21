my_daily_task_list = []

choose = ["1. Add Task", "2. View Tasks", "3. Remove Task", "4. Exit"]

while True:
  
    for option in choose:
        print(option)

    serial_num = input("Enter the serial number: ")

    if serial_num == "1":
        
        enter_new_task = input("Enter a new task: ")
        
        my_daily_task_list.append(enter_new_task)
        
        print("The task is added successfully")

    elif serial_num == "2":
        
        if not my_daily_task_list:
            
            print("The tasks are not added yet")
        else:
            
            print("Your tasks are:")
            
            for i in range(len(my_daily_task_list)):
                
                print(f"{i + 1}. {my_daily_task_list[i]}") 

    elif serial_num == "3":
        
        if not my_daily_task_list:
            
            print("No tasks to remove ")
            
        else:
            for i in range(len(my_daily_task_list)):
                
                print(f"{i + 1}. {my_daily_task_list[i]}")

            try:
                index = int(input("Enter the task number to remove: ")) - 1
                
                if 0 <= index < len(my_daily_task_list):
                    
                    removed_task = my_daily_task_list.pop(index)
                    
                    print(f"Removed: {removed_task}")
                else:
                    print("Invalid number.")
                    
            except ValueError:
                
                print("Please enter a valid number.")

    elif serial_num == "4":
        
        print("Thank you! the application has closed")
        
        break

    else:
        print("Invalid option,  Please choose number between 1  to 4.")
