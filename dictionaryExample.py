customer = {
    "name": "Jhon Smith",
    "age": 30,
    "isValid": True
}
print(customer["name"])
print(customer["age"])
print(customer["isValid"])

print(customer["birthdate"])    # throw Exceptions
print(customer.get("birthdate"))    # don't throw exception
