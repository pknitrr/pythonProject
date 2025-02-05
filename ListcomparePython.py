#List Comprehension
list1 = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for i in list1:
 if "a" in i:
  newlist.append(i)
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

newlist = [x for x in fruits if x != "apple"]
print(newlist)

#Iterable
newlist = [x for x in range(10)]
print (newlist)

newlist = [x for x in range(10) if x % 2 ==0]
print(newlist)  

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)

newlist = ['hello' for x in fruits]
print(newlist)

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
