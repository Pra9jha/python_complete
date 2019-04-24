n=int(input("Enter the value of n up to which harmonic number is to be printed"))
value=0
dis=""
for i in range(1,n+1):
    value=value+1/i
    dis=dis+" 1/"+str(i)+ "+"
print(dis[0:len(dis)-1]+" ="+str(value))