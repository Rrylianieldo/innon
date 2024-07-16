import re

pattern = r'(\w)(\s\d)'
text = 'A 5'

match = re.search(pattern, text)
if match:
    group1 = match.group(1)  # 'A'
    group2 = match.group(2)  # ' 5'
    print(group1, group2)
