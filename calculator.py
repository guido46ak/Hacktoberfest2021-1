def add(x, y):
   return x + y

def subtract(x, y):
   return x - y

def multiply(x, y):
   return x * y

def divide(x, y):
   return x / y

def start():
   print("""Select Operation.
   1.Add
   2.Subtract
   3.Multiply
   4.Divide""")

   choice = input("Select Number(1/2/3/4): ")
   num1 = int(input("Input First Number: "))
   num2 = int(input("Input Second Number: "))

   if choice == '2':
      print(num1,"-",num2,"=", subtract(num1,num2))

   elif choice == '1':
      print(num1,"+",num2,"=", add(num1,num2))

   elif choice == '4':
      print(num1,"/",num2,"=", divide(num1,num2))

   elif choice == '3':
      print(num1,"*",num2,"=", multiply(num1,num2))

   else:
      print("Wrong Input")