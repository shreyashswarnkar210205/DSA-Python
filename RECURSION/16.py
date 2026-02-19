def func(n):
    if n == 1:
        print(n)
        return
    func(n-1)
    print(n)

func(5)