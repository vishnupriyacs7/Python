# dictionary
# ===============
# key value {}
dict1 = {
    "name":"vishnu",
    "email":"vishnu@gmail.com",
    "phone":123456
}
print(dict1)
print(dict1["phone"])
a = dict1.get("email")
print(a)
dict1["name"] = "priya"
print(dict1)
for x in dict1:
    print(x)
    print(dict1[x])
for x,y in dict1.items():
    print(x,y)

# length
print(len(dict1))
dict1["age"] = 30
print(dict1)

dict1.pop("phone")
print(dict1)

del dict1["email"]
print(dict1)

dict1.clear()
print(dict1)

del dict1
print(dict1)
