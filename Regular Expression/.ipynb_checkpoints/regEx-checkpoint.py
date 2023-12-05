import re

txt = "The Rain in spain 007"

pattern = re.compile("^The")
matchResult = pattern.match(txt)

# print(matchResult)
print(re.findall('[a-zA-Z]|[0-9][0-9][0-9]',txt))