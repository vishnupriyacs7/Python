# collection datatypes - list, tuple, set, dictionary
# 1. List
#=============
a = "Hello" #normal
list1 = ["hii","hello","nice"]
print(list1)
print(len(list1))
print(list1[0]) #hii
list2 = [10,20,30,40]
sum = list2[1] + list2[2]
print(sum)

#change list value
list1[0] = "python"
print(list1)
#loop
for x in list1:
    print(x)
#append
list1.append("java") #append @ last
print(list1)
list1.insert(2,"php") #add by index num
print(list1)

#remove
list1.remove("hello")
print(list1)

#clear - delete all
list1.clear()
print(list1)

#to delete completely
del list1
print(list1)
