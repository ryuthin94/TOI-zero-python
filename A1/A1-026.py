n1 = int(input(""))
n2 = int(input(""))
n3 = int(input(""))
even = 0
odd = 0

if n1 % 2 == 0:
  even += 1
else:
  odd += 1
if n2 % 2 == 0:
  even += 1
else:
  odd += 1
if n3 % 2 == 0:
  even += 1
else:
  odd += 1
  
print("even " + str(even))
print("odd " + str(odd))