N = int(input())
m = int(input())

for i in range(N-1):
  n = int(input())
  if n < m:
    m = n

print(m)