''' 1.factorial 

n=int(input("enter"))
fact=1 
if(n==0 or n==1):
    print(1)
else:
    for i in range(1,n+1):
        fact=fact*i
print(fact)


 2.area of a circle

n=float(input("enter radius"))
area=3.14*n*n

print("The area is " + str(area))
'''
'''
n=input().split(' ')
print(n)
sum=0
for i in n:
    sum=sum+int(i)
print("Sum=",sum)
'''
'''
3.. strong number
n=input()
sum=0
for i in n:
    i=int(i)
    pro=1
    
    while(i>1):
        pro=pro*i
        i=i-1
    sum=sum+pro
if(sum==int(n)):
    print("YES")
else:
    print("NO")
'''
'''
4.. leap year
year = int(input("Enter a year :"))
if(year%4 == 0):
    if( year%100 == 0):
        if ( year%400 == 0):
            print(year, end =" ")
            print(" is a leap year")
        else:
            print(year, end =" ")
            print(" is not a leap year")
    else:
        print(year, end =" ")
        print(" is a leap year")
else:
    print(year, end =" ")
    print(" is not a leap year")
'''
'''
5.. GCD of two numbers
def GCD(x,y): 
  
    if x > y: 
        small = y 
    else: 
        small = x 
    for i in range(1, small+1): 
        if((x % i == 0) and (y % i == 0)): 
            gcd = i 
              
    return gcd 
a=int(input())
b=int(input())
print(GCD(a,b))
'''
'''
6.. prime or not
n=int(input())
if n>1:
    for i in range(2,n):
        if(n%i==0):
            print("not prime")
    else:
        print("prime")
else:
    print("not")
'''
'''
7... prime numbers in given range

m=int(input())
n=int(input())
for num in range(m,n+1):
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            print(num)

'''
'''
8. number  palindrome or not
n=int(input())
temp=n
rev=0
while n>0:
    rev=rev*10+n%10
    n=n//10
if(temp==rev):
    print("palindrome")

else:
    print("not")
'''
'''
9.. string palindrome or not
n=input()
b=n[::-1]
if n==b:
    print("palindrome")
else:
    print("not")
'''
'''
10. armstrong or not
num=int(input())
order = len(str(num))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10
if num == sum:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")

'''
'''
11.. largest element in list
a=int(input())
l=[]
for i in range(0,a):
    b=int(input())
    l.append(b)
l.sort()
print(l[-1])
'''
'''
12.. armstrong numbers in given range 
m=int(input())
n=int(input())

for num in range(m,n+1):
   order = len(str(num))
   sum = 0

   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)
    
'''
'''
13.. fibonacci series upto n
n = int(input("Enter the nth value: "))
a = 0
b = 1
sum = 0
print("Fibonacci Series : ", end = " ")
while(sum <= n):
     print(sum, end = " ")
     a = b
     b = sum
     sum = a + b
'''
'''
14.. first n fibonacci series

n=5
a = 2
b = 1
c=[]
if (n < 1): 
    print("error0")
for x in range(n+1): 

    c.append(a)
    sum= a + b 
    a = b
    b = sum
print(c)
f=0
for i in range(len(c)):
    r=c[i]
for i in str(r):
    f+=int(i)
print(f)
'''
'''
15.. decimal to binary

n=int(input())
print(bin(n).replace("0b","")) 
'''
'''
16..binary to decimal
binary=int(input()) 
decimal, i = 0, 0
while(binary != 0): 
    dec = binary % 10
    decimal = decimal + dec * pow(2, i) 
    binary = binary//10
    i += 1
print(decimal)
'''
'''
17.. decimal to octal
n=int(input())
print(oct(n))
'''
'''
18.. octal to decimal
num=int(input()) 
decimal_value = 0 
base = 1
while (num): 
    last_digit = num % 10
    num = int(num / 10)
    decimal_value += last_digit * base
    base = base * 8  
print("The decimal value is :",decimal_value)      
'''


'''
19..binary to octal
binary = input()
if binary == 'x':
    exit();
else:
    temp = int(binary, 2)
    print(binary,"in Octal =",oct(temp))
'''
'''
20.. octal to binary
octal = input("Enter any number in Octal Format: ")
if octal == 'x':
    exit();
else:
    dec = str(int(octal, 8))
    decm = int(dec)
    print(octal,"in Binary =",bin(decm))
'''
'''
21.. remove duplicates
mylist = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist))
print(mylist)
'''
'''
a=int(input())
b=int(input())
list1=[]
list2=[]
for i in range(a):
    
    val=float(input())
    list1.append(val)
for i in range(b):
    val1=float(input())
    list2.append(val1)
if (a and b)!=0:
    cost=sum(list1)*18+sum(list2)*12
    print(str(cost)+" "+"INR")
else:
    print("NOT")
'''
'''
a=['coffee','tea','sugar']
b=['Sai','Manohar','abdff']
c=input()
d=int(input())
if c=='a':
    print("Take",a[d-1])
elif c=='b':
    print("Take",b[d])
else:
    print("NOT")
'''
'''
n=input()
count=0
for i in n:
    if i=='a':
        count=count+1
print(count)
'''
'''
n=input()
l=[]
for i in n:
    l.append(i)
count=0
for j in l:
    if j=='a':
        count=count+1
print(count)
'''
'''
trialing zeros
n=int(input()
i=5
count=0
while ((n/i)>=1):
    count=count+int(n/i)
    i=i*5
print(int(count))

'''
'''
n=int(input())
arr=[]
for i in range(0,n):
    t=int(input())
    arr.append(t)
m=dict()
for i in range(n):
    m[arr[i]]=m.get(arr[i],0)+1
for i in range(n):
    arr[i]=n-m[arr[i]]
print(arr)
'''
'''

import math
n=int(input())
a=n**0.5
if ((a-math.floor(a))==0):
    print("YES")
else:
    print("NO")
    '''
'''
n=input().split(" ")
print(n)
'''
'''
a=input()
b=a.split(' ')
c=' '.join(reversed(b))
print(c)
'''
'''
import sys
n=int(input())
a=[]
for i in range(0,n):
    t=int(input())
    a.append(t)
c=len(a)
min=sys.maxsize
smin=sys.maxsize
for j in range(c):
    if(a[j]<min):
        smin=min
        min=a[j]
    elif((a[j]<smin) and a[j]!=min):
        smin=a[j]
print(smin+min)
'''
'''
n=int(input())
a=[]
for i in range(0,n):
    t=int(input())
    a.append(t)
c=len(a)
product = 0
for i in range (c): 
    for j in range ( i+1,c): 
        product = product + a[i]*a[j]
print(product)
'''
'''
n=int(input())
a=list(map(int,input().strip().split(' ')))[:n]
print(a)
'''
'''
string=input()
b=len(string)
string.strip()
t=""
for i in range(b):
    ch=string[i]
    if ch!=' ':
        t+=ch
    else:
        print(t[0].upper()+". ",end="")
        t=""
temp=""
for j in range(len(t)):
    if j==0:
        temp+=t[0].upper()
    else:
        temp+=t[j].lower()
print(temp)
'''
'''
count coprimes
def gcd(a,b):  
    if (a == 0 or b == 0): 
        return False
    if (a == b): 
        return a 
    if (a > b): 
        return gcd(a-b, b) 
          
    return gcd(a, b-a)
def coprime(a,b):
    return (gcd(a,b)==1)
n=int(input())
arr=list(map(int,input().strip().split(' ')))[:n]
c=len(arr)
count=0
for i in range(0, c-1):
    for j in range(i+1,c):
        if(gcd(arr[i],arr[j])==1):
            count=count+1
print(count)
'''
'''
power of 4 or not
n=int(input())
while(n%4==0):
    n=n/4
if(n==1):
    print('yes')
else:
    print("no")
'''
'''
reverse by groups
a=[1,2,3,4,5,6,7,8,9,10]
res=[]
k=3
for i in range(0,len(a),k):
    res.extend((a[i:i + k])[::-1])
print(res)
'''
'''
for i in range(1,6):
    print(pow(i,2))
'''
'''
a=["abd","vfgd_sge","dxtfgcgf_vfhj","etf_gaevd","gf_vhjv"]
b=[]
c=[]
for i in a:
    if '_' in i:
        b.append(i)
    else:
        c.append(i)
        
print(b)
print(c)
'''
'''
n=5
m=int(n)
for i in range(0, n) : 
    for j in range(0,m):
        if(i==0 or  i==n-1):
            print("#",end=' ')
        elif(j==0 or j==m-1):
            print("*",end=' ')
        else:
            
            print(' ',end=' ')
    print()
'''
'''
def ab(str):
    if len(str)==0:
        return str
    else:
        return ab(str[1:])+str[0]
name='GuviGeek'
print(ab(name))
'''
'''
l1=[2,4,6,8,10]
l2=[1,3,5,7,9]
l3=[]
j,k=0,0
for i in range(10):
    if(i%2==0):
        l3.append(l1[j])
        j=j+1
    else:
        l3.append(l2[k])
        k=k+1
print(l3)
'''
'''
print([i.lower() for i in 'HELLO'])'''
'''
for i in range(1,3):
    print(i)
    for j in range(1,6):
        print(j,end='')
    print()
'''
'''
def sqrt(n,max=0,min=0):
    if max==0:
        max=n
    res=(max+min)/2
    if(res*res==n):
        return res
    elif res*res>=n:
        max=res
    else:
        min=res
    return(sqrt(n,max,min))
print(sqrt(100))
'''
'''
b=list(str)
d=[]
for i in b:
    c=b.count(i)
    d.append(c)
print(max(d))
'''
'''
# Python3 program to find Minimum 
# number of jumps to reach end

# Returns minimum number of jumps
# to reach arr[h] from arr[l]
def minJumps(arr, l, h):

	# Base case: when source and
	# destination are same
	if (h == l):
		return 0

	# when nothing is reachable 
	# from the given source
	if (arr[l] == 0):
		return float('inf')

	# Traverse through all the points 
	# reachable from arr[l]. Recursively 
	# get the minimum number of jumps 
	# needed to reach arr[h] from 
	# these reachable points.
	min = float('inf')
	for i in range(l + 1, h + 1):
		if (i < l + arr[l] + 1):
			jumps = minJumps(arr, i, h)
			if (jumps != float('inf') and
					jumps + 1 < min):
				min = jumps + 1

	return min

# Driver program to test above function
arr = [2,1,1]
n = len(arr)
print('Minimum number of jumps to reach',
	'end is', minJumps(arr, 0, n-1))

# This code is contributed by Soumen Ghosh
'''
'''
list1=[]
list2=[]
n,m = map(int,input().split())
for i in range(0,n):
    list1=list1+[input()]
for i in range(0,m):
    list2=list2+[input()]
for i in range(n):
    for j in range(m):
        if(list1[i]==list2[j]):
            print(i+1,end=" ")
for j in range(m):
    if(list1[i]==list2[j]):
        print(i+1)
'''
'''
if(c==1):
    return a+b
elif(c==2):
    return a-b
elif(c==3):
    return a*b
else:
    return a/b
'''
'''
a=["mon","mon","bun"]
a.sort()
b=[]
for i in a:
    b.append(a.count(i))
c=[]
d=[]
e=[]
w=[]
for i in a:
    if i not in  c:
        c.append(i)
for i in b:
    if i not in d:
        d.append(i)
e=[str(x) for x in d]
w=[i+j for i,j in zip(c,e)]
for i in w:
    print(i)
'''
'''
class Item:
	def __init__(self,itemName,itemType,unitPrice):
		self.itemName=itemName
		self.itemType=itemType
		self.unitPrice=unitPrice
class Store:
	def __init__(self,itemInventory):
		self.itemInventory=itemInventory
	def buyItem(self,item,quantity):
		for items,quantityInHand in itemInventory.items():
			if(items.itemName.lower()==item.lower() and quantity==0):
				return None
			if(items.itemName.lower()==item.lower() and quantity>quantityInHand):
				itemInventory[items]=0
				return items.unitPrice*quantityInHand
			if(items.itemName.lower()==item.lower() and quantity<=quantityInHand):
				itemInventory[items]=quantityInHand-quantity
				return items.unitPrice*quantity
		return None
n=int(input())
itemInventory={}
for i in range(n):
	itemName=input()
	itemType=input()
	unitPrice=int(input())
	quantityInHand=int(input())
	itemInventory[Item(itemName,itemType,unitPrice)]=quantityInHand
store1=Store(itemInventory)
order={}
num=int(input())
for i in range(num):
	itemName=input()
	quantity=int(input())
	order[itemName]=quantity
for itemName,quantity in order.items():
	billAmount=store1.buyItem(itemName,quantity)
	if(billAmount==None):
		print(itemName,"is not available")
	else:
		print("Bill of the item ",itemName,"=",billAmount)
print("Stock in Hand:")
for item,quantityInHand in store1.itemInventory.items():
	print(item.itemName,quantityInHand,sep=" ")

'''
'''
def function(b):
    b.sort()
    return b[0]+b[-1]
a=int(input())
c=input().split()
b=[int(i) for i in c]
d=function(b)
print(d)
'''
'''


class Solution:
    def breakPalindrome(self, palindrome: str):
        if len(palindrome) == 1:
            return ""
        for i in range(len(palindrome) // 2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i + 1:]
        return palindrome[:-1] + 'b';
a=Solution()
b=input()
c=Solution.breakPalindrome(b)
print(c)
'''
'''


def breakPalindrome(palindrome):
    for i in range(len(palindrome)//2):
        if palindrome[i] != 'a':
            return palindrome[:i] + 'a' + palindrome[i+1:]
    return palindrome[:-1] + 'b' if len(palindrome) >= 2 else ""

b=input()
c=breakPalindrome(b)
print(c)


'''

'''

a=input()
b=list(a)
e=[]
for i in b:
    c=b.count(i)
    d=i+str(c)
    e.append(d)
e=list(dict.fromkeys(e))
f=''.join(e)
print(f)
'''

'''

def breakPalindrome(palindrome) -> str:
    if len(palindrome) == 1:
        return "IMPOSSIBLE"
    for i in range(len(palindrome) // 2):
        if palindrome[i] != 'a':
            return palindrome[:i] + 'a' + palindrome[i + 1:]
    return palindrome[:-1] + 'b';
b=input()
print(breakPalindrome(b))
'''
'''
a='Hello World'
b=list(a)
for i in b:
    if i==' ':
        b.remove(i)
for i in b:
    if i==i.upper():
        c=b.index(i)
        b[c]=i.lower()
    elif i==i.lower():
        d=b.index(i)
        b[d]=i.upper()
c=''.join(b)
print(c)
'''
'''
class abc:
    def __init__(self,name):
        self.name=name
    #def display(self):
        #return self.name
class defc(abc):
    def display(self):
        return self.name
b=defc('spandan')
print(b.display())
'''
'''
strong number
a=153
d=[int(i) for i in str(a)]
c=[]
fact=1
for i in d:
    if i==0 or i==1:
        c.append(1)
    else:
        for j in range(1,i+1):
            fact=fact*j
        c.append(fact)
        fact=1
    
print(c)
e=sum(c)
if(e==a):
    print('strong number')
else:
    print('not strong')
        
'''




'''
a=input()
b=a.split()
c=' '.join(reversed(b))
print(c)
'''


# A naive Python implementation of LIS problem

""" To make use of recursive calls, this function must return
two things:
1) Length of LIS ending with element arr[n-1]. We use
max_ending_here for this purpose
2) Overall maximum as the LIS may end with an element
before arr[n-1] max_ref is used this purpose.
The value of LIS of full array of size n is stored in
*max_ref which is our final result """
'''
# global variable to store the maximum
global maximum


def _lis(arr, n):

	# to allow the access of global variable
	global maximum

	# Base Case
	if n == 1:
		return 1

	# maxEndingHere is the length of LIS ending with arr[n-1]
	maxEndingHere = 1

	"""Recursively get all LIS ending with arr[0], arr[1]..arr[n-2]
	IF arr[n-1] is maller than arr[n-1], and max ending with
	arr[n-1] needs to be updated, then update it"""
	for i in xrange(1, n):
		res = _lis(arr, i)
		if arr[i-1] < arr[n-1] and res+1 > maxEndingHere:
			maxEndingHere = res + 1

	# Compare maxEndingHere with overall maximum. And
	# update the overall maximum if needed
	maximum = max(maximum, maxEndingHere)

	return maxEndingHere


def lis(arr):

	# to allow the access of global variable
	global maximum

	# lenght of arr
	n = len(arr)

	# maximum variable holds the result
	maximum = 1

	# The function _lis() stores its result in maximum
	_lis(arr, n)

	return maximum


# Driver program to test the above function
arr = [10, 22, 9, 33, 21, 50, 41, 60]
n = len(arr)
print "Length of lis is ", lis(arr)

# This code is contributed by NIKHIL KUMAR SINGH
'''

'''
a=int(input())
b=int(input())
d=int(input())
c=a**b
e=c%d
print(c)
'''
'''
a=input()
b=list(a)
count1=0
for i in b:
    if i==' ':
        b.remove(i)
for i in b:
    if (i.isalnum()):
        count1+=1
print(count1)
'''

'''


# Python program to find the longest substring with k unique
# characters in a given string
MAX_CHARS = 26

# This function calculates number of unique characters
# using a associative array count[]. Returns true if
# no. of characters are less than required else returns
# false.
def isValid(count, k):
	val = 0
	for i in range(MAX_CHARS):
		if count[i] > 0:
			val += 1

	# Return true if k is greater than or equal to val
	return (k >= val)

# Finds the maximum substring with exactly k unique characters
def kUniques(s, k):
	u = 0 # number of unique characters
	n = len(s)

	# Associative array to store the count
	count = [0] * MAX_CHARS

	# Tranverse the string, fills the associative array
	# count[] and count number of unique characters
	for i in range(n):
		if count[ord(s[i])-ord('a')] == 0:
			u += 1
		count[ord(s[i])-ord('a')] += 1

	# If there are not enough unique characters, show
	# an error message.
	if u < k:
		print ("Not enough unique characters")
		return

	# Otherwise take a window with first element in it.
	# start and end variables.
	curr_start = 0
	curr_end = 0

	# Also initialize values for result longest window
	max_window_size = 1
	max_window_start = 0

	# Initialize associative array count[] with zero
	count = [0] * len(count)

	count[ord(s[0])-ord('a')] += 1 # put the first character

	# Start from the second character and add
	# characters in window according to above
	# explanation
	for i in range(1,n):

		# Add the character 's[i]' to current window
		count[ord(s[i])-ord('a')] += 1
		curr_end+=1

		# If there are more than k unique characters in
		# current window, remove from left side
		while not isValid(count, k):
			count[ord(s[curr_start])-ord('a')] -= 1
			curr_start += 1

		# Update the max window size if required
		if curr_end-curr_start+1 > max_window_size:
			max_window_size = curr_end-curr_start+1
			max_window_start = curr_start

	print (s[max_window_start:max_window_start + max_window_size])

# Driver function
s = "qwertyytrewq"
k = 2
kUniques(s, k)

# This code is contributed by BHAVYA JAIN

str
result=CountAlphanumericChar(str)

def CountAlphanumericChar(str):
    if str==' ':
        print(-1)
    else:
        b=list(str)
    count1=0
    for i in b:
        if i==' ':
            b.remove(i)
    for i in b:
        if (i.isalnum()):
            count1+=1
    print(count1)

   ''' 
'''   
a=input()
c=a.split()
b=[int(i) for i in c]
b.remove(b[0])
print("List Before Swapping:")
print(b)
b[0],b[-1]=b[-1],b[0]
print("List After Swapping:")
print(b)
        
'''

'''
i=0
while i<17:
        print(i)
        i-=3
        i+=5

else:
        print(0)
'''
'''
a=1
if a in range(0,3):
    print("Age :", "[0-3]")
'''
'''
a=int(input())
b=int(input())
sum=0
for i in range(1,b+1):
    sum=sum+a*i
print(int(sum/b))
'''
'''
a=3
b=5
c=5
for c in range(3,8):
    if((b+c-a)>(a+b)):
        break
    a=(a+a)+b
    a=c^a
print(a+b)
'''

'''
p=1
q=11
r=7
if(q-r+p)>(p+q):
    q=(r^10)+p
print(p+q+r)
'''
'''
m=1
a=[3,1,1,3]
if(a[0]&1>a[1]&2 and a[2]&3>a[1]&2):
    for i in range(1,3):
        m=m+a[i]
print(m)
'''
'''
a=1
b=4
c=4
if(b<a or (b+c)>(a-b)):
    a=(b^11)+b
    c=2+c
print(a+b+c)
'''
'''
p=5
q=5
r=10
for i in range(2,6):
    q=(p+8)+p
    if((p+q-r)<(r-p)):
        continue
    else:
        break
    q=q+q
print(p+q)
'''
'''
a=1
b=7
c=4
for c in range(4,8):
    a=(c+b)+c
    if((b+c)<(10-b)):
        a=2^b
print(a+b)
'''
'''
a='tcs'
b='xplore'
ans=a[::-2]+b[::-1]
print(ans)
'''


'''
n=5
a=[10,20,30,40,50]
b=[]
for i in range(0,n):
    s=0
    for j in range(i+1,n):
        s=s+a[j]
    b.append(s)
print(*b)
'''
'''
a='h e l l o'
a=a.replace(" ","")
print(a)
'''
'''
a='h e l l o'
a="".join(a.split())
print(a)
'''
'''
s='welcome to tcs xplore xplore'
s=s.split(' ')

s=list(dict.fromkeys(s))
print(*s)

'''
'''
a=5
b=1
s=a or b
print(s)
'''
'''
a='xplore'
print(a[::2])
'''
'''
m={"a":1,"b":2,"c":3,"d":4,"e":5}
r=[]
for i,j in m.items():
    r+=[i]*j
print(r)
'''
'''
a=[0,1,1,2,3,5,2]
n=len(a)
for i in range(n):
    k=a.count(a[i])
    if(k==1):
        print(a[i])
NONE of options'''
'''
a='hello'
a=list(a)
d={}
for i in a:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)
'''
'''
a=[{"name":"George","age":28},{"name":"Manny","age":21},{"name":"Noah","age":15}]
print(sorted(a,key=lambda i:i['name']))
'''
'''
a=[1,2,3,4,5]
j=0
b=[]
sum=0
for i in a:
    j=j+i
    b.append(j)
print(b)
'''
'''
class Ques:
    def __init__(self,qid,mo,so):
        self.qid=qid
        self.mo=mo
        self.so=so
        self.status="Not Answered"
class Student:
    def __init__(self,rid,qa):
        self.rid=rid
        self.qa=qa
    def evaluateq(self,ansk):
        for k,v in ansk.items():
            for i in self.qa:
                if i.qid==k:
                    if i.mo==v:
                        i.status="correct"
                        break
                    else:
                        i.status="incorrect"
                        break
    def findGrade(self):
        total=0
        for i in self.qa:
            if i.status=="correct":
                total+=i.so
        if total>=80:
            return "A"
        elif total>=70:
            return "B"
        elif total>=60:
            return "C"
        else:
            return "F"
x=int(input())
l=[]
for i in range(x):
    qid=int(input())
    mo=int(input())
    so=int(input())
    l.append(Ques(qid,mo,so))
cd=int(input())
ansk={}
for i in range(cd):
    qid=int(input())
    co=int(input())
    ansk[qid]=co
s=Student(69,l)
s.evaluateq(ansk)
for i in s.qa:
    print(i.qid,i.status)
print(s.findGrade())
'''


'''
a=[]
b=2
for i in range(1,11):
    a.append(i)
for i in a:
    if i%b==0:
        
        a.remove(i)
print(a)
'''

'''
a=[1,2,3,4,5,6,7,8,9,10]
n=len(a)
i=0
itr=1
while(itr<len(a)):
    i=itr
    while(i<len(a)):
        a.remove(a[i])
        print(a)
        i=i+itr
    #print(a)
    itr+=1
#for i in a:
    #print(i,end=" ")
'''

'''

a=input()
b=list(a)
c1=0
c2=0
for i in b:
    if i==' ':
        b.remove(i)
for i in b:
    if i.isupper():
        c1+=1
    elif i.islower():
        c2+=1
print(a)
print('Upper case characters :',c1)
print('Lower case characters :',c2)
'''
'''
a='1234'
b='1234'
c=a.endswith(b)
if c:
    print("yes")
'''
'''
c=[]
f=[]
d=['a','e','i','o','u']
a=int(input())
for i in range(a):
    b=input().split()
'''
'''
d=['amjpyhhh','AMJPYTTVDHFJFDJHD']

f=['a','e','i','o','u']

for i in d:
    #print(i)
    for j in i:
        c=j.lower()
        #print(c)
        if c not in f:
            print('*'+c,end='')
    print(end='\n')
'''
'''
n=36
a=[0]*(n+1)
for i in range(2,n+1):
    if a[i]==0:
        for j in range(i,n+1,i):
            a[j]+=i
print(a[n])
'''
'''
n=21
b=[]
e=[]
for i in range(1,n+1):
    if(n%i==0):
        b.append(i)
print(b)
for i in b:
    if(i>1):
        
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            e.append(i)
print(e)
'''    

'''
a='Hello World'
g=a.split()
print(g)
d=a[::-1]
e=d.split()
f=e[::-1]
for i in f:
    print(i,end=' ')
#j=' '.join(f)
#print(j)
'''
'''
a={0:'abc',1:'defg'}
for i in a:
    print(a[i])
'''
'''
a=lambda x,y:x*y
print(a(10,5))
'''
'''
a=[1,2,3,4,5,6,7,8]
c=len(a)
d=int(c/2)
for i in range(len(a)):
    if (i==d):
        a[:i],a[i:]=a[i:],a[:i]
print(a)

'''
'''
a=2
b=7
c=13
for c in range(3,8):
    b=a
    if((9&a)<b):
        continue
    else:
        a=(c+c)^a
        b=c
print(a+b)
'''
'''
a=5
b=3
c=10
b=1+b
if((5&a)<(c^5)):
    a=(a+12)+c
print(a+b+c)
'''
'''
p=3
q=5
r=6
if((8+9)<(6+q)):
    r=4+r
r=(r+4)+p
print(p+q+r)
'''
'''
a=9
b=3
c=5
for i in range(3,6):
    b=(1+2)&a
    if((c+b+a)<(a-c)):
        continue
    else:
        break
    b=(6+7)+a
print(a+b)

'''
'''

def TransformString(str1,atr2):
	m = len(str1)
	n = len(str2)

	if n != m:
		return -1

	count = [0] * 256

	for i in range(n):	 
		count[ord(str2[i])] += 1
	for i in range(n):	 
		count[ord(str1[i])] -= 1
	for i in range(256): 
		if count[i]:
			return -1

	
	res = 0
	i = n-1
	j = n-1
	while i >= 0:
	
		
		while i>= 0 and str1[i] != str2[j]:
			i -= 1
			res += 1

		
		if i >= 0:
			i -= 1
			j -= 1

	return res
'''

'''
str1= "hlole"
str2 = "hello"
print("Minimum number of operations required is " + str(minOps(str1,str2)))
'''

'''
s=17
e=62
k=5
count=0
for i in range(s,e+1):
    if (i%10)==k:
        count+=1
print(count)
'''
'''
a='abcdefgaaaeiou'
b=[]
c=['a','e','i','o','u']
count1=0
count2=0
count3=0
count4=0
count5=0
for i in a:
    if(i=='a'):
        count1+=1
        continue
    elif(i=='e'):
        count2+=1
        continue
    elif(i=='i'):
        count3+=1
        continue
    elif(i=='o'):
        count4+=1
        continue
    elif(i=='u'):
        count5+=1
        continue
b.append(count1)
b.append(count2)
b.append(count3)
b.append(count4)
b.append(count5)
for i in range(len(b)):
    if b[i]==max(b):
        print(c[i])
'''
'''
a='12345'
b='345'
if(a[-len(b):]==b):
    print("YES")
else:
    print("NO")
'''
'''
sum=0
for i in range(1,input1+1):
    if(input1%i==0):
        sum+=i
print(sum)
'''
'''
def countDecodings(s):
	if len(s) == 0 or len(s) == 1 and s[0] == '0':
		return 0
	return numDecodingsHelper(s, len(s))


def numDecodingsHelper(s,n):
	if n == 0 or n == 1:
		return 1
	count = 0
	if s[n-1] > "0":
		count = numDecodingsHelper(s, n-1)
	if s[n - 2] == '1'or s[n - 2] == '2' and s[n - 1] < '7':
		count += numDecodingsHelper(s, n - 2)
	return count
a='1234'
print(countDecodings(a))
'''

'''
n=10
a=0
b=1
c=1
while(c<n):
    b=b*c
    a=a+(bz
'''
'''
a=[1,2,3,4]
while(len(a)>0):
    a.pop()
print(a)
'''








#an instance or object of a class
'''
tup=("ab","bc","cd")
tup[1]='change'
o/p it will throw error
'''
'''
x=30.6
y=9.0
print(x//y)
print(x/y)
o/p
3.0
3.4
'''
'''
x=("Aman","Raman","Sahil","Shwets")
y=list(x)
y[1]="Kiran"
x=tuple(y)
print(x[1])
o/p Kiran
'''
'''
def ab(*citizens):
    print(citizens[1]+" is fully vacciated.")
ab("Aman","Radhika","Soniya","Vimal")
ab("Saman","Rakhi","Soniya","Rishab","Arun")
o/p
Radhika is fully vacciated.
Rakhi is fully vacciated.
'''
'''
print(bool(""))
print(bool(0))
o/p
False
False
'''
'''
x="GoodMorning and welcome"
print(x[4:])
o/p
Morning and welcome
'''
'''
a=["Arrow","Bow","Chariot"]
for x in a:
    if x=="Bow":
        continue
    print(x)
o/p
Arrow
Chariot
'''
'''
a="It's mandatory to complete \"Xplore\" training."
print(a)
'''
'''
lambda
false
'''
'''
len(str)
'''
'''
maximum of id
'''
'''
l=[15,34,21,11,334,11]
mini=999
i=0
for i in range(len(l)):
    if(l[i]<=mini):
        mini=l[i]
        m=i
print(m)
print(mini)
o/p
5 11
'''
'''
i=0
while i<5:
    print(i)
    i+=1
    if i==3:
        break
else:
    print(0)
o/p 012
'''
'''
x=[12,43,12,32,65,76]
print(x[-2:-1])
o/p 65
'''

'''

c = 0
num = 2
letest = 0

while (c != input1):
   count = 0
   for i in range(2,num):
      if (num % i == 0):
         count+=1
         break
   if (count == 0):
      c+=1
      letest = num
   num = num + 1
return letest

'''

'''

import random 
a=[1,2,3,5,6]
m=3
b=[]
while(len(b)<m):
   c=random.choice(a)
   if (c not in b):
      b.append(c)
   
print(b)
'''
'''
n=int(input())
count=0
while (n>=5):
    n=n//5
    count+=n
print(count)
'''
'''
n=int(input())
i=5
count=0
while ((n/i)>=1):
    count=count+n//i
    i=i*5
print(count)
'''
'''
d=['a','b','c']
for i in d:
    if i=='b':
        continue
    print(i)
'''
'''
n=15
if n>0:
    print(n*-1)
else:
    print(n)
o/p -15
'''
'''
def func1(str):
    str="Turn your wounds into wisdom"
    print(str)
str="Dreams dont work unless you do"
func1(str)
print(str)

o/p Turn your wounds into wisdom
    Dreams dont work unless you do
'''
'''
s1={"AI","Machine Learning","Angular JS"}
s1.remove("Devops")
print(s1)
o/p error
'''
'''
t1=(500,550,600,650,600,550)
t2=t1[3:-1]
print(t2)
o/p (650,600)
'''
'''
def f1(a,b,c,d):
    print(a%c)
n=[20,30,40,50]
f1(*n)
o/p 20
'''
'''
def fn1(a,b):
    s=a**2
    print(s)
    def fn2(a,b):
        return a+b
    add=fn2(a,b)
    return add+5
result=fn1(50,10)
print(result)
o/p 2500
    65
'''
'''
l=["icse","cbse","state"]
print("\n".join(l))
'''
'''
a=[2018,2019,2018,2020,2019,2021]
a=list(set(a))
print(a)
o/p [2018, 2019, 2020, 2021]
'''
'''
str="Be Yourself"
d={}
for i in str:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for i in d:
    print(i,d[i])
o/p
B 1
e 2
  1
Y 1
o 1
u 1
r 1
s 1
l 1
f 1
'''
'''
popitem
'''
'''
l=["s","a","o","r"]
while len(l)>0:
    l.pop()
print(len(l))
o/p 0
'''
'''
l=[10,24,35,80,105,150,200]
for a in l:
    if(a>100):
        break
    if(a % 5==0):
        print(a)
o/p 10
    35
    80
'''
'''
m=[{"name":"Taj mahal","Built":1653},{"name":"Charminar","Built":1591},{"name":"Gateway of India","Built":1924}]
print(sorted(m,key=lambda m:m['name']))
o/p
[{'name': 'Charminar', 'Built': 1591}, {'name': 'Gateway of India', 'Built': 1924}, {'name': 'Taj mahal', 'Built': 1653}]
'''
'''
class el:
    def __init__(self,name,etype):
        self.name=name
        self.etype=etype
    def availability(self,required):
        return f"The requuired number of {self.etype}laptop is {required}"
class Lap(el):
    def availability(self,required=10):
        return super().availability(required=10)
l=Lap("Reatail Store","Dell")
print(l.availability())
o/p
    The requuired number of Delllaptop is 10

'''
'''
dict1={'color':{'attri':['red']},'brand':{'hyundai':'advanced'}}
dict2={'availability':{'status':'instock'},'color':{'hyundai':'white'}}
dict3={**dict1,**dict2}
print(dict3)
o/p
    {'color': {'hyundai': 'white'}, 'brand': {'hyundai': 'advanced'}, 'availability': {'status': 'instock'}}
'''
'''
from math import log,floor
n=256
a=log(n)/log(4)
a=floor(a)
if a:
    print(n, "is a power of 4")
else:
    print(n, "is not a power of 4")
'''



	
'''	
from sys import maxint
c=[]
a=int(input())
for i in range(a):
    b=int(input())
    c.append(b)
max_so_far = -maxint - 1
max_ending_here = 0
	
for i in range(0, size):
    
    
    max_ending_here = max_ending_here + a[i]
    if (max_so_far < max_ending_here):
	max_so_far = max_ending_here

    if max_ending_here < 0:
	max_ending_here = 0
print(max_so_far)
'''
'''
a=int(input())
b=[]
f=[]
for i in range(a):
    c=input()
    b.append(c)
print(b)
for i in b:
    for j in i:
        if j not in f:
            f.append(j)
            print(''.join(f))
'''
'''
import sys
a=int(input())
b=[int(i) for i in input().split()]
d=int(input())
b.sort()
sum = 0
cost = 0
min_cost = sys.maxsize
for i in range(0, a):
    if (b[i] < 0):
        cost = abs(b[i]) * d + (sum - abs(b[i]) * i)
        sum += abs(b[i])
        min_cost = min(min_cost,cost)
print(min_cost)
'''

'''
def areDistinct(strr, i, j):

	visited = [0] * (26)

	for k in range(i, j + 1):
		if (visited[ord(strr[k]) -
				ord('a')] == True):
			return False
			
		visited[ord(strr[k]) -
				ord('a')] = True

	return True

def longestUniqueSubsttr(strr):
	
	n = len(strr)
	
	res = 0
	
	for i in range(n):
		for j in range(i, n):
			if (areDistinct(strr, i, j)):
				res = max(res, j - i + 1)
				
	return res


st = input()
len = longestUniqueSubsttr(st)
print(len)
'''	
'''
a=int(input())
b=int(input())
c=[int(i) for i in str(b)]
count=0
for i in c:
    if i==a:
        count+=1
print(count)

'''

'''
n=int(input())
a=[]
for i in range(n):
    c=input()
    a.append(c)
b=[]
for i in a:
    if i not in b:
        b.append(i)
b.sort()
print(b)
'''


'''
n=5
a=1
for i in range(n):
    for j in range(i+1):
        print(a,end=" ")
        a+=1
    print()
'''
#takes input as string without size and convert it to char array and int array
'''
import java.util.Arrays;
import java.util.regex.Pattern;
import java.util.Scanner;
public class Main {

    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine();
        String[] words = line.split(" ");
        System.out.println(Arrays.toString(words));
        int size=words.length;
        int [] arr = new int [size];
        for(int i=0; i<size; i++) {
            arr[i] = Integer.parseInt(words[i]);
        }
        System.out.println(Arrays.toString(arr));
        System.out.println(arr.getClass().getSimpleName());

        
    }
}
'''
'''
# Python 3 program to swap even
# and odd bits of a given number

# Function for swapping even
# and odd bits
def swapBits(x) :
	
	# Get all even bits of x
	even_bits = x & 0xAAAAAAAA

	# Get all odd bits of x
	odd_bits = x & 0x55555555
	
	# Right shift even bits
	even_bits >>= 1
	
	# Left shift odd bits
	odd_bits <<= 1

	# Combine even and odd bits
	return (even_bits | odd_bits)


# Driver program
# 00010111
x = 20

# Output is 43 (00101011)
print(swapBits(x))


# This code is contributed
# by Nikita Tiwari.

'''
'''
p=7
q=6
r=15
for r in range(2,7):
    p=(p^3)+q
    q=(q+p)+r
for r in range(5,7):
    p=(12+4)+q
print(p+q)
'''
'''
def f(a,b):
    if(a>1):
        return a+f(b-1,a-2)
    else:
        return a+b
    return a-b
print(f(4,2))
'''
'''

n=int(input())
s = 0
for i in range(1,n):
    if(n % i == 0):
        s = s+ i
if (s ==n):
    print("Perfect")
else:
    print("Not Perfect")
    
'''
'''
def rotate(arr,d,n):
    arr[:]=arr[d:]+arr[:d]
    return arr
n=int(input())
arr=[int(i) for i in input().split()]
d=int(input())
print(rotate(arr,d,n))
'''
'''
import pymysql as pysql
db=pysql.connect("localhost","root","","test",)
ins=db.cursor()
query="insert into student values(2,'charan')"
ins.execute(query)
db.commit()
print("success")
db.close()
'''

a=3
b='12'
c=list(b)
c.sort(reverse=True)
d=int(''.join(c))
print(d)

