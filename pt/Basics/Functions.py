# def sum(x,y):
#     return x+y

# print(sum(4,3))

#Polymorphism -- same thing work differently.....
# def multiple(p1,p2):
#     return p1*p2

# print(multiple(5,'a'))
# print(multiple(5,4))

#Two return values............
# import math
# def circle(r):
#     area = math.pi*r **2
#     circumference = 2*math.pi*r
#     return area,circumference    
# a,c = circle(3)
# print("Area = ",a,"Circumference = ",c)

#default value.........

# def greet(name = "User"):
#     return "Hello, "+name

# print(greet("Hritik"))
# print(greet())

#Lambda function........

# cube = lambda x:x**3
# print(cube(3))

# *args..........to handle multi value arguments

# def sum_all(*args):
#     return sum(args)

# def sum_all(*args):
#     print(args)
#     for i in args:
#         print(i*2)
#     return sum(args)

# print("Sum is:",sum_all(1,2))
# print("Sum is:",sum_all(1,2,3,4,5))
# print("Sum is:",sum_all(1,2,3,4,5,6,7,8))

#**kwargs..........to handle multi values arguments in key:value format

# def print_hero(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key} : {value}")

# print_hero(name="Shaktiman",power="Lazer")
# print_hero(name="Shaktiman")
# print_hero(name="Shaktiman",power="Lazer",enemy="Doctor")

#yield.........it store value in memory during the iterations by pauses the function and save its state.

# def even_generator(limit):
#     for i in range(2,limit+1,2):
#         yield i

# for num in even_generator(10):
#     print(num)

#recursive function.............

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
    