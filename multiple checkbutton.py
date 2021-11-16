from tkinter import *
from tkinter.ttk import Combobox
   
def resett():
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)
    e8.delete(0,END)
    e9.delete(0,END)
    e10.delete(0,END)
    e11.delete(0,END)
    e12.delete(0,END)
    e13.delete(0,END)
    e14.delete(0,END)
    e15.delete(0,END)
    e16.delete(0,END)
    e17.delete(0,END)
    e18.delete(0,END)
    e19.delete(0,END)
    e20.delete(0,END)
    e21.delete(0,END)
    e22.delete(0,END)
    e23.delete(0,END)
    e24.delete(0,END)
    e25.delete(0,END)
    sub_entry.delete(0,END)
    total_entry.delete(0,END)

    

var=Tk()

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=IntVar()
var23=IntVar()
var24=IntVar()
var25=IntVar()

t1=IntVar()
t2=IntVar()
t3=IntVar()
t4=IntVar()
t5=IntVar()
t6=IntVar()
t7=IntVar()
t8=IntVar()
t9=IntVar()
t10=IntVar()
t11=IntVar()
t12=IntVar()
t13=IntVar()
t14=IntVar()
t15=IntVar()
t16=IntVar()
t17=IntVar()
t18=IntVar()
t19=IntVar()
t20=IntVar()
t21=IntVar()
t22=IntVar()
t23=IntVar()
t24=IntVar()
t25=IntVar()

i=IntVar()

def pay():
    choise1=int(t1.get())
    print(choise1)
    choise2=float(t2.get())
    choise3=float(t3.get())
    choise4=float(t4.get())
    choise5=float(t5.get())
    choise6=float(t6.get())
    choise7=float(t7.get())
    choise8=float(t8.get())
    choise9=float(t9.get())
    choise10=float(t10.get())
    choise11=float(t11.get())
    choise12=float(t12.get())
    choise13=float(t13.get())
    choise14=float(t14.get())
    choise15=float(t15.get())
    choise16=float(t16.get())
    choise17=float(t17.get())
    choise18=float(t18.get())
    choise19=float(t19.get())
    choise20=float(t20.get())
    choise21=float(t21.get())
    choise22=float(t22.get())
    choise23=float(t23.get())
    choise24=float(t24.get())
    choise25=float(t25.get())

    total1=50*choise1+80*choise2+90*choise3+70*choise4+120*choise5+100*choise6
    total2=50*choise7+50*choise8+60*choise9+70*choise10+30*choise11
    total3=50*choise12+50*choise13+60*choise14+70*choise15
    total4=50*choise16+80*choise17+90*choise18+70*choise19+120*choise20+100*choise21
    total5=50*choise22+50*choise23+60*choise24+120*choise25

    final=total1+total2+total3+total4+total5
    sub_entry.insert(1,final)

    value1=int(final*15/100)
    value2=int(final+value1)
    total_entry.insert(3,value2)
    
    i.set(final)

def quitt():
    var.destroy()
    

def click1():
    if var1.get()==1:
        e1.config(state=NORMAL)
    else:
        e1.config(state=DISABLED)

def click2():
    if var2.get()==1:
        e2.config(state=NORMAL)
    else:
        e2.config(state=DISABLED)

def click3():
    if var3.get()==1:
        e3.config(state=NORMAL)
    else:
        e3.config(state=DISABLED)

def click4():
    if var4.get()==1:
        e4.config(state=NORMAL)
    else:
        e4.config(state=DISABLED)


def click5():
    if var5.get()==1:
        e5.config(state=NORMAL)
    else:
        e5.config(state=DISABLED)

def click6():
    if var6.get()==1:
        e6.config(state=NORMAL)
    else:
        e6.config(state=DISABLED)

def click7():
    if var7.get()==1:
        e7.config(state=NORMAL)
    else:
        e7.config(state=DISABLED)

def click8():
    if var8.get()==1:
        e8.config(state=NORMAL)
    else:
        e8.config(state=DISABLED)

def click9():
    if var9.get()==1:
        e9.config(state=NORMAL)
    else:
        e9.config(state=DISABLED)


def click10():
    if var10.get()==1:
        e10.config(state=NORMAL)
    else:
        e10.config(state=DISABLED)

def click11():
    if var11.get()==1:
        e11.config(state=NORMAL)
    else:
        e11.config(state=DISABLED)

def click12():
    if var12.get()==1:
        e12.config(state=NORMAL)
    else:
        e12.config(state=DISABLED)

def click13():
    if var13.get()==1:
        e13.config(state=NORMAL)
    else:
        e13.config(state=DISABLED)

def click14():
    if var14.get()==1:
        e14.config(state=NORMAL)
    else:
        e14.config(state=DISABLED)


def click15():
    if var15.get()==1:
        e15.config(state=NORMAL)
    else:
        e15.config(state=DISABLED)

def click16():
    if var16.get()==1:
        e16.config(state=NORMAL)
    else:
        e16.config(state=DISABLED)

def click17():
    if var17.get()==1:
        e17.config(state=NORMAL)
    else:
        e17.config(state=DISABLED)

def click18():
    if var18.get()==1:
        e18.config(state=NORMAL)
    else:
        e18.config(state=DISABLED)

def click19():
    if var19.get()==1:
        e19.config(state=NORMAL)
    else:
        e19.config(state=DISABLED)


def click20():
    if var20.get()==1:
        e20.config(state=NORMAL)
    else:
        e20.config(state=DISABLED)

def click21():
    if var21.get()==1:
        e21.config(state=NORMAL)
    else:
        e21.config(state=DISABLED)

def click22():
    if var22.get()==1:
        e22.config(state=NORMAL)
    else:
        e22.config(state=DISABLED)

def click23():
    if var23.get()==1:
        e23.config(state=NORMAL)
    else:
        e23.config(state=DISABLED)

def click24():
    if var24.get()==1:
        e24.config(state=NORMAL)
    else:
        e24.config(state=DISABLED)


def click25():
    if var25.get()==1:
        e25.config(state=NORMAL)
    else:
        e25.config(state=DISABLED)



frame1=Frame(var,bd=7,width=200).grid(row=1,columnspan=300,sticky=E)
Label(frame1,text="F A S T    F O O D    R E S T A U R A N T ",height=2,width=120,font="Forte",bd=7,bg="light blue").grid(row=0,columnspan=40)
Label(frame1,text="FAST FOOD",font="Forte",bg="pink").grid(row=1,column=2)
Label(frame1,text="   Items   ",font="bold").grid(row=2,column=1,sticky=W)
Label(frame1,text="   Price   ",font="bold").grid(row=2,column=2,sticky=W)
Label(frame1,text="   Qty   ",font="bold").grid(row=2,column=3)

c1=Checkbutton(frame1,text="Noodles",fg="navy blue",variable=var1,command=click1).grid(row=3,column=1,sticky=W)
c2=Checkbutton(frame1,text="Momos",fg="navy blue",variable=var2,command=click2).grid(row=4,column=1,sticky=W)
c3=Checkbutton(frame1,text="salad",fg="navy blue",variable=var3,command=click3).grid(row=5,column=1,sticky=W)
c4=Checkbutton(frame1,text="pattie",fg="navy blue",variable=var4,command=click4).grid(row=6,column=1,sticky=W)
c5=Checkbutton(frame1,text="manchurian",fg="navy blue",variable=var5,command=click5).grid(row=7,column=1,sticky=W)
c6=Checkbutton(frame1,text="fried vegies",fg="navy blue",variable=var6,command=click6).grid(row=8,column=1,sticky=W)
button1=Button(var,text="DONE",bg="orange").grid(row=9,column=3,sticky=W)


Label(frame1,text="50rs").grid(row=3,column=2,sticky=W)
Label(frame1,text="80rs").grid(row=4,column=2,sticky=W)
Label(frame1,text="90rs").grid(row=5,column=2,sticky=W)
Label(frame1,text="70rs").grid(row=6,column=2,sticky=W)
Label(frame1,text="120rs").grid(row=7,column=2,sticky=W)
Label(frame1,text="100rs").grid(row=8,column=2,sticky=W)



e1=Entry(frame1,width=5,state=DISABLED,textvariable=t1)
e1.grid(row=3,column=3)
e2=Entry(frame1,width=5,state=DISABLED,textvariable=t2)
e2.grid(row=4,column=3)
e3=Entry(frame1,width=5,state=DISABLED,textvariable=t3)
e3.grid(row=5,column=3)
e4=Entry(frame1,width=5,state=DISABLED,textvariable=t4)
e4.grid(row=6,column=3)
e5=Entry(frame1,width=5,state=DISABLED,textvariable=t5)
e5.grid(row=7,column=3)
e6=Entry(frame1,width=5,state=DISABLED,textvariable=t6)
e6.grid(row=8,column=3)




###############################SHAKES###############################################


Label(frame1,text="SHAKES",font="Forte",bg="pink").grid(row=1,column=6,sticky=W)
Label(frame1,text="   Items   ",font="bold").grid(row=2,column=5,sticky=W)
Label(frame1,text="   Price   ",font="bold").grid(row=2,column=6,sticky=W)
Label(frame1,text="   Qty   ",font="bold").grid(row=2,column=7)

c7=Checkbutton(frame1,text="dry fruit shake",fg="navy blue",variable=var7,command=click7).grid(row=3,column=5,sticky=W)
c8=Checkbutton(frame1,text="MANGO SHAKE",fg="navy blue",variable=var8,command=click8).grid(row=4,column=5,sticky=W)
c9=Checkbutton(frame1,text="OREO SHAKE",fg="navy blue",variable=var9,command=click9).grid(row=5,column=5,sticky=W)
c10=Checkbutton(frame1,text="BANANA SHAKE",fg="navy blue",variable=var10,command=click10).grid(row=6,column=5,sticky=W)
c11=Checkbutton(frame1,text="CHOCOLATE SHAKE",fg="navy blue",variable=var11,command=click11).grid(row=7,column=5,sticky=W)
button2=Button(var,text="DONE",bg="orange").grid(row=8,column=7,sticky=W)


Label(frame1,text="50rs").grid(row=3,column=6,sticky=W)
Label(frame1,text="50rs").grid(row=4,column=6,sticky=W)
Label(frame1,text="60rs").grid(row=5,column=6,sticky=W)
Label(frame1,text="70rs").grid(row=6,column=6,sticky=W)
Label(frame1,text="30rs").grid(row=7,column=6,sticky=W)

e7=Entry(frame1,width=5,state=DISABLED,textvariable=t7)
e7.grid(row=3,column=7)
e8=Entry(frame1,width=5,state=DISABLED,textvariable=t8)
e8.grid(row=4,column=7)
e9=Entry(frame1,width=5,state=DISABLED,textvariable=t9)
e9.grid(row=5,column=7)
e10=Entry(frame1,width=5,state=DISABLED,textvariable=t10)
e10.grid(row=6,column=7)
e11=Entry(frame1,width=5,state=DISABLED,textvariable=t11)
e11.grid(row=7,column=7)



###########################################SANDWICHES################################################################

Label(frame1,text="SANDWICHES",font="Forte",bg="pink").grid(row=10,column=2,sticky=W)
Label(frame1,text="   Items   ",font="bold",).grid(row=11,column=1,sticky=W)
Label(frame1,text="   Price   ",font="bold").grid(row=11,column=2,sticky=W)
Label(frame1,text="   Qty   ",font="bold").grid(row=11,column=3)

c12=Checkbutton(frame1,text="Grilled sandwich",fg="navy blue",variable=var12,command=click12).grid(row=12,column=1,sticky=W)
c13=Checkbutton(frame1,text="Chees sandwich",fg="navy blue",variable=var13,command=click13).grid(row=13,column=1,sticky=W)
c14=Checkbutton(frame1,text="Vegitable sandwich",fg="navy blue",variable=var14,command=click14).grid(row=14,column=1,sticky=W)
c15=Checkbutton(frame1,text="French toast",fg="navy blue",variable=var15,command=click15).grid(row=15,column=1,sticky=W)
button2=Button(var,text="DONE",bg="orange").grid(row=16,column=3,sticky=W)

Label(frame1,text="50rs").grid(row=12,column=2,sticky=W)
Label(frame1,text="50rs").grid(row=13,column=2,sticky=W)
Label(frame1,text="60rs").grid(row=14,column=2,sticky=W)
Label(frame1,text="70rs").grid(row=15,column=2,sticky=W)

e12=Entry(frame1,width=5,state=DISABLED,textvariable=t12)
e12.grid(row=12,column=3)
e13=Entry(frame1,width=5,state=DISABLED,textvariable=t13)
e13.grid(row=13,column=3)
e14=Entry(frame1,width=5,state=DISABLED,textvariable=t14)
e14.grid(row=14,column=3)
e15=Entry(frame1,width=5,state=DISABLED,textvariable=t15)
e15.grid(row=15,column=3)

###########################payment method############################
Label(frame1,text="PAYMENT METHOD",font="Forte",bg="pink").grid(row=10,column=5,sticky=W)
p_method=Label(frame1,text="Payment Method",font="bold")
p_method.grid(row=12,column=4)

delivery=["Cash","Paytym"]
listt=Combobox(frame1,values=delivery)
listt.grid(row=13,column=4)


tax=Label(frame1,text="GST",font="bold")
tax.grid(row=12,column=5)


tax_entry=Entry(frame1)
tax_entry.grid(row=12,column=6)
tax_entry.insert(2,"15%")

sub_total=Label(frame1,text="Sub Total",font="bold")
sub_total.grid(row=13,column=5)
sub_entry=Entry(frame1)
sub_entry.grid(row=13,column=6)

total_label=Label(frame1,text="Total",font="bold")
total_label.grid(row=14,column=5)
total_entry=Entry(frame1)
total_entry.grid(row=14,column=6)

total_button=Button(frame1,text="Total",bg="orange",command=pay)
total_button.grid(row=15,column=4)

reset_button=Button(frame1,text="Reset",bg="orange",command=resett)
reset_button.grid(row=15,column=5)

exit_button=Button(frame1,text="Exit",bg="orange",command=quitt)
exit_button.grid(row=15,column=6)



########################################deserts####################################################################

Label(frame1,text="DESERTS",font="Forte",bg="pink").grid(row=1,column=10)
Label(frame1,text="   Items   ",font="bold").grid(row=2,column=9,sticky=W)
Label(frame1,text="   Price   ",font="bold").grid(row=2,column=10,sticky=W)
Label(frame1,text="   Qty   ",font="bold").grid(row=2,column=11)

c1=Checkbutton(frame1,text="Cup cakes",fg="navy blue",variable=var16,command=click16).grid(row=3,column=9,sticky=W)
c2=Checkbutton(frame1,text="Chooroes",fg="navy blue",variable=var17,command=click17).grid(row=4,column=9,sticky=W)
c3=Checkbutton(frame1,text="ice creams",fg="navy blue",variable=var18,command=click18).grid(row=5,column=9,sticky=W)
c4=Checkbutton(frame1,text="Chocolawa cake",fg="navy blue",variable=var19,command=click19).grid(row=6,column=9,sticky=W)
c5=Checkbutton(frame1,text="Gulab Jamun",fg="navy blue",variable=var20,command=click20).grid(row=7,column=9,sticky=W)
c6=Checkbutton(frame1,text="Rasmalai",fg="navy blue",variable=var21,command=click21).grid(row=8,column=9,sticky=W)
button3=Button(var,text="DONE",bg="orange").grid(row=9,column=11,sticky=W)


Label(frame1,text="50rs").grid(row=3,column=10,sticky=W)
Label(frame1,text="80rs").grid(row=4,column=10,sticky=W)
Label(frame1,text="90rs").grid(row=5,column=10,sticky=W)
Label(frame1,text="70rs").grid(row=6,column=10,sticky=W)
Label(frame1,text="120rs").grid(row=7,column=10,sticky=W)
Label(frame1,text="100rs").grid(row=8,column=10,sticky=W)



e16=Entry(frame1,width=5,state=DISABLED,textvariable=t16)
e16.grid(row=3,column=11)
e17=Entry(frame1,width=5,state=DISABLED,textvariable=t17)
e17.grid(row=4,column=11)
e18=Entry(frame1,width=5,state=DISABLED,textvariable=t18)
e18.grid(row=5,column=11)
e19=Entry(frame1,width=5,state=DISABLED,textvariable=t19)
e19.grid(row=6,column=11)
e20=Entry(frame1,width=5,state=DISABLED,textvariable=t20)
e20.grid(row=7,column=11)
e21=Entry(frame1,width=5,state=DISABLED,textvariable=t21)
e21.grid(row=8,column=11)

############################################DRINKS###############################################


Label(frame1,text="DRINKS",font="Forte",bg="pink").grid(row=10,column=10,sticky=W)
Label(frame1,text="   Items   ",font="bold").grid(row=11,column=9,sticky=W)
Label(frame1,text="   Price   ",font="bold").grid(row=11,column=10,sticky=W)
Label(frame1,text="   Qty   ",font="bold").grid(row=11,column=11)

c12=Checkbutton(frame1,text="Cold drinks",fg="navy blue",variable=var22,command=click22).grid(row=12,column=9,sticky=W)
c13=Checkbutton(frame1,text="Fruit Juice",fg="navy blue",variable=var23,command=click23).grid(row=13,column=9,sticky=W)
c14=Checkbutton(frame1,text="Mix Juice",fg="navy blue",variable=var24,command=click24).grid(row=14,column=9,sticky=W)
c15=Checkbutton(frame1,text="Apple Cyder",fg="navy blue",variable=var25,command=click25).grid(row=15,column=9,sticky=W)
button4=Button(var,text="DONE",bg="orange").grid(row=16,column=11,sticky=W)

Label(frame1,text="50rs").grid(row=12,column=10,sticky=W)
Label(frame1,text="50rs").grid(row=13,column=10,sticky=W)
Label(frame1,text="60rs").grid(row=14,column=10,sticky=W)
Label(frame1,text="120rs").grid(row=15,column=10,sticky=W)

e22=Entry(frame1,width=5,state=DISABLED,textvariable=t22)
e22.grid(row=12,column=11)
e23=Entry(frame1,width=5,state=DISABLED,textvariable=t23)
e23.grid(row=13,column=11)
e24=Entry(frame1,width=5,state=DISABLED,textvariable=t24)
e24.grid(row=14,column=11)
e25=Entry(frame1,width=5,state=DISABLED,textvariable=t25)
e25.grid(row=15,column=11)

var.mainloop()

