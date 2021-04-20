import json
from string import ascii_uppercase, digits


# Словарь с ключами длиной < 6
data2 = json.load(open("dictionary.json"))
data_cleand2 = json.load(open("dictionary.json"))

for i in data2.keys():
    if len(i.split()) > 1 or i[0] in ascii_uppercase or i[0] in digits:
        data_cleand2.pop(i)

short_words = data_cleand2
keys_short = []

for i in data_cleand2.keys():
    if len(i) >= 6:
        keys_short.append(i)
for x in keys_short:
    short_words.pop(x)
# Словарь с ключами длиной 5-9

data3 = json.load(open("dictionary.json"))
data_cleand3 = json.load(open("dictionary.json"))

for i in data3.keys():
    if len(i.split()) > 1 or i[0] in ascii_uppercase or i[0] in digits:
        data_cleand3.pop(i)

medium_words = data_cleand3
keys_medium = []

for i in data_cleand3.keys():
    if 5 < len(i) <= 9:
        keys_medium.append(i)
for x in keys_medium:
    medium_words.pop(x)

# Словарь с ключами длиной >9
data4 = json.load(open("dictionary.json"))
data_cleand4 = json.load(open("dictionary.json"))

for i in data4.keys():
    if len(i.split()) > 1 or i[0] in ascii_uppercase or i[0] in digits:
        data_cleand4.pop(i)

long_words = data_cleand4
keys_long = []

for i in data_cleand4.keys():
    if len(i) <= 9:
        keys_long.append(i)
for x in keys_long:
    long_words.pop(x)
