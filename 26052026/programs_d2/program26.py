def cal(num1,num2,operator):
  if operator=="+":
    return num1 + num2
  elif operator=="-":
    return num1 - num2
  elif operator=="*":
    return num1 * num2
  elif operator=="/":
    return num1 / num2
while True:
  try:
    num1=int(input("enter first number:"))
    break
  except ValueError:
    print("please enter numbers only")
    continue
while True:
  try:
    num2=int(input("enter second number:"))
    break
  except ValueError:
    print("please enter numbers only")
    continue

op=("+","-","*","/")
while True:
  try:
    operator=str(input("enter operator:"))
    if operator in op:
     break
  except ValueError:
    print("please enter valid operators")
    continue
print("result:",cal(num1,num2,operator))
