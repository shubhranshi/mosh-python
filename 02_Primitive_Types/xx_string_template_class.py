# In the String module, Template Class allows us to create simplified syntax for output specification.
# The format uses placeholder names formed by $ with valid Python identifiers (alphanumeric characters
# and underscores).

# Example 1
# A Simple Python template example
from string import Template

# Create a template that has placeholder for value of x
t = Template('x is $x')

# Substitute value of x in above template
print(t.substitute({'x' : 1}))      # x is 1


# Example 2
# List Student stores the name and marks of three students
Student = [('Ram',90), ('Ankit',78), ('Bob',92)]

# We are creating a basic structure to print the name and # marks of the students.
t = Template('Hi $name, you have got $marks marks')

for i in Student:
    print(t.substitute(name = i[0], marks = i[1]))

# Output
# Hi Ram, you have got 90 marks
# Hi Ankit, you have got 78 marks
# Hi Bob, you have got 92 marks


# Example 3
template = Template('$name is the $job of $company')
string = template.safe_substitute(name='Raju Kumar', job='TCE')
print(string)   # Raju Kumar is the TCE of $company


# Example 4
t = Template('I am $name from $city')
print('Template String =', t.template)      # Template String = I am $name from $city


# Example 5
# The $$ can be used to escape $ and treat as part of the string.
template = Template('$$ is the symbol for $name')
string = template.substitute(name='Dollar')
print(string)       # $ is the symbol for Dollar


# Example 6
# The ${Identifier} works similar to that of $Identifier. It comes in handy when valid identifier characters
# follow the placeholder but are not part of the placeholder.
template = Template( 'That $noun looks ${noun}y')
string = template.substitute(noun='Fish')
print(string)       # That Fish looks Fishy






