word = input()
vowel = ['a', 'e', 'i', 'o', 'u']
v = 0

for i in range(0, 3):
  if word[i] in vowel:
    v += 1

print(v)