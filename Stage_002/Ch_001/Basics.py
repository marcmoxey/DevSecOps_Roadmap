print(2 + 2)
print(2 )
print(2 + 3 * 6 )
print((2 + 3) * 6)
print(2 ** 8)
print(23 / 7)
print(23 // 7 )
print(2                +                         2)
print((5 - 1) * ((7 + 1) / (3 - 1)))

# The Integer, Floating-Point, and String Data Types 

#print('hello, world!) error - unterminated string literal
print('Alice' + 'Bob')
#print('Alice' + 5) error - TypeError: can only concatenate str (not "int") to str : use str() to turn 5 to a string  print('Alice' + str(5))
print('Alice' * 5)
#print('Alice' * 'Bob')  error - TypeError: can't multiply sequence by non-int of type 'str'
#print('Alice' * 5.0) error - TypeError: can't multiply sequence by non-int of type 'float'

# Storing Values in Variables

spam = 40 
print(spam)
eggs = 2 
print(spam + eggs)
print(spam + eggs + spam)
spam = spam + 2
print(spam)
spam = 'hello'
print(spam)
spam = 'Goodbye'
print(spam)



# my_name = input("What is your name?: ")
# print(my_name)

# The len() function 
print(len('hello'))
print(len('My very energetic monster just scarfed nachos'))
print(len(''))

#print('I am' + 25 + ' years old') # error - TypeError: can only concatenate str (not "int") to str

# The str(), int() and float functions
print(str(29))
print('I am ' + str(29) + ' years old' )
print(str(0))
print(str(-3.14))
print(int('42'))
print(int('99'))
print(int(1.25))
print(int(1.99))
print(float('3.14'))
print(float(10))
spam = input('>')
spam = int(spam)
print(spam)
spam = spam * 10 / 5
print(spam)
print(int(7.7))
print(int(7.7) + 1)

print(42 == '42') # false
print(42 == 42.0) # true
print(42.0 == 0042.000) # true

# The type function 
print(type(42))
print(type(42.0))
print(type('forty two'))
name = 'Zophie'
print(type(name))
print(type(len(name)))


# The round() and abs() Functions
print(round(3.14))
print(round(7.7))
print(round(2.2))
print(round(3.14, 1))
print(round(7.777777,3))
print(abs(25))
print(abs(-25))
print(abs(-3.14))
print(abs(0))