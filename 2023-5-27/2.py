a = 80 + 75 + 55
print(a / 3)


pin = "881120-1068234"
print(pin[7:8])


a = "a:b:c:d"
b = a.replace(":", "#")
print(b)

a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

pin = "881120-1068234"
yyyymmdd = pin[0:6]
num = pin[7:14]
print(yyyymmdd)
print(num)


a = ["Life", "is", "too", "short"]
result = " ".join(a)
print(result)

a = (1, 2, 3)
b = (4,)
print(a + b)


a = {"A": 90, "B": 80, "C": 70}
result = a.pop("B")
print(a)
print(result)
