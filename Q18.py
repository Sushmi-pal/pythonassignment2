import json
info={"about_me":[{"name":"Sushmita Palikhe",
      "age":22}]}
# File representation of json data
with open("info.json",'w') as f:
    json.dump(info,f,indent=2)

# String representation of json data
serialize_info=json.dumps(info,indent=2)
print('Serializing')
print(serialize_info)


print('Deserializing')
json_file = open('info.json' )
data = json.load(json_file)
print(data)
json_file.close()

deserialize_info=json.loads(serialize_info)
print(deserialize_info)