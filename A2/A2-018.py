color,num = map(str,input().split())
num = int(num)
i = 1
case = ''

if num % 3 == 0:
  case = 'M0'
elif num % 3 == 1:
  case = 'M1'
  num -= 1
elif num % 3 == 2:
  case = 'M2'
  num -= 2

if color == 'R':
  while i < num:
      print('Red',end=' ')
      print('Green',end=' ')
      print('Blue',end=' ')
      i += 3
  if case == 'M1':
    print('Red')
  elif case == 'M2':
    print('Red',end=' ')
    print('Green')

elif color == 'G':
  while i < num:
      print('Green',end=' ')
      print('Blue',end=' ')
      print('Red',end=' ')
      i += 3
  if case == 'M1':
    print('Green')
  elif case == 'M2':
    print('Green',end=' ')
    print('Blue')

elif color == 'B':
  while i < num:
      print('Blue',end=' ')
      print('Red',end=' ')
      print('Green',end=' ')
      i += 3
  if case == 'M1':
    print('Blue')
  elif case == 'M2':
    print('Blue',end=' ')
    print('Red')