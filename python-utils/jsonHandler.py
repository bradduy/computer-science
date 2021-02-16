import json

user = {
    "name": "Duy",
    "age": 18,
    "nation": "Vietnam",
    "hasChildren": False
}
##### Convert object as string ##########################
userJSON = json.dumps(user, indent=4, sort_keys=True)
print(type(userJSON))

##### Save object as json ############################
with open('user.json', 'w') as file:
    json.dump(user, file, indent=4)


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


##############################################
##### Encode JSON - 1st method ###############
duy = User('Duy', 21)
def encodeUser(obj):
    if isinstance(obj, User):
        return {
            "name": obj.name,
            "age": obj.age,
            obj.__class__.__name__: True
        }
    else:
        raise TypeError("Object of type User is not JSON serializable")

duyJSON = json.dumps(duy, default=encodeUser)
print(duyJSON)


##############################################
##### Encode JSON - 2nd method ###############
from json import JSONEncoder

class UserEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, User):
            return {
                "name": obj.name,
                "age": obj.age,
                obj.__class__.__name__: True
            }
        return JSONEncoder.default(self, obj)

duyJSON = json.dumps(duy, cls=UserEncoder)
duyJSON = UserEncoder().encode(duy)
print(duyJSON)


##############################################
##### Decode JSON ############################

def decodeUser(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct

result = json.loads(duyJSON, object_hook=decodeUser)
print(type(result))
print(f'The {result} consists of {result.name} and {result.age}')
    