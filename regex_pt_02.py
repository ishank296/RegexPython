# Metacharacters
import re

# .  - Any character except a newline
# \d - Any digit [0-9]
# \D - Not a digit
# \w - Word Character [a-zA-Z0-9_]
# \W - Not a word
# \s - Whitespace
# \S - Not a Whitespace

# \b - Word boundary
# \B - Not a word boundary
# ^  - start of a string
# $  - end of a string


# pattern to match phone numbers e.g. 645-235-060
re.compile("^\d\d\d-\d\d\d-\d\d\d$")
re.compile("^[0-9]{3}\-[0-9]{3}\-[0-9]{3}$")


# pattern to match all phone number starting with 800 or 900
re.compile("^[89]00\-[0-9]{3}\-[0-9]{3}")

# pattern to match any word that starts with any character except `b` and ends with `at`
re.compile("[^b]at")