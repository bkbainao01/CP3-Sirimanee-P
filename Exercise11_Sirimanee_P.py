'''
    *
   ***
  *****
 *******
*********
'''
i=0
while(i!= 1):
    num = int(input())
    for x in range(num):
        print(" "*(num-x)+"*"*(x*2+1))
    i= int(input("Play Again (Yes=1/No=0): "))


