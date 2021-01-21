

def fibonacci():
    a,n=0,1
    while True:
        a,n = n,n+a
        yield n

fib_ = fibonacci()
while True:
    print(next(fib_))

        
    