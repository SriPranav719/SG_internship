# Create pattern-printing programs using nested loops.
                                    
pattern = "*"
for i in range(0, 10):
        print(pattern*i)
        

pattern = "*"
for i in range(10, 0, -1):
    print(pattern*i)
    
    

pattern = "|"

for row in range(10):
    for column in range(50):
        pass
    print(pattern * column)


rows = 6

for i in range(1, rows, -1):
    spaces = " " * (rows - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)



    


