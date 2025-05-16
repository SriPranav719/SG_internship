import random


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



#                     #song playlist
                    
                    
my_playlist = []

choose = ["1. Add Song", "2. View Songs", "3. Remove Song", "4. Shuffle the playlist ", "5. Exit" ]

while True:
    
    

    for option in choose:
        print(option)
        
    serial_num = input("Enter the serial number: ")
    
    if serial_num == "1":
        
        add_song = input("Enter name of the song : ")
        
        my_playlist.append(add_song)
        
        print("The song added successfully !")
        
        
    elif serial_num == "2":
        
        if not my_playlist:
            print("Their are no songs added to the playlist")
            
        else:
            print("-----Your Playlist------")
            for i in range(len(my_playlist)):
                
                print(f"{i + 1}. {my_playlist[i]}")
            
    elif serial_num == "3":
        
        if not my_playlist:
            print("Their are no songs in playlist to remove")
            
        else:
            for i in range(len(my_playlist)):
                
                print(f"{i + 1}. {my_playlist[i]}") 
                
            try:
                index = int(input("Enter the serial num of the song you want to remove from the playlist : "))-1
                
                if 0<= index <= len(my_playlist):
                    
                    removed_song = my_playlist.pop(index)
                    
                    print(f"{removed_song} is successfully removed from the playlist")
                    
                else:
                    print("Invalid number")
                    
            except ValueError:
                print(" Please enter a valid number")
                
    elif serial_num == "4":
        
        
        print("playing :", random.choice(my_playlist))
        
        

    elif serial_num == "5":
    
        print("Thank you! the application is closed")
        
        break
    
    else:
        print("Invalid input, choose song according to the serial number given only")
    
        
        
        
    
    