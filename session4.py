import radndom
print("welcome to this python aplication")
print("what do u want this aplication do")
print("1.add two numbers. ")
print("2. random number. ")
print("3.print a random word ")
print("4.multiplye two numbers.  ")
inpute=input("enter ur choise : ")
match inpute:
    case "1":
        num1=int(input("enter the first number : "))
        num2=int(input("enter the sec number : "))
        print(f"the sum of {num1} and {num2} is {num1 + num2}")