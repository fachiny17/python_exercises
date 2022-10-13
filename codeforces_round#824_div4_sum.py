# Codeforces exercise 

lst = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,5,16,17,18,19,20]

a = int(input('a = '))
b = int(input('b = '))
c  = int(input('c = '))

num = (a) + (b)
pep = (a) + (c)
og = (b) + (c)


if int(c) == num and c in lst:
    print('YES')
elif int(a) == og and a in lst:
    print('YES')
elif int(b) == pep and b in lst:
    print('YES')
else:
    print('NO')