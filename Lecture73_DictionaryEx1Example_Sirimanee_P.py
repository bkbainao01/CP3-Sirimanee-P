def showBill():
    total = 0
    print("-".center(50,"-"))
    print("Feberk09 Restaurant Bill".center(50, "-"))
    for i in range(len(menuList)):
        print(menuList[i][0] + " : ", menuList[i][1], " THB")
        total = total + menuList[i][1]
    print("-".center(50, "-"))
    print("Total: %d" % total+" THB")
    print("-".center(50, "-"))

print("Feberk09 Restaurant".center(50,"-"))
print("*** Instruction : Enter your menu ")
print("and if you don't want to add then enter 'exit' ")
menuList = []
systemMenu = {"hamburger": 50, "fried rice": 50, "american fried rice": 56, "pork steak": 100, "dolly fish steak": 90}
while True:
    menuName = input("Please Enter Menu: ").lower()
    if (menuName == "exit"):
        break
    else:
        # print(systemMenu.get(menuName)) #can get value from key
        # print(systemMenu[menuName])     #can get value from key
        if menuName in systemMenu.keys():
            menuList.append([menuName, systemMenu[menuName]])
        else:
            print("My restaurant doesn't have this menu!!")
            print("Try Again!!!")

showBill()
