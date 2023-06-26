num1 = int(input("Enter 1st operand="))
num2 = int(input("Enter 2nd operand="))
print("Select any 1 operator/option for operation on the operand:")
option = int(input("1)Addition\n2)Subtraction\n3)Multiplication\n4)Division\n5)Module\n\n6)exponential\n7)Floor\n"))
if option==1:
    print("Addition =",num1+num2)
elif option==2:
    print("Subtraction =",num1-num2)
elif option==3:
    print("Multiplication =",num1*num2)
elif option==4:
    print("Division =",num1/num2)
elif option==5:
    print("Module =",num1%num2)
elif option==6:
    print("Exponential =",num1**num2)
elif option==7:
    print("Floor =",num1//num2)
else:
    print("Invalid choice. Please select a valid choice between 1-7.")