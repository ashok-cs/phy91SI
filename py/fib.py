def fib(n):    
    if n<1: 
        print("Invalid argument")
    elif n==1:
        return 0
    elif n==2:
        return 1
    
    a,b = 0,1
    
    for i in range(2,n):
        a,b=b,a+b
    return b

def phi_approx(n):
    f_n=fib(n)
    f_p=fib(n-1)
    φ=f_n/f_p
    print(n,f_n,f_p,"%.4f"%φ)    
    return
    