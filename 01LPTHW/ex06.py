# define a variable
types_of_people = 10
# make a string
x = f"There are {types_of_people} types of people."

# define a variable
binary = "binary"
do_not = "don't"
# make a string
y = f"Those who know {binary} and those who {do_not}."

# print string
print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = "False"
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))
# 没看懂上面这个命令

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)