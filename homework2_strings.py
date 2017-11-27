import sys       #first

s = raw_input().strip()
result=1
for letters in s:
    if letters==letters.upper():
        result+=1
print result


import sys        #second
new_s=''
n = int(raw_input().strip())
s = raw_input().strip()
k = int(raw_input().strip())
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for letter in s:
    if letter.lower() in alphabet:
        if letter==letter.lower():
            if letter in alphabet:
                f=alphabet.index(letter)
                numb=f+k
                if numb<=25:
                    new_s+=alphabet[numb]
                else:
                    new_numb=numb % 26
                    new_s+=alphabet[new_numb]
        else:
            if letter.lower()in alphabet:
                f=alphabet.index(letter.lower())
                numb=f+k
                if numb<=25:
                    new_s+=(alphabet[numb]).upper()
                else:
                    new_numb=numb % 26
                    new_s+=(alphabet[new_numb]).upper()
    else:
        new_s+=letter
print new_s


import sys         #third
S = raw_input().strip()
n=0
l=[]
a=''
for letter in S:
    if len(a)<=2:
        a+=letter
    if len(a)==3:
        l+=[a]
        a=''
for element in l:
    if element[0]!='S':
        n+=1
    if element[1]!='O':
        n+=1
    if element[2]!='S':
        n+=1
print n


import sys         #fourth
n=0
d=[]
letters=['h','a','c','k','e','r','r','a','n','k']
q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    for letter in s:
        if letter==letters[n]:
            n+=1
        if n==10:
            break
    if n==10:
        print 'YES'
        d=[]
        n=0
    else:
        print 'NO'
        d=[]
        n=0


a=raw_input().strip()     #fifth
l=[]
c=a.lower()
for letter in c:
    l.append(letter)
b=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
n=0
for letter in b:
    if letter in l:
        n+=1
    if n==26:
        break
if n==26:
    print 'pangram'
else:
    print 'not pangram'