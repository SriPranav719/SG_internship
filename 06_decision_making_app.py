# Build a decision-making application using complex conditional logic.
                           
age = int(input("Enter your age: "))

degree = input("Enter your Educational level : ")

percentage = float(input("Enter your percentage : "))

experence = input("Enter the years of experience : ")


if age > 21 and experence and percentage > 70:
    print("Yes you are eligible for job")
    
else:
    print("Your eligibilty ciretria doesnt match our requirements")
    

    

def student_grades(score):
    
    if score <90 <= 100:
        print("Your grade is A+")