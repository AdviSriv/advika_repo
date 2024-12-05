num= input("Enter the number: ")
l= len(num)
for i in range(0,l):
    if num[i]>num[i+1]:
        break
peak_index= i
print("The peak value is at index: ")
print(peak_index)

for i in range(peak_index,l-1):
    if num[i]<num[i+1]:
        break

if i==l-2:
    print("It is a hill number.")
else:
    print("Not a hill number.")