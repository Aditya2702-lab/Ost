print("***** Calculator *****")
l=[]
def addition(l):
    print(f"Sum : {sum(l)}")
    l.clear()
def subtraction(num1,num2):
    print(f"Difference : {round((num1-num2),2)}")
def multiplication(l):
    m=1
    for i in l:
        m*=i
    print(f"Multiplication : {m} ")
    l.clear()
def division(num1,num2):
    print(f"Division : {round((num1/num2),2)}")

while(True):
    try:
          ch=int(input("Addition : 1\nSubtraction : 2\nMultiplication : 3\nDivision : 4\nExit : 5\nEnter your choice : "))
          if ch==5:
              break
          match ch:
              case 1:
                  n=int(input("How many numbers you want to add : "))
                  for i in range(0,n):
                      l.append(float(input(f"Enter {i+1} number : ")))
                  addition(l)
              case 2:
                  a=float(input("Enter the 1 number : "))
                  b=float(input("Enter the 2 number : "))
                  subtraction(a,b)
              case 3:
                  n = int(input("How many numbers you want to multiply : "))
                  for i in range(0, n):
                      l.append(float(input(f"Enter {i + 1} number : ")))
                  multiplication(l)
              case 4:
                  a = float(input("Enter the 1 number : "))
                  b = float(input("Enter the 2 number : "))
                  division(a, b)
          print("-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-")
    except ZeroDivisionError:
          print("Division by zero is not allowed!")
    except ValueError:
           print("Invalid Input! please enter valid input.")
    print("-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-")




