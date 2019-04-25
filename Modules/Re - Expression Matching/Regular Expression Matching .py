import re
# This is used for pattern Matching

# Import the regex module with import re.

# Create a Regex object with the re.compile() function. (Remember to use a raw string.)

# Pass the string you want to search into the Regex object’s search() method. This returns a Match object.

# Call the Match object’s group() method to return a string of the actual matched text.

PhoneNumbers = ['917-231-4287', '631-639-9604', '718-474-6892', '552-987-5014']

phoneNumRgex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
for n in PhoneNumbers:
  mo = phoneNumRgex.search(n)
  print('Phone number found: ' + mo.group())

print("\n")

AreaCode = ['347', '516', '917', '718', '631', '8102', '9625', '814']
AreaCodeRGEX = re.compile(r'\d\d\d')
for m in AreaCode:
 so = AreaCodeRGEX.search(m)
 print('Area code found:' + so.group())

 """Grouping with Parentheses"""
 """https://automatetheboringstuff.com/chapter7/"""

regularRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = regularRegex.search('My number is 415-555-4242.')
print(mo.group(1))