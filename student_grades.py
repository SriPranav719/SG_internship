student = input("Enter your score : ") 
try:
    student = float(student)

except ValueError:
    print("enter a valid input")
    
    
# print(student)
# print(type(student))

if student > 100:
    print("Enter score between 1 to 100")

elif student > 90 and student<= 100:
    print("Your grade is A+")

elif student > 80 and student <= 90:
    print("Your grade is A")
    
elif student > 70 and student <= 80:
    print("Your grade is B+")
    
elif student > 60 and student <= 70:
    print("Your grade is B")
    
elif student > 50 and student <= 60:
    print("Your grade is C+")
    
elif student >= 35 and student <= 50:
    print("Your grade is C")
    
elif student < 35:
    print("Your grade is F")