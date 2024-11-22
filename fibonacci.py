def fibonacci(n):
    fib = [0, 1]  # Initialize the Fibonacci sequence list with the first two values
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])  # Calculate the next Fibonacci number and add it to the list

    return fib

n = 10  # Specify the number of Fibonacci numbers to generate
fib_sequence = fibonacci(n)
print(fib_sequence)