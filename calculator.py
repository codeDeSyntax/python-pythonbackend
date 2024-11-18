print("Math calculator")


addition = "addition"
multiplication = "multiplication"
subtraction = "substraction"

print("Choose operation")
print(addition )
print(subtraction  )
print(multiplication )

choice = input("Choose operation: ")

if choice :
    num1 = int(input("first number: "))
    num2 = int(input("second number: "))

    if choice == "addition":
        result = num1 + num2
        print("The result of your operation is " + str(result))

    elif choice == "multiplication": 
        result = num1 * num2
        print("The result of your operation is " + str(result))

    else:
        result = num1 - num2
        print("The result of your operation is " + str(result))


       






