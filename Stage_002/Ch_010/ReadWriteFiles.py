# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 10:36:34 2026

@author: moxey
"""

from pathlib import Path 

Path('spam', 'bacon', 'eggs')
result = str(Path('spam','bacon','eggs'))
print(result)


my_files = ['account.txt','details.csv','invite.docx']
for filename in my_files:
    print(Path(r'C:\Users\Al', filename))
    
    

# Joining Paths 
path = Path('spam') / 'bacon' / 'eggs'
print(path)
path = Path('spam') / Path('bacon/eggs')
print(path)
path = Path('spam') / Path('bacon', 'eggs')
print(path)

# 'spam' / 'bacon' - error - must be a pth object : TypeError: unsupported operand type(s) for /: 'str' and 'str' error

# Accessing the Current Working Directory 
import os 
path = Path.cwd()
print(path)
# os.chdir('C:\\Windows\\System32')
print(Path.cwd())

# Accessing the Home Directory 
path = Path.home()
print(path)

# Creating New Folders 
# os.makedirs('C:\\delicious\\walnut\\waffles')

# Path(r'C:\Users\moxey\Desktop\DevSecOps_Roadmap\Stage_002\Ch_010\spam').mkdir()

# Handling Absoulte and Relative Paths 
path = Path.cwd()
print(path)
path = Path.cwd().is_absolute()
print(path)
path = Path('spam/bacon/eggs').is_absolute()
print(path)

path = Path('my/relative/path')
print(path)
path = Path.cwd()
print(path)
path = Path.cwd() / Path('my/relative/path')
print(path)
path = Path('my/relative/path').absolute()
print(path)


# Getting the parts of a Filepath
p = Path('C:/Users/Ai/spam.txt')
print(p.anchor)
print(p.parent)
print(p.name)
print(p.stem)
print(p.suffix)
print(p.drive)
print(p.parts)
print(p.parts[3])
print(p.parts[0:2])

path = Path.cwd()
print(path)
path = Path.cwd().parents[0]
print(path)
path = Path.cwd().parents[1]
print(path)
path = Path.cwd().parents[2]
print(path)

# Finding File Size and Timestamp

from pathlib import Path

calc_file = Path('C:/Windows/System32/calc.exe')

# .stat() — gets file metadata (real method ✅)
print(calc_file.stat())
# → returns an os.stat_result object with 
#   file info (size, timestamps, permissions)

# Get specific stat fields:
print(calc_file.stat().st_size)   # file size in bytes
print(calc_file.stat().st_mtime)  # last modified time 
                             # (as a Unix timestamp)

# Convert Unix timestamp to human-readable:
import time
print(time.asctime(time.localtime(calc_file.stat().st_mtime)))


# Finding Files Using Glob Patterns 
p = Path('C:/Users/moxey/Desktop')
print(p.glob('*'))
print(list(p.glob('*')))



for name in Path('C:/Users/moxey/Desktop').glob('*'):
    print(name)
    
    
# Checking Path Validity 
win_dir = Path('C:/Windows')
not_exists_dir = Path('C:/This/Folder/Does/Not/Exist')
calc_file_path = Path('C:/Windows/System32/calc.exe')
print(win_dir.exists())
print(win_dir.is_dir())
print(not_exists_dir.exists())
print(calc_file_path.is_file())
print(calc_file_path.is_dir())

d_drive = Path('D:/')
print(d_drive.exists())


# The File Reading and Writing Process 
p = Path('spam.txt')
p.write_text('Hello, world!')
print(p.read_text())


# Opening Files 
hello_file = open(r'C:\Users\moxey\Desktop\DevSecOps_Roadmap\Stage_002\Ch_010\hello.txt', encoding='UTF-8')


# Reading the contents of the file
hello_content = hello_file.read()
print(hello_content)

sonnet_file = open(r'C:\Users\moxey\Desktop\DevSecOps_Roadmap\Stage_002\Ch_010\sonnet29.txt')
sonnet_connet = sonnet_file.readlines()
print(sonnet_connet)


# Writing to Files
bacon_file = open('bacon.txt', 'w', encoding='UTF-8')
bacon_file.write('Hello, world\n')
bacon_file.close()
bacon_file = open('bacon.txt', 'a', encoding='UTF-8')
bacon_file.write('Bacon is not a vegetable')
bacon_file.close()
bacon_file = open('bacon.txt', encoding='UTF-8')
content = bacon_file.read()
bacon_file.close()
print(content)


# Using with Statements 
file_obj = open('data.txt','w',encoding='UTF-8')
file_obj.write('Hello, world!')
file_obj.close()
file_obj = open('data.txt',encoding='UTF-8')
content = file_obj.read()
file_obj.close()
print(content)

# using statment 
with open('data.txt', 'w', encoding='UTF-8') as file_obj:
    file_obj.write('This was use with statments')
with open('data.txt', encoding='UTF-8') as file_obj:
    content = file_obj.read()
    
print(content)


# Saving Variables with the shelve Module 
import shelve 

shelf_file = shelve.open('mydata')
shelf_file['cats'] = ['Zophie','Pooka','Simon']
shelf_file.close()
shelf_file = shelve.open('mydata')
print(type(shelf_file))
print(shelf_file['cats'])
shelf_file.close()

shelf_file = shelve.open('mydata')
print(list(shelf_file.keys()))
print(list(shelf_file.values()))
shelf_file.close()