#Defining function for addition.
def add(x, y):
   return x + y

#Defining function for substraction.
def subtract(x, y):
   return x - y

#Defining function for multiplication.
def multiply(x, y):
   return x * y

#Defining function for division.
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

   #Knowing which operation to perform.
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

if __name__ == '__main__':
    start()
