name = input()
surname = input()
age = input()

if len(name) > 5 and len(surname) > 5:
  password = name[0] + name[1] + surname[-1] + age[-1]
  print(password)
else:
  password = name[0] + age + surname[-1]
  print(password)