n = int(input())
factorial = 1

for i in range(n):
  factorial = factorial * n
  n = n-1

print(factorial)