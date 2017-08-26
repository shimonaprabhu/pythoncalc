from tkinter import *

root=Tk()
equal=""
equation=StringVar()# to update text of label

calculation=Label(root,textvariable=equation)#update text whenever uppdated

equation.set("Enter your equation")

calculation.grid(columnspan=4)

def buttonprs(num):
    global equal
    equal=equal+str(num)
    equation.set(equal)
def equalpress():
    global equal
    total=str(eval(equal))
    equation.set(total)
    equal=""
def clearpress():
    global equal
    equal=""
    equation.set("")

Button1=Button(root,text="1",command=lambda:buttonprs(1))
Button1.grid(row=1,column=0)
Button2=Button(root,text="2",command=lambda:buttonprs(2))
Button2.grid(row=1,column=1)
Button3=Button(root,text="3",command=lambda:buttonprs(3))
Button3.grid(row=1,column=2)
Button4=Button(root,text="4",command=lambda:buttonprs(4))
Button4.grid(row=2,column=0)
Button5=Button(root,text="5",command=lambda:buttonprs(5))
Button5.grid(row=2,column=1)
Button6=Button(root,text="6",command=lambda:buttonprs(6))
Button6.grid(row=2,column=2)
Button7=Button(root,text="7",command=lambda:buttonprs(7))
Button7.grid(row=3,column=0)
Button8=Button(root,text="8",command=lambda:buttonprs(8))
Button8.grid(row=3,column=1)
Button9=Button(root,text="9",command=lambda:buttonprs(9))
Button9.grid(row=3,column=2)
Button0=Button(root,text="0",command=lambda:buttonprs(0))
Button0.grid(row=4,column=1)

Add=Button(root,text="+",command=lambda:buttonprs("+"))
Add.grid(row=1,column=3)
Sub=Button(root,text="-",command=lambda:buttonprs("-"))
Sub.grid(row=2,column=3)
Mul=Button(root,text="*",command=lambda:buttonprs("*"))
Mul.grid(row=3,column=3)
Div=Button(root,text="/",command=lambda:buttonprs("/"))
Div.grid(row=4,column=3)



equalsign=Button(root,text="=",command=equalpress)
equalsign.grid(row=4,column=2)

clearsign=Button(root,text="C",command=clearpress)
clearsign.grid(row=4,column=0)

# lambda is anonymous equation

root.mainloop()
