x = 1 #bin =01
y = 2 #bin =10

print(bin(x))
print(bin(y))
# symbols for And = & Or = | Not = ~ for xor ^ for shift left << shift right >>
#AND
print(f"AND: x:{bin(x)} y:{bin(y)} = {x&y}") #01 and 10 = 00 = 0
#OR
print(f"OR: x:{bin(x)} y:{bin(y)} = {x | y}") # 01 or 10 = 11 = 3
#Not
print(f"x:{bin(x)} not x:{~x}") # x not x = 0b01 + 1 -0b10 = -2 y not y = 0b10  = -0b11 = -3
print(f"y:{bin(y)} not y:{~y}")
#XOR
print(f"x:{bin(x)} y:{bin(y)} xor: {x ^ y}") # 01 and 10 = 11 = 3
#Shift left
print(f"y:{bin(y)} shift left by 2 : {y << 2}") # shift left y = 0b1000 = 8
#Shift right
print(f"y: {bin(y)} shift right by 1: {y >> 1}") #shift right 1 y = 0b01 = 1