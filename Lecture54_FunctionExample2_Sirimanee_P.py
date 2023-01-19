'''
 วิธีแรกในการสร้างฟังก์ชันคือ ดูภาพรวมก่อน
 ดูองค์ประกอบทั้งหมด อย่าเพิ่งเขียนทั้งหมดในทีเดียว เพื่อให้เราจะได้จัดลำดับความคิดได้
'''
def login():
    count = 0
    allCount = 4
    while True:
        username = input("Username : ")
        password = input("Password : ")
        if username.__eq__("admin") and password.__eq__("1234"):
            while True:
                showMenu()
                menuSelected()
                if input("You want to continue program ?? (Y/N) :") != 'y':
                    exit(0)
        else:
            count += 1
            allCount-=1
            print("Wrong username or password!!!")
            print("You can input wrong username or password wrong only "+str(allCount)+" time")
            print("Program will shutdown")

            if count > 3:
                exit(1)
def showMenu():
    print("----------iShop-----------")
    print("1. Vat Calculator ")
    print("2. Price Calculator")
    print("3. Exit Program")
    print("--------------------------")
def menuSelected():
        userSelected = input(">> ")
        if  userSelected == '1':
            return vatCalculate(int(input("Price (THB) : ")))
        elif userSelected == '2':
            return priceCalculate()
        elif userSelected == '3':
            exit(0)
        else:
            return "Wrong menu !!!"
def vatCalculate(total):
    try:
        vat = 7 / 100
        result = total + (total * vat)
        print("Total : ", result)
        return result
    except ValueError as e:
        print("That's not valid number! ",e)
        exit(1)
def priceCalculate():
    if True:
        try:
            price1 = int(input("Product1 Price : "))
            price2 = int(input("Product2 Price : "))
        except ValueError as e:
            print("That's not valid number! ",e)
            exit(1)
    return vatCalculate(price1+price2)

# Call Function
print(login())

