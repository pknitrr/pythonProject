x1 = "Hello World"	#str	
print("x1 is" , type(x1), "and value is", x1 )

x2 = 20	#int
print("x2 is" , type(x2), "and value is", x2 )

x3 = 20.5	#float
print("x3 is" , type(x3), "and value is", x3 )

x4 = 1j	#complex
print("x4 is" , type(x4), "and value is", x4 )

x5 = ["apple", "banana", "cherry"]	#list	
print("x5 is" , type(x5), "and value is", x5 )

x6 = ("apple", "banana", "cherry")	#tuple
print("x6 is" , type(x6) , "and value is", x6)

x7 = range(6)	#range	
print("x7 is" , type(x7) , "and value is", x7)

x8 = {"name" : "John", "age" : 36}	#dict
print("x8 is" , type(x8), "and value is", x8 )

x9 = {"apple", "banana", "cherry"}	#set	
print("x9 is" , type(x9 ), "and value is", x9)

x10 = frozenset({"apple", "banana", "cherry"})	#frozenset
print("x10 is" , type(x10), "and value is", x10 )

x11 = True	#bool	
print("x11 is" , type(x11), "and value is", x11 )

x12 = b"Hello"	#bytes	
print("x12 is" , type(x12), "and value is", x12 )

x13 = bytearray(5)	#bytearray	
print("x13 is" , type(x13), "and value is", x13 )

x14 = memoryview(bytes(5))	#memoryview	
print("x14 is" , type(x14), "and value is", x14)

x15 = None           #NoneType
print("x15 is" , type(x15), "and value is", x15 )
