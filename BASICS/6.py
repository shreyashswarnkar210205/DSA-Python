from math import *
num=int(input("Enter a Number "))
res=[]
for i in range(1, int(sqrt(num))+1):
    if num%i==0:
        res.append(i)
        if i!=num//i:
            res.append(num//i)
        else: 
            continue
res.sort()
print(res)
#TC -> O(sqrt(n))+O(n log(n))