a1,b1 = map(str,input().split())
a2,b2 = map(str,input().split())

if a1 == a2 and b1 == b2:
  print(1000000)
elif a1 != a2 and b1 == b2:
  print(100000)
elif b1[3] == b2[3] and b1[4] == b2[4] and b1[2] != b2[2] and a1 == a2:
  print(1000)
elif b1[2] == b2[2] and b1[3] == b2[3] and b1[4] == b2[4] and a1 == a2:
  print(2000)
elif b1[3] == b2[3] and b1[4] == b2[4] and b1[2] != b2[2] and a1 != a2:
  print(100)
elif b1[2] == b2[2] and b1[3] == b2[3] and b1[4] == b2[4] and a1 != a2:
  print(200)
elif a1 == a2 and b1 != b2:
  print(20)
else:
  print(0)