def func(n, i=1):
    if i == n:
        print(i)
        return
    func(n, i+1)
    print(i)

func(6)