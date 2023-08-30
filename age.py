a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a < b:
    m = a
else:
    m = b
if c < m:
    m = c
if d < m:
    m = d
print(m)