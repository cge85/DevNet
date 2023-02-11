import xmltodict

with open("xml_data.xml") as data:
    xml_example = data.read()

xml_dict = xmltodict.parse(xml_example)
print(xmltodict.unparse(xml_dict, pretty=True))