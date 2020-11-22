sum = [ ]
a=1
while a < 1000:
    if a % 3 ==0:
        sum.append(a)
    elif a % 5 == 0:
        sum.append(a)
    a = a + 1
print (sum)
sums = 0
for i in sum:
    sums = sums + i
print (sums)

