age = 36
txt = "My name is John, I am ", age
print(txt)
print("My name is John, I am ", age)

x = 'Welcome'
print(x[3])

#Use the len function to print the length of the string.
x = "Hello World"
print(len(x))

x = 'Welcome'
print(x[3:5])

x = 'Welcome'
print(x[3:])

txt = " Hello World "
x= txt.strip()
print(x)

#Replace the character H with a J.
txt = "Hello World"
txt = txt.replace("H","J")
print(txt)

#If x = 9, what is a correct syntax to print 'The price is 9.00 dollars'?
x=9
print(f'The price is {x:.2f} dollars')

age = 36
txt = f"My name is John, and I am {age}"
print(txt)

print(f'The price is {2 + 3} dollars')
