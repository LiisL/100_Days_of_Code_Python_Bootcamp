#Calculator
from art import logo

#Add
def add(n1, n2):
  return n1+n2
  
#Substract
def substract(n1, n2):
  return n1-n2
#Multiply
def multiply(n1, n2):
  return n1*n2

#Divide
def divide(n1, n2):
  return n1/n2

operations  = {

  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide
}
def calculator():
  print(logo)
  num1 = float(input("Whats the first number: "))
  
  
  for key in operations:
    print(key)
  should_continue = True
  while should_continue:
  
    operation_symbol = input("Pick an operation from the list above: ")
    num2 = float(input("Whats the next number: "))
    
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    if input(f"Type 'y' to continue calculating with {answer} or type 'n' to exit.") == "y":
      num1 = answer
    else: 
      should_continue = False
      calculator()


calculator()