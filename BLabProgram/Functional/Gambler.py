import random
times=int(input("Enter the number of time you want to play "))
it=0
win=0
loss=0

while it<=times:
    total_money=int(input("Enter the total amount you have to invest"))
    goal=int(input("Enter the goal you want to touch "))
    if goal>total_money  :
        while total_money>0 and total_money<goal:
            random_value=random.uniform(0,1)
            # print("random value is      " + str(random_value))
            if random_value>=0.5:
                 total_money=total_money+1
            else:
                total_money=total_money-1
            # print("total money is    "+str(total_money))
            # print("goal is  "+str(goal))
        if total_money==goal:
            print("Win")
            win+=1
        else :
            print("loss")
            loss+=1
        it+=1
print("Total win is ::>>"+str(win))
print("Total loss is ::>"+str(loss))
print("win percentage is ::>"+str((win*100)/times))
print("Loss percentage is ::>"+str((loss*100)/times))


