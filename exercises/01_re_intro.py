# 1. Check whether the given strings contain 0xB0. Display a boolean result

import re

line1 = 'start address: 0xA0, func1 address: 0xC0'
line2 = 'end address: 0xFF, func2 address: 0xB0'

print(bool(re.search(r'0xB0', line1)))
print(bool(re.search(r'0xB0', line2)))

# 2. replace all occurrences of 5 with five for the given string.
ip = 'They ate 5 apples and 5 oranges'
print(re.sub('5', 'five', ip))

# 3. Replace only the first occurrence of 5 with five for the given string.
print(re.sub('5', 'five', ip, 1))

# 4. For the given list, filter all elements that do not contain e.
items = ['goal', 'new', 'user', 'sit', 'eat', 'dinner']
res = [w for w in items if not re.search(r'e', w)]
print(res)

# 5. Replace all occurrences of note irrespective of case with X
ip = 'This note should not be NoTeD'
print(re.sub('note', 'X', ip, flags=re.IGNORECASE))

# 6. For the given input string, display all lines not containing start irrespective of case.
para = '''good start
 Start working on that
 project you always wanted
 stars are shining brightly
 hi there
 start and try to
 finish the book
 bye'''

pat = re.compile('start',re.IGNORECASE)
for line in para.split('\n'):
    if not pat.search(line):
        print(line)

# 7. For the given list, filter all elements that contain either a or w.
items = ['goal', 'new', 'user', 'sit', 'eat', 'dinner']
res = [w for w in items if re.search(r'[aw]',w)]
print(res)

# 8. For the given list, filter all elements that contain both e and n.
items = ['goal', 'new', 'user', 'sit', 'eat', 'dinner']
res = [w for w in items if re.search('e',w) and re.search('n',w)]
print(res)

# 9. For the given string, replace 0xA0 with 0x7F and 0xC0 with 0x1F.
ip = 'start address: 0xA0, func1 address: 0xC0'
res = re.sub('0x7F','0x1F',re.sub('0xA0','0x7F',ip))
print(res)