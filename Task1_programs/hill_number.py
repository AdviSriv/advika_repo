num = input("Enter the number: ")
l = len(num)

peak_index = 0
for i in range(1, l):
    if num[i] > num[peak_index]:
        peak_index = i
        
for i in range(1, peak_index):
    if num[i] <= num[i - 1]:
        print("Not a hill number.")
        break
else:
    for i in range(peak_index + 1, l):
        if num[i] >= num[i - 1]:
            print("Not a hill number.")
            break
    else:
        print("It is a hill number.")
