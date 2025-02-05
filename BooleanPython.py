x =15
y=0
print(bool(x)) #true
print(bool(y)) #false
str1 = "Hello" 
str2 = "" 
print(bool(str1)) #true
print(bool(str2)) #false

print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))
print(bool([])) 

print(bool(("apple", "cherry", "banana")))
print(bool(())) 

#these should return false
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#Functions can Return a Boolean
def myFunction() :
  return True
print(myFunction())

#Print "YES!" if the function returns True, otherwise print "NO!":
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

#Check if an object is an integer or not:
x = 200
print(isinstance(x, int))

