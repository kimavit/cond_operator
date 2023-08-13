num = int (input())
d = num % 10
c = ((num // 10) % 10)
b = ((num // 100) % 10)
a = num // 1000
if a+d == b-c :
    print ("ДА")
else :
    print ("НЕТ")