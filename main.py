from art import logo
#Calculator

#add
def add(n1, n2):
  return n1 + n2

#multiply
def multiply(n1, n2):
  return n1 * n2

#divide
def divide(n1, n2):
  return n1 / n2

#subtract
def subtract(n1, n2):
  return n1 - n2

operations = {
  '+' : add,
  '-' : subtract,
  '*' : multiply,
  '/' : divide
}

def calculator():
  print(logo)
  num1 = float(input("What's the first number?  "))
  
  for operation in operations:
    print(operation)
  
  should_continue = True
  while should_continue:
    operation_symbol = input("Pick an operation from the above options: ")
    num2 = float(input("What's the second number?  "))
    Calc_func = operations[operation_symbol]
    answer = Calc_func(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input("Do you want to perform more operations press 'y' or if you want to start a new calculation press 'n' ") == "y" :
      num1 = answer
    else:
      should_continue = False
      calculator()

calculator()