def fib(n):
    print("fib(", n ,")->",end="")
    if n==0:
        print("0")
        return 0
    if n==1:
        print("1")
        return 1
    print("fib(%d) + fib(%d)"%(n-1,n-2))
    return fib(n-1)+fib(n-2)
fib(5)
