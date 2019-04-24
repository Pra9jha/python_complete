import math

def prime_check(value):
    print("value is "+str(value))
    for i in range(2,int(math.sqrt(number))+1):
        if value%i==0:
            return False
    return True

number=int(input("Enter the number "))
primefactor=[]
i=0
while prime_check(number)==False:
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            number = int(number / i)
            print("number is "+str(number), end="   ")
            print("primefactor is "+str(i))
            primefactor.append(i)
            break
primefactor.append(number)
print(primefactor)