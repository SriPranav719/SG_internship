print("Enter number for Arithametic operations")
print("1. Additon")
print("2. Subtraction")
print("3. Multiplication")
print("4.Division ")

choice = input("Enter the choice : ")
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))



if choice == "1":
    print(num1 + num2)

elif choice == "2":
    print(num1 - num2)

elif choice == "3":
    print(num1 * num2)
    
elif choice == "4":
    if num1 == 0 or num2 ==0:
        print("cannot divide by 0") 
    else :
        print(num1/num2)
     


                                
                                    # data type conversions
    
#int to float

# integer= 123
# print(float(integer))


# #float to int

# float = 344
# print(int(float))

# #int to str

# int = 4

# print(str(int))