import json

data = json.load(open("smartcity-ks.json"))

f = open(".env", "w")

for key, value in data.items():
    value = value.replace("\n", "\\n")
    f.write(f'{key.upper()}="{value}"\n')
