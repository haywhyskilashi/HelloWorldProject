import time

firstname = "bro"
Secondname = 'Folorunsho'
fullname = firstname + ' ' + Secondname
print("Hello " + fullname)

age = 21
age = age + 1
print(age)
print("Your age is " + str(age))

height = 250.05
print("your height is " + str(height) + "cm")

human = True
print("Are you a human? " + str(human))

name = "ayluayeo"
print(name.replace('a', 'b'))

x = 1
y = 2.0
z = "3"

print("X is " + str(x))
print("Y is " + str(y))
print("Z is " + z)

name = input("what is your name?")
age = int(input('How old are you'))
height = float(input('How tall are you? '))
age = (age) + 1

print('Hello ' + name + ',' + ' ' + 'Good afternoon')
print('You will be  ' + str(age) + 'yrs old' + ' ' + 'next year')
print('You are ' + ' ' + str(height) + 'cm' + " " + 'tall')

pi = -3.14

# Slicing and indexing
# SLICING = creating a substring by extracting elements from another
# string===== [start : stop : step]

# INDEXING
name = 'Ayo Oluwa'
first_name = name[0:3]
last_name = name[4:9]
funky_name = name[0:9:3]
reversed_name = name[::-2]

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

# REMOVE AND CREATING A SUBSTRING using slice() function

website1 = "http://facebook.com"
website2 = "http://wikipedia.com"

slice1 = slice(7, 15)  # counting from left to right
slice2 = slice(7, -4)  # counting from right to left, it is in negative

print(website1[slice1])
print(website2[slice2])

# If statements
age1 = int(input("How old are you?"))

if age1 >= 18:
    print("Youre eligible")
elif age1 == 1000:
    print("Youre immortal")
else:
    print("Youre not eligible")

# logical operators (and, or, not)

temperature = int(input("What is the temperature outside?"))

# and = both conditions must be true
if temperature >= 0 and temperature <= 30:
    print("The temperature outside is good today. " + " " + "Todays Temperature is " + " " + str(temperature))
    print("You can go outside")

# or = one of the condition have to be true
elif temperature <= 0 or temperature >= 30:
    print("The temperature today is bad. Stay inside " + " " + str(temperature))
    print("Stay inside")
else:
    print("Your temperature is " + " " + str(temperature))

# Not = used to check if two or more conditionals statement is true
# flips a conditional statement to FALSE if it is TRUE, and flips to TRUE if it is FALSE

# while loops = statement will execute its code as long as
#               condition remains true

name = ""

while len(name) == 0:
    name = input("Enter your name")

print("Hello " + name)

# FOR LOOP = a statement that will execute its block of a
#              limited amount of times

for i in range(50, 101, 20):
    print(i)

for j in "Bro code":
    print(j)

for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1)
print("Happy new year")

# nested loop= having inner loop
# rows = outer loop
# columns = inner loop

rows = int(input("How many rows? "))
columns = int(input("How many columns"))
symbols = input("Enter a symbol: ")

for r in range(rows):
    for c in range(columns):
        print(symbols, end="")
    print()

# loop control statement = used to change loop execution from
#         normal sequence
#   break, continue and pass
# break = used to terminate the loop entirely
# continue = skips to the next iteration of the loop
# pass = does nothing, acts as a placeholder

# break
while True:
    name = input("Enter your name: ")
    if name != "":
        break

# contiune
phone_number = "123-456-7890"

for p in phone_number:
    if p == "-":
        continue
    print(p, end="")

# pass
for i in range(1, 21):
    if i == 13:
        pass
    else:
        print(i)

# list = used to store multiple item in a single variable

food = ["pizza", "hamburger", "hotdog", "spagetti"]

food[0] = "sushi"

# food.sort
# food.count()
# food.append()
# food.clear()
for y in food:
    print(y)

# 2D list = list of lists

drinks = ["coffee","soda","tea"]
dinner = ["pizza","hamburger","hotdog"]
dessert = ["cake", "ice cream"]

food = [drinks,dinner,dessert]

print(food[2][0])


# tuple = collection which is ordered and unchangable
#           used to group together related data

student = ("bro", 21, "male")
# print(student.index("male")

for d in student:
    print(d)

if "bro" in student:
    print("Bro is here!")

# set = collection which is unordered and unindex. No duplicate values

