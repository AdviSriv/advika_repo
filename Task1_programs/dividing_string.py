def div_string(string,num):
    l=len(string)
    if l%num!=0:
        print("The division cannot be made.")
        return
    part_size = l / num
    k = 0
    for i in string:
        if k % part_size == 0:
            print()
        print(i, end='')
        k += 1


s="abcdabcdabcdabcd"
n= int(input("Enter the number of divisions: "))
div_string(s,n)
