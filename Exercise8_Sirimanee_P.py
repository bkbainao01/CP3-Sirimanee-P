username = input("Username: ")
password = input("Password: ")
if username.__eq__("admin") and password.__eq__("nimda"):
    print(" Log in Successful !")
    print("--------------feberk09 Shop------------")
    print("1. Electric Monthly Calculation ")
    print("2. Water Monthly Calculation ")
    print("3. Vat Calculation")
    print("4. Price Calculation")
    print("---------------------------------------")
    selMenu = input("Select Menu :")
    if selMenu == '1':
        print("Electrical Monthly Calculation Program")
        energyUse = int(input("Electric Unit : "))
        if energyUse <= 150:
            energyCharge = 2.35
            serviceCharge = 8.19
            ft = 0
            vat = 7 / 100
        else:
            energyCharge = 3.25
            serviceCharge = 38.22
            vat = 7 / 100
            ft = 0

        baseTariff = (energyUse * energyCharge) + serviceCharge
        ftCharge = energyUse * ft
        tax = baseTariff * vat
        total = baseTariff + tax
        print("---------------------------------------")
        print("         Electrical Monthly Bill")
        print(" Used Energy           : ", energyUse)
        print(" Energy Charge         : ", energyCharge)
        print(" Service Charge        : ", serviceCharge)
        print(" Ft Rate               : ", ft)
        print(" Base Tariff           : ", baseTariff)
        print(" Ft Charge             : ", ftCharge)
        print(" Tax 7%                : ", tax)
        print(" Total Electric Charge : ", tax)
        print("---------------------------------------")
    elif selMenu == '2':
        print("Water Monthly Calculation Program ")
        waterUnit = int(input("Used Water : "))
        if 80 < waterUnit <= 90:
            waterPrice = 12.5
        elif 70 < waterUnit <= 80:
            waterPrice = 11.33
        elif 60 < waterUnit <= 70:
            waterPrice = 11.00
        elif 50 < waterUnit <= 60:
            waterPrice = 10.68
        elif 40 < waterUnit <= 50:
            waterPrice = 10.68
        elif 30 < waterUnit <= 40:
            waterPrice = 10.35
        else:
            waterPrice = 8.5
        service = 3
        vat = 7 / 100
        tax = ((waterUnit * waterPrice) + service) * vat
        total = ((waterUnit * waterPrice) + service) + tax
        print("---------------------------------------")
        print("         Water Monthly Bill")
        print(" Used Water (Unit)     : ", waterUnit)
        print(" Water Price / Unit    : ", waterPrice)
        print(" Tax 7%                : ", '%.2f' % tax) #กำหนดให้แสดงผลแค่ทศนิยม 2 ตำแหน่ง
        print(" Total Electric Charge : ", total)
        print("---------------------------------------")
    elif selMenu == '3':
        print("Vat Calculation Program")
        price = int(input("Price : "))
        vat = 7/100
        tax = price * vat
        total = price+tax
        print("Total : " ,total)
    elif selMenu == '4':
        print("Price Calculation Program ")
        product1 = float(input("Price Product 1 : "))
        quantity1 = int(input("Quantity of Product 1 : "))
        product2 = float(input("Price Product 2 : "))
        quantity2 = int(input("Quantity of Product 2 : "))
        print("Total : ",(product1*quantity1)+(product2*quantity2))
    else:
        print("Error!!")




