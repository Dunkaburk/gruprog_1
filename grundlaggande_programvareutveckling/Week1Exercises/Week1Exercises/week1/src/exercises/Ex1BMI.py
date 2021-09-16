def BMI_calculator():
    weight = input("Please enter weight")
    height = input("Please enter height in meters")

    bmi = float(weight)/(float(height)*float(height))

    return ("Your BMI is", bmi)




print(BMI_calculator())


 