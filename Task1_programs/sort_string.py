s = input("Enter the string: ")

list = []
l = len(s)
for i in range(0, l):
    list.append(s[i])

for i in range(0, l):
    for j in range(0, l):
        if list[i] < list[j]:
            list[i], list[j] = list[j], list[i]
j = ""

for i in range(0, l):
    j = j + list[i]

print(j)