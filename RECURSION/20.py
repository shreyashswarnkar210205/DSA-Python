def func(n):
    if n==1:
        return 1
    return n + func(n-1)

print(func(3))

#Time Complexity -> O(n)
#Space Complexity -> O(n)