# use '', ""
# """ quotes for multiline """
text = """
I love python 
i want to learn 
and started learning
"""

print(text)
msg = "Hello"
print(msg[1]) #index number
print(msg[1:4]) #print as a sequence eg: ell 1 to 4 , 4 excluded
print(len(msg)) #length of string
print("  Hello World  ".strip()) #remove white space
print(msg.lower()) #lowercase
print(msg.upper()) # uppercase
print(msg.replace("l","k")) #character replace

a = "learn"
b = "python"
c = a + " " + b #merging
print(c)

name = "Abhjith"
age = 30
text = "my name is {}, i am {} years old "
print(text.format(name,age)) #replace variables using format to placeholders
