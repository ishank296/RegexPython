import re
from typing import Pattern

pattern_01 = re.compile("^[A-Z]+$")      # matches string that contains only one or more uppercase letters
pattern_02 = re.compile("[A-Z]+")        # matches any string that contains atleast one uppercase letters
pattern_03 = re.compile(r"^[A-Za-z\s]+$") # matches any string that contains uppercase/lowercase letters
                                          # and space characters

# search method look for patter all over string whereas match method only checks the start of string



print("###Using re search method ##")
print(pattern_01.search("HELLO WORLD"))
print(pattern_01.search("hello world"))
print(pattern_01.search("HELLOWORLD"))
print(pattern_02.search("hello WORLD"))


print("\n##Using re match method##")
print(pattern_01.match("HELLO WORLD"))
print(pattern_01.match("hello world"))
print(pattern_01.match("HELLOWORLD"))
print(pattern_02.match("hello WORLD"))


print(pattern_03.search("hello world"))
print(pattern_03.search("Hello World"))


# 3 lowercase letters
# 3-5 digits
# one symbol
# upto to two uppercase characters (optional)

pattern_04 = re.compile("^[a-z]{3}[1-9]{3,5}[^a-zA-Z0-9]{1}[A-Z]{0,2}$")


# match any string with length of 10
pattern_05 = re.compile("^.{10}$")

print(pattern_05.search("0123456789"))
print(pattern_05.search("abcdefghij"))
print(pattern_05.search("a white lo"))


# validating emails
pattern_06 = re.compile("^[a-zA-Z0-9\._]+[@]{1}[a-zA-Z0-9]+\.{1}[a-zA-Z]{2,3}$")
print(pattern_06.match("mail@gmail.com"))
print(pattern_06.match("mymail@test.com"))
print(pattern_06.match("fancy_mail@xyz.co"))