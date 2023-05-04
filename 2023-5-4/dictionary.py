a = {"name": "pey", "phone": "01199903323", "birth": "1118"}

del a["name"]
print(a)

grade = {"pey": 10, "julliet": 99}
print(grade["julliet"])

a = {1: "a", 1: "b"}
print(a)

a = {"name": "pey", "phone": "01199903323", "birth": "1118"}
print(a.values())
print(a.keys())
print(a.items())
a.clear()
print(a)

a = {"name": "pey", "phone": "01199903323", "birth": "1118"}
print(a.get("name"))

print("name" in a)
print("email" in a)

b = {"name": "홍길동", "age": "30", "birth": "1128"}

