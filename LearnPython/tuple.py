# Tuple - array - ()
# we cant delete attend data
tuple1 = ("python","java","php",".Net")
print(tuple1)
print(tuple1[2])
# tuple1[0] = "C" #not work
print(tuple1)

for x in tuple1:
    print(x)

# delete possible
# del tuple1
# print(tuple1)  #error

tuple2 = (1,2,3,4)
tuple3 = tuple1 + tuple2
print(tuple3)
print(tuple3[4])