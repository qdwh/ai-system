Write a Python function that calculates the factorial of a number. Test the function using the numbers 5, 7, and 10.

<jupyter_code>
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
print(factorial(7))
print(factorial(10))
<jupyter_output>
120
5040
3628800
<jupyter_text>
Exercise 3: Write a Python function that calculates the Fibonacci sequence up to a given number. Test the function using the number 10.
<jupyter_code>
def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

print(fibonacci(10))
<jupyter_output>
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
<jupyter_text>
Exercise 4: Write a Python function that checks if a number is a prime number. Test the function using the numbers 5, 7, and 10.
<jupyter_code>
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while