f1 = 0
f2 = 1
fib = [f1,f2]
def fibonacci(n):
    for i in range(2,n):
        fib.append(fib[i-1] + fib[i-2]) 
    return fib    
n = 5        
print(fibonacci(n))        

