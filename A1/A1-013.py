ch = input("")
num = int(input(""))

if ch == "H" and num == 4567:
  print("safe unlocked")
elif ch == "H" and num != 4567:
  print("safe locked - change digit")
elif ch != "H" and num == 4567:
  print("safe locked - change char")
else:
  print("safe locked")