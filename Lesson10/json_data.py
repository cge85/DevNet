import json

with open("json_file.json") as data:
    json_read = data.read()

json_dict = json.loads(json_read)
json_dict ["name"] = "cliff"
json_dict ["age"] = "27"
del(json_dict["car"])
json_dict ["iam"] = "The best coder and smartest man in the universe"

with open("json_file.json", "w") as data:
    json.dump(json_dict, data, indent = 4)