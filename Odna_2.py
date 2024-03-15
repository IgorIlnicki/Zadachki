from functools import reduce

a = [2,4,6,8,10,12]
volume = reduce(lambda x,y: x+y, map(int,a))                 #  int, input().strip().split()))

s = 0
for el in a:
    s+=el

print(f"     volume = {s}")
print(f"     volume = {volume}")