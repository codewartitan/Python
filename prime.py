num1=int(input("Enter a Number: "))
#num2 = num1*1
for i in range(1,num1):
    if (num1%i)==0:
        print("It is not a prime number")
        print(i,"Is divisible by ",num1//i,"is",num1)
else:
    print("It is  a prime number")