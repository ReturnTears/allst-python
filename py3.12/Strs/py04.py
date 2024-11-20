import json
json_str = '{"name":"Bob","age":18}'
py_dict = json.loads(json_str)
print(py_dict)

from xml.etree import ElementTree as ET

xml_str = "<person><name>Kang</name><age>20</age></person>"
root = ET.fromstring(xml_str)
print(root.tag)
