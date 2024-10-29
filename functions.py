import math

# Q1 - Write a function that returns the square of a number

def square(x):
    return x * x
    #return x ** 2

result1 = square(2)
print(result1)

# Q2 - Write a function that takes two numbers as arguments and returns their sum

def sumOfTwo (num1,num2):
    return num1 + num2

result2 = sumOfTwo(2,3)
print(result2)

# Q3 - Write a function that multiplies two numbers but can also accept and multiply strings

def multiply (p1 , p2):
    return p1 * p2

result3 = multiply("hello ",3)
print(result3)

# Q4 - Write a function that returns both area and circumference of a circle given its radius

def circle(radius):
    area =  round(math.pi * radius ** 2,2)
    circumference = round(2 * math.pi * radius,2)

    return area , circumference

result4 = circle(5)
print(result4)

# Q5 - Write a function that greets a user , if they enter their name as an argument and if not then do it by default

def greet(name = "User"):
    greet = "Hello " + name

    return greet

result5 = greet()
print(result5)


# Q6 - Write a lambda function that returns cube of a number

cube = lambda x : x ** 3

print(cube(3))

# Q7 - Write a function with *args and **kwargs

def sumAll(*args):
    return sum(args)

result7 = sumAll(1,2,3,4,5)
print(result7)


def sumAll2(**kwargs):
    return sum(kwargs.values())

def items(**kwargs):
    for k,v in kwargs.items():
        print(k,v)

items(a=1,b=2,c=3,d=4,e=5)
result8 = sumAll2(a=1,b=2,c=3,d=4,e=5)
print(result8)

# Q8 - generator function that yields numbers

def evens(limit):
    for i in range(limit + 1):
        if i % 2 == 0:
            yield i

result8 = evens(10)
print(result8)

for num in evens(10):
    print(num)

# Q9 - Write a recursive function that returns the factorial of a number

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

result9 = factorial(5)
print(result9)





