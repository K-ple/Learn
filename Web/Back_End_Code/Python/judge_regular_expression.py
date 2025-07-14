import re

url = input()

pattern = r'^(http|https)://[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+/[a-zA-Z0-9-_/?.=]*$'
match = re.match(pattern, url)
print(match is not None)
