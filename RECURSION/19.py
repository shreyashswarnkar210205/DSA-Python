def func(n, sum=0, i=1):
    if i>n:
        print(sum)
        return
    func(n, sum+i, i+1)

func(5)