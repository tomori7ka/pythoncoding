a = [1, 2, 3, ["a", "b", "c", ["A", "B"]]]
print(a[3])

b = [3, ["ㄱ", ["A", "B", "C"], "ㄴ", "ㄷ"], 2, 1, 0]

# ㄷ 을 출력
print(b[1][3])
# B 를 출력
print(b[1][1][1])

a = [1, 2, 3, 4, 5]
print(a[0:2])
b = [4, 5, 6]
print(a + b)

a = [1, 2, 3]
a[2] = 4
print(a)

del a[1]
print(a)

