##This was made while learning from FreeCodeCamp Tutotrial
##This is little In-efficient. Will Create my own Cal with improved logic

from tkinter import *

root= Tk()

root.title("Simple Calculator with Tkinter")

#Text Field Widget
num=Entry(root,width=40,borderwidth=10)
num.grid(row=0,column=0,columnspan=3, padx=15, pady=30)

#Functions for Cal:
#To read data/nums on buttons:
def button_click(number):
    exp = num.get()
    num.delete(0,END)
    num.insert(0, str(exp)+str(number))
    return

##Function  for ADD Button '+'
def button_add():
    f_num=num.get()
    global first_num
    global math
    math = "add"
    first_num=int(f_num)
    num.delete(0,END)

##Function for SUB Button '-'
def button_sub():
    f_num=num.get()
    global first_num
    global math
    math = "sub"
    first_num=int(f_num)
    num.delete(0,END)


##Function for MULTI Button  '*'
def button_multi():
    f_num=num.get()
    global first_num
    global math
    math = "multi"
    first_num=int(f_num)
    num.delete(0,END)


## Function for DIV Button '/'
def button_div():
    f_num=num.get()
    global first_num
    global math
    math = "div"
    first_num=int(f_num)
    num.delete(0,END)
    

##Equal Button '='
def button_eql():
    second_num = num.get()
    num.delete(0,END)

    if math == 'add':
        num.insert(0, first_num+int(second_num))

    if math == 'sub':
        num.insert(0, first_num-int(second_num))

    if math == 'multi':
        num.insert(0, first_num*int(second_num))

    if math == 'div':
        num.insert(0, first_num/int(second_num))

##Clear button
def button_clr():
    num.delete(0,END)

##Creating Buttons:
butt_0 = Button(root, text='0', padx=40,pady=20,command=lambda:button_click(0))
butt_1 = Button(root, text='1',  padx=40,pady=20,command=lambda:button_click(1))
butt_2 = Button(root, text='2', padx=40,pady=20,command=lambda:button_click(2))
butt_3 = Button(root, text='3', padx=40,pady=20,command=lambda:button_click(3))
butt_4 = Button(root, text='4', padx=40,pady=20,command=lambda:button_click(4))
butt_5 = Button(root, text='5', padx=40,pady=20,command=lambda:button_click(5))
butt_6 = Button(root, text='6', padx=40,pady=20,command=lambda:button_click(6))
butt_7 = Button(root, text='7', padx=40,pady=20,command=lambda:button_click(7))
butt_8 = Button(root, text='8', padx=40,pady=20,command=lambda:button_click(8))
butt_9 = Button(root, text='9', padx=40,pady=20,command=lambda:button_click(9))

butt_add = Button(root, text='+', padx=39, pady=20, command=button_add)
butt_sub = Button(root, text='-', padx=41, pady=20, command=button_sub)
butt_multi= Button(root, text='*', padx=41, pady=20, command=button_multi)
butt_div= Button(root, text='/', padx=41, pady=20, command=button_div)

butt_eql = Button(root, text='=', padx=88, pady=20, command=button_eql)
butt_clr = Button(root, text='CLEAR', padx=74, pady=20, command=button_clr)


##def creat_butt():
##    for i in range(0,10):
##        butt_i = Button(root, text=i, padx=40,pady=20,command=lambda:button_click(i))
##
##creat_butt()

#Putting the Buttons on Screen on proper posistion
butt_1.grid(row=3,column=0)
butt_2.grid(row=3,column=1)
butt_3.grid(row=3,column=2)

butt_4.grid(row=2,column=0)
butt_5.grid(row=2,column=1)
butt_6.grid(row=2,column=2)

butt_7.grid(row=1,column=0)
butt_8.grid(row=1,column=1)
butt_9.grid(row=1,column=2)

butt_0.grid(row=4,column=0)

butt_add.grid(row=5, column=0)
butt_sub.grid(row=6, column=0)
butt_multi.grid(row=4, column=1)
butt_div.grid(row=4, column=2)

butt_eql.grid(row=5, column=1, columnspan=2)
butt_clr.grid(row=6 , column=1, columnspan=2)

#For continous looping
root.mainloop()
