# set - {}
# unordered and unindexed

set1 = {"java","python","php",".Net"}
print(set1) #random print
# print(set1[0]) #error
for x in set1:
    print(x)
    print("php" in set1) #true - present
    print("laravel" in set1) #false - not present

#add
set1.add("flutter")
print(set1)
set1.update(["c","cpp","ruby"]) #multiple
print(set1)

#remove
set1.remove("c")
print(set1)
set1.discard("cpp")
print(set1)
set1.discard("c#")
print(set1)
# set1.remove("c#")
print(set1)