from tkinter import *
import  math

def leftClickButton(event):
    result = float(weightTextbox.get())/math.pow((float(heightTextbox.get())/100),2)
    if result > 30:
        resultLb.configure(text="อ้วนมาก /โรคอ้วนระดับ 3")
    elif 25 <= result <= 29.90:
        resultLb.configure(text="อ้วน / โรคอ้วนระดับ 2")
    elif 23 <= result <= 24.90:
        resultLb.configure(text="อ้วน / โรคอ้วนระดับ 1")
    elif 18.50 <= result <= 22.90:
        resultLb.configure(text="ปกติ / สุขภาพดี")
    else:
        resultLb.configure(text="น้ำหนักน้อย / ผอม")

def doubleClickButton(event):
    print("Double Click !!!")

mainWindow = Tk()
heightLb = Label(mainWindow,text="ส่วนสูง (cm.)").grid(row=1,column=0)
heightTextbox = Entry(mainWindow)
heightTextbox.grid(row=1,column=1)
weightLb = Label(mainWindow,text="น้ำหนัก (kg.)").grid(row=2,column=0)
weightTextbox = Entry(mainWindow)
weightTextbox.grid(row=2,column=1)
calculateBt = Button(mainWindow,text="คำนวณ")
calculateBt.bind("<Button-1>",leftClickButton)
calculateBt.grid(row=3,column=0)
resultLb = Label(mainWindow,text="ผลลัพธ์")
resultLb.grid(row=3,column=1)
mainWindow.mainloop()