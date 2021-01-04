

def fib(n):
    a = 0
    b = 1
    li = []
    for i in range(n):
        li.append(a)
        temp = a
        a = b
        b = temp + a
    return li;


li = fib(20)
print(li)