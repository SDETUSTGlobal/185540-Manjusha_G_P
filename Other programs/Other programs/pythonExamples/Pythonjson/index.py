import json
x = {"name": "John", "age": 30, "city": "New York"}
print(json.dumps(x))
print(json.dumps(x, separators=(". ", " = ")))
print(json.dumps(x, indent=4, separators=(" . ", " = ")))
print(json.dumps(x, indent=4, sort_keys=True))