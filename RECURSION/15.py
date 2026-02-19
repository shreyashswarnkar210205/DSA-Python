def func(n, i=1):
    if i == n:
        print(i)
        return
    print(i)
    func(n, i+1)

func(16)