# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 07:30:28 2026

@author: moxey
"""
# Read CSV Files
import csv
example_file = open('C:/Users/moxey/Desktop/DevSecOps_Roadmap/Stage_002/Ch_018/example3.csv')
example_reader = csv.reader(example_file)
example_data = list(example_reader)
print(example_data)
print(example_data[0][0]) # First Row, first column
print(example_data[0][1]) # First row, first column
print(example_data[0][2]) # First Row, third column
print(example_data[1][1]) # Second row, second column
print(example_data[6][1]) # Seventh row, second column
example_file.close()


# Accessing Data in a for loop

example_file = open('C:/Users/moxey/Desktop/DevSecOps_Roadmap/Stage_002/Ch_018/example3.csv')
example_reader = csv.reader(example_file)

for row in example_reader:
    print('Row #' + str(example_reader.line_num) + ' ' + str(row))
example_file.close()


# Writing CSV Files 
output_file = open('C:/Users/moxey/Desktop/DevSecOps_Roadmap/Stage_002/Ch_018/output.csv', 'w', newline='')
output_writer = csv.writer(output_file)
output_writer.writerow(['spam','eggs','bacon', 'ham'])
output_writer.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
output_writer.writerow([1,2,3.141592,4])
output_file.close()


# Using Tab Instead of commas 
output_file = open('output.tsv', 'w', newline='')
output_writer = csv.writer(output_file, delimiter='\t', lineterminator='\n\n')
output_writer.writerow(['spam','eggs','bacon','ham'])
output_writer.writerow(['Hello, world!', 'eggs','bacon','ham'])
output_writer.writerow([1,2,3.141592,4])
output_file.close()


# Handling Header Row
example_file = open('C:/Users/moxey/Desktop/DevSecOps_Roadmap/Stage_002/Ch_018/exampleWithHeader3.csv')
example_dict_reader = csv.DictReader(example_file)
example_dict_data = list(example_dict_reader)
print(example_dict_data)


example_file = open('C:/Users/moxey/Desktop/DevSecOps_Roadmap/Stage_002/Ch_018/exampleWithHeader3.csv')
example_dict_data =  csv.DictReader(example_file)
for row in example_dict_reader:
    print(row['Timestamp'], row['Fruit'], row['Quantity'])
example_file.close()

example_file = open('C:/Users/moxey/Desktop/DevSecOps_Roadmap/Stage_002/Ch_018/example3.csv')
example_dict_reader = csv.DictReader(example_file, ['time', 'name', 'amount'])
for row in example_dict_reader:
    print(row['time'], row['name'], row['amount'])
example_file.close()

output_file = open('output2.csv', 'w', newline='')
output_dict_writer = csv.DictWriter(output_file,['Name', 'Pet', 'Phone'])
output_dict_writer.writeheader()
output_dict_writer.writerow({'Name': 'Alice', 'Pet': 'cat', 'Phone': '555-1234'})
output_dict_writer.writerow({'Name': 'Bob','Phone': '555-9999'})
output_dict_writer.writerow({'Phone': '555-5555', 'Name': 'Carol', 'Pet': 'dog'})
output_file.close()

# Versatile Plaintext Formats 

# Reading JSON Data
import json
json_string = '{"name": "Alice Doe", "age": 30, "car": null, "programmer":true, "address": {"street": "100 Larkin St.", "city": "San Francisco", "zip": "94102"}, "phone": [{"type": "mobile", "number": "415-555-7890"},{"type": "work", "number": "415-555-1234"}]}'
python_data = json.loads(json_string)
print(python_data)

# Writing JSON Data
json_string = json.dumps(python_data, indent=2)
print(json_string)


# XML

# Reading XML Files 
import xml.etree.ElementTree as ET

xml_string = """<person>
<name>Alice Doe</name>
<age>30</age>
<programmer>true</programmer>
<car xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>
<address>
    <street>100 Larkin St.</street>
    <city>San Francisco</city>
    <zip>94102</zip>
</address>
<phone>
    <phoneEntry>
        <type>mobile</type>
        <number>415-555-7890</number>
    </phoneEntry>
    <phoneEntry>
        <type>work</type>
        <number>415-555-1234</number>
    </phoneEntry>
</phone>
</person>"""

root = ET.fromstring(xml_string)
print(root)
print(root.tag)
print(list(root))

print(root[0].tag)
print(root[0].text)
print(root[3].tag)
print(root[3].text == None)
print(root[4].tag)
print(root[4][0].tag)
print(root[4][0].text)

for elem in root:
    print(elem.tag, '--', elem.text)
    


for elem in root.iter():
    print(elem.tag, '--', elem.text)
    
    
for elem in root.iter('number'):
    print(elem.tag, '--', elem.text)
    
    

import xmltodict 
xml_string = """<person>
<name>Alice Doe</name>
<age>30</age>
<programmer>true</programmer>
<car xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>
<address>
    <street>100 Larkin St.</street>
    <city>San Francisco</city>
    <zip>94102</zip>
</address>
<phone>
    <phoneEntry>
        <type>mobile</type>
        <number>415-555-7890</number>
    </phoneEntry>
    <phoneEntry>
        <type>work</type>
        <number>415-555-1234</number>
    </phoneEntry>
</phone>
</person>"""

python_data = xmltodict.parse(xml_string)
print(python_data)

# Writing XML Files
person = ET.Element('person') # Create the root XML elemnet 
name = ET.SubElement(person, 'name') # Create <name> and put it under <person>
name.text = 'Alice Doe' # Set the text between <name> and </name>
age = ET.SubElement(person, 'age')
age.text = '30' # XML content is always a string
programmer = ET.SubElement(person, 'programer')
programmer.text = 'true'
car = ET.SubElement(person, 'car')
car.set('xsi:nil', 'true')
car.set('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
address = ET.SubElement(person, 'address')
street = ET.SubElement(address, 'street')
street.text = '100 Larkin St.'
result = ET.tostring(person, encoding='UTF-8')
print(result)