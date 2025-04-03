def move_last_digit_to_front(num):
  num_str = str(num)
  if len(num_str) == 1:
      return num  
  return int(num_str[-1] + num_str[:-1])

num = int(input(""))
operation = input("")

modified_num = move_last_digit_to_front(num)

if operation == '+':
  result = num + modified_num
  operator = "+"
elif operation == '*':
  result = num * modified_num
  operator = "*"
else:
  print("Invalid operation")
  result = None

if result is not None:
  print(f"{num} {operator} {modified_num} = {result}")