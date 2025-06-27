#age = int(input("Enter age : "))
#day = "Wednesday"
# if age < 13:
#     print("Child")
# elif age < 20:
#     print("Teenager")
# elif age < 60:
#     print("Adult")
# else:
#     print("Senior")

# price = 12 if age >= 18 else 8
# if day == "Wednesday":
#     price = price - 2

# print(f"Your ticket price is ${price}")    

# score = int(input("Enter your Score: "))

# if score > 101:
#     print("Enter valid score....!!")
#     exit()
# if score >=90:
#     print("Grade A")
# elif score >=80:
#     print("Grade B")
# elif score >=70:
#     print("Grade C")
# elif score >=60:
#     print("Grade D")
# else:
#     print("Grade F")    

# fruit = input("Enter fruit: ")
# color = input("Enter color of fruit: ")
# if fruit == "banana":
#     if color == "Green":
#        print("Unripe")
#     elif color == "Yellow":
#        print("Ripe")
#     elif color == "Brown":
#        print("Overripe")
#     else:
#        print("Enter valid color....!!!")

# password = input("Enter password: ")
# size = len(password)

# if size < 6:
#     print("Weak")
# elif size <10:
#     print("Medium")
# else:
#     print("Strong")

yr = int(input("Enter the year: "))

if (yr%4 == 0) or (yr%100 ==0 and yr%400==0):
    print("Year is leap year...")
else:
    print("Not...")