dictionary=[{"name": "John", "age": 30}, {"name": "Jane", "age": 25}, {"name": "Doe","age": 40}]

dictionary.sort(key=lambda x:x["age"])

print(dictionary)