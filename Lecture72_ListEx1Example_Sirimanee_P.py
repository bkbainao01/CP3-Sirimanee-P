def showBill():
    total = 0
    print("My Food".center(20, " "))
    for i in range(len(menuList)):
        print(menuList[i][0]+" : ",menuList[i][1])
        total = total+ menuList[i][1]
    print("Total: %d" % total)

menuList = []


while True:
    menuName = input("Please Enter Menu: ")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = int(input("Price: "))
        menuList.append([menuName,menuPrice])

showBill()



