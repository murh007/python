'''
age = 3
if age >=18:
   print('your age is',age)
   print('adult')
else:
   print('your age is',age)
   print('teenager')

age = 8
if age >=18:
   print('adult')
elif age >=6:
   print('teenager')
else:
   print('kid')  


s = input('birth:')
birth = int(s)
if birth <2000:
   print('00前')
else:
   print('00后')

names = ['michale,''bob','tracy']
for name in names:
    print(name)

sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum + x
    print(sum)

a = list(range(5))
print(a)

sum = 0
for x in range(101):
    sum = sum + x
    print(sum)

sum =0
n = 99
while n>0:
   sum = sum +n
   n = n - 2
print(n)
'''
