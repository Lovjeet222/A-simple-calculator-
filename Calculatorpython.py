print("Hello welcome to the smart calculator..... ")
print("Menu:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Exit")
while True :
    choose = int(input("Choose 1/2/3/4/5:"))
    if choose == 5:
        print("Thanks for using smart calculator .")
        break
    Num1 = int(input("Enter number 1 :"))
    Num2 = int(input("Enter number 2 :"))
    if choose == 1 :
        print("addition:",Num1+Num2)
    elif choose == 2:
        print("Your answer :", Num1-Num2)
    elif choose == 3 :
        print("Your answer:",Num1*Num2)
    elif choose == 4:
        print("Your answer :",Num1/Num2)
