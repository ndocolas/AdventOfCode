import re

code = open(0).read()

list = re.findall(r"mul\(\d+,\d+\)",code) 

nums = [re.findall(r'\d+', text) for text in list]

t = sum(int(num[0])*int(num[1]) for num in nums)

print(t)