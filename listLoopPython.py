#rename the file
#Loop Through a List : by using a for loop
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#Loop Through the Index Numbers: Use the range() and len() functions 
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

#Using a While Loop
thsilist = [1,2,3,4,5]
i=0
while i<len(thislist):
 print(thislist[i])
 i = i+1

#Looping Using List Comprehension
thislist = [11,12,13,14]
[print(y) for y in thsilist]

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
