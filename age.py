import datetime
Name = input("Please Enter Your Name : ")
Age= int(input("Enter your Age : "))
now = datetime.datetime.now()
Year=now.year
diff = 100-Age
#print (Year)
print("Your name is:",Name," \n","Your Age is:",Age,"\n","& 100th Birhtday will be :",str(diff+Year))