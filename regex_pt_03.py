import re


string = """ 
 This is simple-example. hyphens can occur anywhere
 in a sentence.
"""

string_2 = """
 A few unexpected words are to be expected
"""

pattern_01 = "\w+-?\w+"  # match any word with or without hyphen
pattern_02 = "\w+-\w+"   # match any word containing one hyphen
pattern_03 = "\w{3}"     # match any word with length of 3 characters
pattern_04 = "\w{3,5}"   # match any workd with length between 3 to 4 characters

# capture group
# treat everything within bracket () as single unit
pattern_05 = "(?:un)?expected"

# character sets
pattern_06 = "[a-zA-Z\-]"


# boundaries
pattern_07 = r"\b\w+"

# look ahead\behind assertions
# match string based on preceded/succeded by given pattern
string_3 = "1: hello world, 2: hello world"
pattern_08 = "(?<=1: )hello world"
pattern_09 = "hello world(?=,)"

# modifiers
# m - multiline. ^ and $ match start/end of line
# i - case in-sensitive match
# s - single line match
string_4 = """This is single line match character
 second line example"""

pattern_10 = "character."
pattern_11 = "(?s)character"

# condition group
# (condition)?(?(1) world| bye)



print(re.findall(pattern_01,string))
print(re.findall(pattern_02,string))
print(re.findall(pattern_03,string))
print(re.findall(pattern_04,string))
print(re.findall(pattern_05,string_2))
print(re.findall(pattern_07,string))
print(re.findall(pattern_08,string_3))
print(re.findall(pattern_09,string_3))
print(re.findall(pattern_10,string_4))
print(re.findall(pattern_11,string_4))

