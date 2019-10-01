# https://www.hackerrank.com/challenges/py-if-else/

n = int(input().strip())
if n % 2 != 0:
    print('Weird')
elif 2 <= n <= 5 and n % 2 == 0:
    print('Not Weird')
elif 6 <= n <= 20 and n % 2 == 0:
    print('Weird')
else:
    print('Not Weird')

# https://www.hackerrank.com/challenges/python-loops/

n = int(input('Enter number: '))
for i in range(n):
    print(i**2)

# https://www.hackerrank.com/challenges/write-a-function/


def is_leap(year):
    leap = False
    if year%4 == 0:
        if year%400 == 0:
            return True
        elif year%100 == 0:
            return leap
        else:
            return True
    else:
     return leap

# https://www.hackerrank.com/challenges/python-print/

n = int(input())
l = ''
for i in range(n+1):
    l = l + str(i)
k = int(l)
print (k)

# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/

a = input('Enter the number of students who have subscribed to the English newspaper: ')
eng = input('List of student roll numbers who have subscribed to the English newspaper: ')
b = input('Enter the number of students who have subscribed to the French newspaper: ')
fr = input('List of student roll numbers who have subscribed to the French newspaper: ')
listeng = [int(s) for s in eng.split() if s.isdigit()]
listeng = set(listeng)
listfr = [int(s) for s in fr.split() if s.isdigit()]
result = listeng.symmetric_difference(listfr)
print(len(result))