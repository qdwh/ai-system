Write a Python function that calculates the factorial of a number.

<jupyter_code>
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
<jupyter_output>
120
<jupyter_text>
Write a Python function that checks whether a passed string is palindrome or not.
<jupyter_code>
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome('madam'))
<jupyter_output>
True
<jupyter_text>
Write a Python program to find the sum of all elements in a list using recursion.
<jupyter_code>
def sum_list(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[0] + sum_list(lst[1:])

print(sum_list([1, 2, 3, 4, 5]))
<jupyter_output>
15
<jupyter_text>
Write a Python program to find the maximum number in a list using recursion.
<jupyter_code>
def max_in_list(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        max_rest = max_in_list(lst[1:])
        return max_rest if max_rest > lst[0] else lst[0]

print(max_in_list([1, 3, 5, 7,