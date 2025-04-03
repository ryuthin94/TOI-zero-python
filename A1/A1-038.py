N = int(input())
n = 1
while n <= N:
  if n%5 == 0:
    print("X", end="")
  elif n%5 != 0:
    print("*", end="")
  n += 1