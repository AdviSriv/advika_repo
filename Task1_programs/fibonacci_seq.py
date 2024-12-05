n=int(input("Enter the number of elements in the series: "))
num1=0
num2=1
i=1
res=0
print(res,end=' ')
while i<=n:
    res=num1+num2
    print(res, end=' ')
    num1,num2=num2,res
    i=i+1


