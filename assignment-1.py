#Section 1: Variables and Types 
name = "Mosi"
age = 47
height = 6.2
is_student = True

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))

#Section 2: User Input and Math

name = input("What's your name? ")
birth_year = input("What year were you born? ")
birth_year = int(birth_year)
age = (2026 - birth_year)
print (f"Hi, {name}! you are approximately {age} years old.")

#Section 3: Type conversion and f-strings

number_1 = input("Please enter a number. ")
number_2 = input("Please enter another number. ")
number_1 = float(number_1)
number_2 = float(number_2)
answer = number_1 * number_2

print(f"{number_1} x {number_2} = {answer}")

#Section 4: Formatted receipt


item = "Organic whole cashews"
price = 16.99
quantity = 2
total = price * quantity

print()
print("====================")
print()
print("RECEIPT")
print()
print("====================")
print()
print(f"Item: {item}")
print()
print(f"Price: ${price}")
print()
print(f"Quantity: {quantity}")
print()
print("-------------------")
print(f"Total: ${total}")
print()
print("====================")

#Section 5: 

name = input("What's your name? ")
hometown = input("What's your hometown? ")
hobby = input("What's your favorite hobby? ")
fun_fact = input("What's a fun fact about yourself? ")
birth_year = input("What year were you born? ")
birth_year = int(birth_year)
age = 2026 - birth_year

print()
print("<<<<<<<<<<>>>>>>>>>>")
print()
print(f"PROFILE: {name}")
print()
print("<<<<<<<<<<>>>>>>>>>>")
print()
print(f"Hometown: {hometown}")
print()
print(f"Hobby: {hobby}")
print()
print(f"Fun Fact: {fun_fact}")
print()
print(f"Age: {age}")
