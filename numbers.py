# printing the prime digits in the given number
def print_prime_digits(number):
    prime_digits={"2","3","5","7"}
    number_str=str(number)
    print("prime digits in the given number:")
    for digit in number_str:
        if digit in prime_digits:
            print(digit)
    print()
number=23456784
print_prime_digits(number)

#armstrong number program
num=int(input("enter any number:"))
order=len(str(num))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum=sum+digit**order
    temp//=10
if sum==num:
    print(num,"armstrong number")
else:
    print (num,"not armstrong number")


#type: ignore
