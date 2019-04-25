import re

heroRegex = re.compile(r'Norales|Tina Fey|Batman')
mo1 = heroRegex.search('Batman,Tina Fey,Norales ')
print(mo1.group())

mo2 = heroRegex.search('Tina Fey and Batman.')
print(mo2.group())

