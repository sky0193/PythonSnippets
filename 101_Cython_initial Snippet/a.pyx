cdef int _fib(int n):
    cdef int i
    cdef int a=0, b=1
    for i in range(n):
        a, b = a + b,a
    return a

def fib(n):
    return _fib(n)
