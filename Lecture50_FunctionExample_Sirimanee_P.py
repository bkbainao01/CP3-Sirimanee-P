def addNumber(x,y):
    print(x, "+", y, "=", x + y)
    print(x, "-", y, "=", x - y)
    print(x, "*", y, "=", x * y)
    #การกำหนดให้แสดงทศนิยม 2 ตำแหน่ง
    print(x, "/", y, "=", '%.2f'%(x / y))


addNumber(int(input("Number 1: ")), int(input("Number 2: ")))



