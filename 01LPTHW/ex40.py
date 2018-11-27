# create a dictionary with a key "apple"
# mystuff = {'apple': "I AM APPLES!"}
# print(mystuff['apple'])

# create a module
# this goes in mystuff.py
# def apple():
#     print("I AM APPLES!")

# import mystuff
# mystuff.apple()

# create another module ,put a variable in it
# def apple():
#     print("I AM APPLES!")

# this is just a viariable
# tangerine = "Living reflection of a dream"

# import mystuff

# mystuff.apple()
# print(mystuff.tangerine)

# compare the different between dictionary, module
# mystuff['apple'] # get apple from dic
# mystuff.apple() # get apple from module
# mystuff.tangerine # same thing, it's just a variable


# create a class
# class MyStuff(object):

#     def __init__(self):
#         self.tangerine = "And now a thousand years between"

#     def apple(self):
#         print("I AM CLASSY APPLES!")


# instantiate a class
# thing = MyStuff()
# thing.apple
# print(thing.tangerine)

# now I have three ways to get things from things:
# # dict style
# mystuff['apple']

# # module style
# mystuff.apple()
# print(mystuff.tangerine)

# # class style
# thing = MyStuff()
# thing.apple()
# print(thing.tangerine)

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
"I dont't want to get sued",
"So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
"With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()