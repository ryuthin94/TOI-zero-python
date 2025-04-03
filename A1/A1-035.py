N = int(input())
sum = 0
n = 1
all = 0

for i in range(N):
  sum = n*n
  n = n + 1
  all = all + sum

print(all)