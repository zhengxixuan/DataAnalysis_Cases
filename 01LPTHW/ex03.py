# what to do ?
print("I will now count my chickens:")

# learn count
print("Hens", 25 +30 / 6)
print("Roosters", 100 - 25 * 3 % 4)

print("Now I will count the eggs:")

print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

print("Is it true that 3 + 2 < 5 - 7?")

print(3 + 2 < 5 - 7)

print("What is 3 + 2?", 3 + 2)
print("What is 5 - 7?", 5 - 7)

print("Oh, that's why it's False.")

print("How about some more.")

print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)

# 为什么运行结果，母鸡数字是30.0，而公鸡数是97？同样计算，一个是浮点数，一个不是浮点数？

# 使用浮点数重写
print("I will now count my chickens:")

print("Hens", 25.0 +30.0 / 6.0)
print("Roosters", 100.0 - 25.0 * 3.0 % 4.0)

print("Now I will count the eggs:")

print(3.0 + 2.0 + 1.0 - 5.0 + 4.0 % 2.0 - 1.0 / 4.0 + 6.0)

print("Is it true that 3 + 2 < 5 - 7?")

print(3.0 + 2.0 < 5.0 - 7.0)

print("What is 3 + 2?", 3 + 2)
print("What is 5 - 7?", 5 - 7)

print("Oh, that's why it's False.")

print("How about some more.")

print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)
# 运行结果，母鸡数字是30.0，而公鸡数是97.0，为什么两次不一样？
# 因为十进制小数不能精确的表示为二进制小数。
# 计算母鸡时，30/6 二进制有小数，所以加总之后是有小数的，故体现为30.0
# 计算公鸡时，一直都是整数，所以是97