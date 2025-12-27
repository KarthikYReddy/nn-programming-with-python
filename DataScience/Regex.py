import re
regex_sentense = "I love to eat pizza and pasta 3 times a day"
print(re.findall(r"a.d", regex_sentense))
print(re.findall(r"pi.*ta",regex_sentense))
print(re.findall(r"lo.+at",regex_sentense))
print(re.findall(r"piz?za",regex_sentense))

print(re.findall(r"\d",regex_sentense))
print(re.findall(r"\W",regex_sentense))
print(re.findall(r"pizza\sand\spasta",regex_sentense))
print(re.findall(r"\D",regex_sentense))
print(re.findall(r"\W",regex_sentense))
print(re.findall(r"\S",regex_sentense))

pattern="((pizza)|(pasta))"
matches=re.findall(pattern,regex_sentense)
print("captured words : ",matches)

