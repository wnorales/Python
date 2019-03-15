# Comments in Python are marked by the start of #
midpoint = 5

lower = []
upper = []

for i in range(10):
    if i < midpoint:
        lower.append(i)
    else:
        upper.append(i)
print(upper)
print(lower)
# In Python, code blocks are denoted by indentation:
# In Python, indented code blocks are always preceded by a colon (:) on the previous line.
# In Python you need to be careful after every : you need to pull back the statement

x = 5
if x < 4:
    y = x * 2
print(x)

if x < 4:
    y = x * 2
print(x)