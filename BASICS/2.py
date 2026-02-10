from math import log10
num = int(input("Enter a number: "))
count = 0
while num>0:
    count+=1
    num=num//10
print("Total Digits ", count)

# Time complexity is O(log10 n), this means that the number from which we are dividing comes in the base of log if we divided it with 2 then the Time Complexity would have been O(log2 n)
# Space Complexity is O(1) as there are constatnt number of variables and there is increse in number of variables