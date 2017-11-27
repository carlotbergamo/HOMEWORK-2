def solveMeFirst(a,b):    #first
   return a+b 
  
num1 = input()
num2 = input()
res = solveMeFirst(num1,num2)
print res


import sys                #second

def simpleArraySum(n, ar):
    return sum(ar)

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = simpleArraySum(n, ar)
print(result)


import sys            #third

def solve(a0, a1, a2, b0, b1, b2):
    alice=0
    bob=0
    if a0>b0:
        alice+=1
    if a1>b1:
        alice+=1
    if a2>b2:
        alice+=1
    if b0>a0:
        bob+=1
    if b1>a1:
        bob+=1
    if b2>a2:
        bob+=1
    return alice, bob

a0, a1, a2 = raw_input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = raw_input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print " ".join(map(str, result))


import sys         #fourth

def aVeryBigSum(n, ar):
    return sum(ar)

n = int(raw_input().strip())
ar = map(long, raw_input().strip().split(' '))
result = aVeryBigSum(n, ar)
print(result)


import sys        #fifth

n = int(raw_input().strip())
a = []
b = []
c = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)
for i in range(len(a)):
    b+=[a[i][i]]
    c+=[a[i][-(i+1)]]
sum1 = sum(b)
sum2 = sum(c)
print abs(sum1-sum2)


import sys      #sixth

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
zero=0
positive=0
negative=0
for i in arr:
    if i==0:
        zero+=1
    if i>0:
        positive+=1
    if i<0:
        negative+=1
print float(positive)/n
print float(negative)/n
print float(zero)/n


import sys      #seventh

n = int(raw_input().strip())
for i in range(n):
    print ' '*(n-(i+1))+'#'*(i+1)


import sys         #eighth
import itertools
arr = map(int, raw_input().strip().split(' '))
comb = itertools.combinations(arr, 4)
maximum=0
minimum=sum(arr)
for i in comb:
    s=sum(i)
    if s>maximum:
        maximum=s
    if s<minimum:
        minimum=s
print minimum, maximum


import sys         #ninth

def birthdayCakeCandles(n, ar):
    m=max(ar)
    return ar.count(m)

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = birthdayCakeCandles(n, ar)
print(result)


import sys         #tenth

def timeConversion(s):
    if s[8]=='P' and s[:2]=='12':
        newtime=s[:8]
    if s[8]=='A' and s[:2]=='12':
        newtime= '00'+s[2:]
        newtime=newtime[:8]
    if s[8]=='A' and s[:2]!='12':
        newtime=s[:8]
    if s[8]=='P' and s[:2]!='12':
        first=str(int(s[:2])+12)
        newtime=first+s[2:]
        newtime=newtime[:8]
    return newtime
        

s = raw_input().strip()
result = timeConversion(s)
print(result)