# Boolean Value 
spam = True 
print(spam)

# Comparison Operators 
print(42 == 42)
print(42 == 99)
print(2 != 3)
print(2 != 2)
print('hello' == 'hello')
print('hello' == 'Hello')
print('dog' != 'cat')
print(True == True)
print(True != False)
print(42 == 42.0)
print(42 == '42')
print(42 < 100)
print(42 > 100) 
print( 42 < 42)
eggs = 42
print(eggs <= 42)
my_age = 29
print(my_age >= 10)

# Boolean Operators 
print(True and True)
print(True and False)
print(False or True)
print(False or False)

print(not True) # evaluates to the opposite boolean value 
print(not not not not True)

# Mixing Boolean and Comparison Operators 
print((4 < 5) and ( 5 < 6 ))
print((4 < 5) and (9 < 6))
print((1 ==2) or( 2 == 2) )

spam = 4 
print( 
       2 + 2 == spam and not 2 + 2 == (spam + 1) and 2 * 2 == 2+ 2
      
      
      
      )

# Components of Flow Control
name = 'Marc'
age = 11
if name == 'Alice':
    print('Hi, Alice')
elif age <  12:
    print('You are not Alice, kiddo')
#else:
    #print('Hello, stranger')
    

spam = 2
if spam == 1:
    print('Hello')
elif spam == 2: 
    print('Howdy')
else:
    print('Greetings')