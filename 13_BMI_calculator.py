# Create a BMI calculator function.
def bmi_calculator():
    
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    bmi = weight / (height ** 2)
    
    print(("Your BMI is: ",bmi))

    if bmi < 18.5:
        return("You are underweight.")
        
    elif 18.5 <= bmi < 24.9:
        return("You have a normal weight.")
        
    elif 25 <= bmi < 29.9:
        return("You are overweight.")
        
    else:
        return("You have obesity")

print(bmi_calculator())