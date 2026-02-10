#Palindrome kind of problems
num = int(input("Enter a number: "))
#num = 12321
rev=0
new = num
while new>0:
    id= new%10
    rev= id + (rev*10)
    new= new//10

if rev==num:
    print("Palindrome")
else:
    print("Not a Panlindrome")