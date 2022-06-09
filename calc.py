from tkinter import *


cal = Tk()
cal.title('CALCULATOR')
operator = ""
text_input=StringVar()

def btnClick(num):
    global operator
    operator=operator+str(num)
    text_input.set(operator)
def clearDisplay():
    global operator
    operator=""
    text_input.set("")
def btnEqual():
    global operator
    sum=str(eval(operator))
    text_input.set(sum)
    operator = ""

textDisplay=Entry(cal,font=('arial',20, 'bold'),textvariable=text_input,bd=30,insertwidth=4,bg="powder blue",justify='right').grid(columnspan=4)
#==============================================================================================================================
btn7=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),bg="powder blue", text='7',command=lambda:btnClick(7)).grid(row=1,column=0)
btn8=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),bg="powder blue",text='8',command=lambda:btnClick(8)).grid(row=1,column=1)
btn9=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),bg="powder blue",text='9',command=lambda:btnClick(9)).grid(row=1,column=2)
Add=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),bg="powder blue",text='+',command=lambda:btnClick('+')).grid(row=1,column=3)
#======================================================================================================================
btn4=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),bg="powder blue",text='4',command=lambda:btnClick(4)).grid(row=2,column=0)
btn5=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),bg="powder blue",text='5',command=lambda:btnClick(5)).grid(row=2,column=1)
btn6=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),bg="powder blue",text='6',command=lambda:btnClick(6)).grid(row=2,column=2)
Sub=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),bg="powder blue",text='-',command=lambda:btnClick('-')).grid(row=2,column=3)
#=======================================================================================================================
btn3=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),bg="powder blue",text='3',command=lambda:btnClick(3)).grid(row=3,column=0)
btn2=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),bg="powder blue",text='2',command=lambda:btnClick(2)).grid(row=3,column=1)
btn1=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),bg="powder blue",text='1',command=lambda:btnClick(1)).grid(row=3,column=2)
Mul=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),bg="powder blue",text='*',command=lambda:btnClick('*')).grid(row=3,column=3)
#======================================================================================================================
btn0=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),bg="powder blue",text='0',command=lambda:btnClick(0)).grid(row=4,column=0)
btnEqual=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),bg="powder blue",text='=',command=btnEqual).grid(row=4,column=1)
btnClear=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),bg="powder blue",text='C',command=clearDisplay).grid(row=4,column=2)
Div=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),bg="powder blue",text='/',command=lambda:btnClick('/')).grid(row=4,column=3)
#========================================================================================================================













cal.mainloop()