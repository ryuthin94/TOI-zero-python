bub,bub_val = input().split()
tea,sweet,tea_val = input().split()
tea_val = int(tea_val)
bub_val = int(bub_val)
total = 0

if bub == "H":
  total = 5 * bub_val
elif bub == "O":
  total = 3 * bub_val
elif bub == "J":
  total = 2 * bub_val

if tea == "R":
  if sweet == "1":
    total = total + (tea_val * 12)
  elif sweet == "2":
    total = total + (tea_val * 18)
  elif sweet == "3":
    total = total + (tea_val * 25)
elif tea == "T":
  if sweet == "1":
    total = total + (tea_val * 15)
  elif sweet == "2":
    total = total + (tea_val * 20)
  elif sweet == "3":
    total = total + (tea_val * 30)
elif tea == "M":
  if sweet == "1":
    total = total + (tea_val * 10)
  elif sweet == "2":
    total = total + (tea_val * 15)
  elif sweet == "3":
    total = total + (tea_val * 20)

print(total)