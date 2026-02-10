num=int(input("Enter a number: "))
new=num
n=len(str(num))
arm=0
while new>0:
    id=new%10
    arm=arm+(id**n)
    new=new//10
if arm==num:
    print("Armstrong")
else:
    print("Not Armstrong")