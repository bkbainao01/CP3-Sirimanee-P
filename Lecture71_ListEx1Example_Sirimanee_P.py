def showBill():
    total = 0
    print("My Food".center(20, " "))
    for i in range(len(menuList)):
        print(menuList[i], priceList[i])
        total = total+ priceList[i]
    print("Total: %d" % total)

menuList = []
priceList = []
while True:
    menuName = input("Please Enter Menu: ")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = int(input("Price: "))
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()



