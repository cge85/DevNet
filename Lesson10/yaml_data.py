import yaml

with open("yaml_sample.yaml") as data:
    yaml_sample = data.read()

yaml_dict = yaml.load(yaml_sample, Loader=yaml.FullLoader)
yaml_dict ["interface"] ["name"] = "GigabitEthernet1/28"
yaml_dict ["interface"] ["duplex"] = "Full"
print(yaml_dict, )

with open("yaml_sample.yaml", "w") as data:
    data.write(yaml.dump(yaml_dict, default_flow_style=False))

