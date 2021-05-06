import random
list1 = ["s","w","g"]
usernumber = 0
comouternumber = 0
chance = 10
while(1):
    computerchose = random.choice(list1)
    desgiene = input("Enter You Opction for Snake s, Water w, Gun g : ")
    if not(computerchose==desgiene):
        if(computerchose=="s" and desgiene=="w"):
            comouternumber +=1
        elif(computerchose=="w" and desgiene=="s"):
            usernumber +=1
        elif(computerchose=="g" and desgiene=="s"):
            comouternumber +=1
        elif(computerchose=="s" and desgiene=="g"):
            usernumber += 1
        elif(computerchose=="w" and desgiene=="g"):
            comouternumber +=1
        elif(computerchose=="g" and desgiene=="w"):
            usernumber += 1
        else:
            print("Plese Enter Right option")
            chance +=1
        chance -=1
        print(f"You Have Remaing chance {chance} into 10")
    else:
        print("Your and computer same answer round is tie ")
    if(chance==0):
        print(f"Your Game is End You Score is {usernumber} And Computer Score is {comouternumber}")
        nextgame = input("You Run This Game again [y/n] : ")
        if(nextgame=="y" or nextgame=="Y"):
            chance=10
        elif(nextgame=="n" or nextgame=="N"):
            break
        else:
            print("You Enter Wrong Answer So Game Is Out")
            break