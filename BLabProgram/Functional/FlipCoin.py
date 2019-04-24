import  random
# random.randrange(2,7,3),random.shuffle([1,2,3,4,5,6]),random.choice(3,4,5),random.uniform(0,1)
input=int(input("Enter the number of time we want to toss the coin "))
h=0
t = 0
for i in range(input):
    outcome=random.uniform(0,1)
    print("%.2f" % outcome)
    if outcome<=0.5:
     h+=1
     print("head")
    else:
      t+=1
      print("Tail")
print("% of head is "+str((h*100)/input))
print("% of tail is "+ str((t*100)/input))
