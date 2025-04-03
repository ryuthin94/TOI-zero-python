N = int(input())
vowel = ['A', 'E', 'I', 'O', 'U']
num = 0

for i in range(N):
  a = input()
  if a[0] in vowel:
    num += 1

print(num)