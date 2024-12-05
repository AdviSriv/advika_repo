s=input("Enter a string: ")
l=list(s)
n=len(l)
for i in range(0,n):
    min=i
    for j in range(i+1,n):
        if l[j]<l[min]:
          min=j
    l[i],l[min]=l[min],l[i]
s=''.join(l)
print("sorted string: ")
print(s)



