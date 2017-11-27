numb= int(raw_input())     #first
lenght= int(raw_input())
array= map( int, raw_input().split())
pos = array.index(numb)
print pos


from __future__ import print_function   #second

def insertionSort(ar):    
    numb=ar[m-1]
    new=ar[::-1]
    for element in range(1, len(new)):
        if new[element] > numb:
            new[element-1] = new[element]
            print (*new[::-1])
        elif new[element] < numb:
            new[element-1] = numb
            print (*new[::-1])
            break
        if element == m-1 and new[element]>numb:
            new[m-1] = numb
            print(*new[::-1])
            break

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)


from __future__ import print_function      #third
def insertionSort(ar):    
    for element in range(1, len(ar)):
        if ar[element] > ar[element-1]:
            print (*ar)
        elif ar[element] < ar[element-1]:
            ar = sorted(ar[:element+1]) + ar[element+1:]
            print (*ar)

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)


def insertion_sort(l):     #fourth
    for i in xrange(1, len(l)):
        j = i-1 
        key = l[i]
        while (j >= 0) and (l[j] > key):
           l[j+1] = l[j]
           j -= 1
        l[j+1] = key

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertion_sort(ar)
print (" ".join(map(str,ar)))


n = int(raw_input())      #fifth
ar = map(int, raw_input().split())
numb = 0
for pos in range(len(ar)):
    new_pos = pos
    while ar[pos] < ar[new_pos - 1] and new_pos!=0:
        numb += 1
        new_pos -= 1
    if ar[new_pos] >= ar[new_pos-1] or new_pos == 0:
        ar.insert(new_pos, ar[pos])
        ar.pop(pos+1)

print (numb)


def partition(ar):     #sixth  
    equal=[ar[0]]
    left=[]
    right=[]
    for element in range(1, len(ar)):
        if ar[element] > ar[0]:
            right+=[ar[element]]
        elif ar[element] < ar[0]:
            left+=[ar[element]]
        else:
            equal+=[ar[element]]
    for i in left+equal+right:
        print (i,)

m = input()
ar = [int(i) for i in raw_input().strip().split()]
partition(ar)


n=int(raw_input())     #seventh
ar=map(int, raw_input().split())
lst=[]
numb=range(100)
for element in numb:
    lst+=[ar.count(element)]
for i in lst:
    print (i,)


n = int(raw_input())     #eight
ar = map(int, raw_input().split())
for element in sorted(ar):
    print (element,)


from itertools import combinations     #ninth
n=int(raw_input())
ar=map(int, raw_input().split())
ar=sorted(ar)
dif= abs(ar[0]-ar[1])
lst=[ar[0], ar[1]]
for element in range(1,len(ar)-1):
    dif1 = abs(ar[element+1]-ar[element])
    if dif1 < dif:
        dif = dif1
        lst = [ar[element], ar[element+1]]
    elif dif1 == dif:
        lst+=[ar[element], ar[element+1]]

for i in lst:
    print (i,)


n=int(raw_input())     #tenth
ar=map(int,raw_input().split())
new_arr=sorted(ar)
if len(ar)%2!=0:
    median=new_arr[(len(ar)-1)/2]
elif len(ar)%2==0:
    a=new_arr[(len(ar))/2]
    b=new_arr[(len(ar)+2)/2]
    median=(a+b)/2

print (median)