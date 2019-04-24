input=int(input("Enter four digit year "))
digit=0
n=input
while n>0:
    n=int(n/10)
    digit+=1
if digit==4 and input%400==0 or input%4==0 and input%100!=0:
    print(str(input)+ "This is a leap year")
else:
    print("The value is not the leap year or you have entered wrong input digit ")

