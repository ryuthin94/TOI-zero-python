temp = int(input(""))
prefix = input("")
if prefix == "C" or prefix == "c":
  if temp <= 0:
    print("solid")
  elif temp > 0 and temp < 100:
    print("liquid")
  elif temp >= 100:
    print("gas")
elif prefix == "F" or prefix == "f":
  if temp <= 32:
    print("solid")
  elif temp > 32 and temp < 212:
    print("liquid")
  elif temp >= 212:
    print("gas")