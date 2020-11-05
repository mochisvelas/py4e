import re

print( sum( [ int(num) for num in re.findall('[0-9]+', open('/mnt/c/Users/Brenner/Downloads/regex_sum_925328.txt').read())]))
