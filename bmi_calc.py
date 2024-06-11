def Bmi_calculator(height,weight):
    Bmi=weight/(height*height)
    return Bmi
def main():
    try:
        Weight = float(input("Enter your weight in kilograms : "))
        Height = float(input("Enter your height in meters : "))

        if Weight <= 0 or Height <= 0:
            print("Input is invalid! Weight and height must be greater than zero.")
        else:
            bmi = Bmi_calculator( Height,Weight)
            print(f"Your BMI is: {bmi:.2f}")

        if bmi < 18.5:
            print("Category:Under weight")
        elif bmi < 24.9:
            print("Category:Normal weight")
        elif bmi < 29.9:
            print("Category:Over weight")
        else:
            print("Category:obese")

    except ValueError:
        print("Input is invalid! Weight and height must be numeric values.")

if __name__ == "__main__":
    main()