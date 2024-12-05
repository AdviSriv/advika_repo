card_no=input("Enter a credit card no: ")
card_no=card_no.replace(" ","")
card_no=card_no.replace("-","")
card_no=card_no[::-1]

odd_dig_sum=0
even_dig_sum=0

for i in card_no[::2]:
    odd_dig_sum+= int(i)

for i in card_no[1::2]:
    i=int(i)*2
    if i>=10:
        even_dig_sum+=(1+(int(i)%10))
    else:
        even_dig_sum+=int(i)

total=even_dig_sum+odd_dig_sum

if total%10==0:
    print("Valid card number.")
else:
    print("Invalid card number.")


