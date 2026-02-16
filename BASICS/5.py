num=int(input("Enter a number"))
result =[]
n=1
while n<=(num//2 ):
    if num%n == 0:
        result.append(n)
    n+=1
result.append(num)
print(result)