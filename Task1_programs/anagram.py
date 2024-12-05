s1=input("Enter the first string: ")
s2=input("Enter the second string: ")
t=sorted(s1)
p=sorted(s2)
if t==p:
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")