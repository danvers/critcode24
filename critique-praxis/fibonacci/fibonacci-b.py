# In mathematics, the Fibonacci sequence is a sequence in which each number is the sum of the two preceding ones. 
# Numbers that are part of the Fibonacci sequence are known as Fibonacci numbers, commonly denoted Fn .
# Many writers begin the sequence with 0 and 1, although some authors start it from 1 and some (as did Fibonacci) 
# from 1 and 2. Starting from 0 and 1, the sequence begins
# 
# see more at: https://en.wikipedia.org/wiki/Fibonacci_sequence
# 

def fibonacci(n, num1=0, num2=1, count=1):
    if count > n:
        return
    print(num2, end=" ")
    fibonacci(n, num2, num1 + num2, count + 1)

# Example usage:
n = 10
fibonacci(n)