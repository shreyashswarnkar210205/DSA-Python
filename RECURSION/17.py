def func(n):
    if n == 1:
        print(n)
        return
    print(n)
    func(n-1)

func(6)