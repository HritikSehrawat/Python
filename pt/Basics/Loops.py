
#positive count.....
# numbers = [1,-2,3,-4,5,6,-7,-8,9,10]
# positive_count = 0

# for num in numbers:
#     if num>0:
#         positive_count +=1
# print("Total positive numbers: ",positive_count)

#sum of even numbers....
#n = int(input("Enter value of n: "))
# sum = 0
# for i in range(1,n+1):
#     if i%2==0:
#         sum = sum + i
# print("Sum of even values: ",sum)

#table....
# for i in range(1,n+1):
#     if i==5:
#         continue
#     else:
#      print(f"{n} * {i} = {n*i}")

#Reversed string.....
# str = input("Enter string: ")
# rev_str = ""

# for char in str:
#     rev_str = char + rev_str
# print("Reversed string: ",rev_str)

#first non repetive character.....  
# str = input("Enter string: ")

# for i in str:
#     if str.count(i) == 1:
#         print("First non repetive character is: ",i)
#         break

#factorial.....
n=int(input("Enter value of n: "))
# temp = n
# f=1
# for i in range(1,n+1):
#     f = f*i
# print(f"(Factorial of {n}is: {f}")

# while(temp>0):
#     f=f*temp
#     temp = temp-1
# print(f"Factorial of {n} is: {f}")

#Prime.....
# is_prime = True
# for i in range(2,n):
#     if n%i == 0:
#         print("Not prime....")
#         is_prime = False
# print(n,"is prime")

items = ["apple","banana","orange","apple","strawberry"]

unique_item = set()
for item in items:
    if item in unique_item:
        print("Duplicate item is: ",item)
    else:
        unique_item.add(item)