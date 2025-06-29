# Arithmetic - Addition, subtraction, multiplication , division , modulus
# ========================================================================
a = 100
b = 20
c = a + b
print(c)

c = a - b
print(c)

c = a * b
print(c)

c = a / b
print(c)

c = a % b
print(c)

# exponentiation
c = 2 ** 5
print(c)

# floor divider (w/o decimal)
a = 10
b = 3
c = a // b
print(c)

# Assignment Opertaors
#=======================
# assignment =  x= 10
x = 10
#  +=   x +=4 --> x = x + 4
x += 4
print(x)

#  -=   x -=4 --> x = x - 4
x -= 4
print(x)

#  *=   x *=4 --> x = x * 4
x *= 4
print(x)

#  /=   x /=4 --> x = x / 4
x /= 4
print(x)

#  %=   x %=4 --> x = x % 4
x %= 4
print(x)

#  //=   x //=4 --> x = x // 4
x //= 4
print(x)

#  **=   x **=4 --> x = x ** 4
x **= 4
print(x)

# Comparison Operators - ==, !=, >,<, >=,<=
# ===========================================
a = 10
b = 20
print (a == b) #equal to
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# Logical operators - and, or, not
# =================================
a = 10
print(a ==10 and a < 5)
print(a ==100 or a < 5)
print(not(a==100) )
