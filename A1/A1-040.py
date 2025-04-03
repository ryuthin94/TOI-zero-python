n = 0
sum = 0
n = int(input())

if n == 1:
  sum += 100
elif n == 2:
  sum += 120
elif n == 3:
  sum += 200
elif n == 4:
  sum += 60
  
while n != 5:
  n = int(input())
  if n == 1:
    sum += 100
  elif n == 2:
    sum += 120
  elif n == 3:
    sum += 200
  elif n == 4:
    sum += 60

print("Bye Bye")
print("Total Calories:",sum)