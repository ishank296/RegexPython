import re

# \A restricts the match to the start of string
# \Z restricts the match to the end of string
# re.fullmatch() ensures pattern matches the entire input string
# \b restricts the match to the start and end of words
# \B matches wherever \b doesn't match
# ^	 restricts the match to the start of line
# $	 restricts the match to the end of line

# 1. check if the given strings start with be.

line1 = 'be nice'
line2 = '"best!"'
line3 = 'better?'
line4 = 'oh no\nbear spotted'

pat = re.compile(r'^be')
print(bool(re.search(pat,line1)))
print(bool(re.search(pat,line2)))
print(bool(re.search(pat,line3)))
print(bool(re.search(pat,line4)))


# 2. For the given input string, change only the whole word red to brown.
words = 'bred red spread credible red.'
res = re.sub(r'\bred\b', 'brown', words)
print(res)

# 3. For the given input list, filter all elements that contain 42 surrounded by word characters.
words = ['hi42bye', 'nice1423', 'bad42', 'cool_42a', '42fake', '_42_']
print([w for w in words if re.search(r'\B42\B',w)])

# 4. For the given input list, filter all elements that start with den or end with ly.
items = ['lovely', '1\ndentist', '2 lonely', 'eden', 'fly\n', 'dent']
print([e for e in items if re.search(r'\Aden|ly\Z',e)])

# 5. For the given input string, change whole word mall to 1234 only if it is at the start of a line.
para = '''
(mall) call ball pall
ball fall wall tall
mall call ball pall
wall mall ball fall
mallet wallet malls
mall:call:ball:pall'''

print(re.sub(r'^mall\b', '1234', para,flags=re.M))


# 6. For the given list, filter all elements having a line starting with den or ending with ly
items = ['lovely', '1\ndentist', '2 lonely', 'eden', 'fly\nfar', 'dent']
print([w for w in items if re.search(r'^den|ly$',w,re.M)])