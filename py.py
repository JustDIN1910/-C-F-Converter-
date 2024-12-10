from tkinter import*
window =Tk()
window.title("C'--F'")
window.iconbitmap ("/New folder/thermometer.ico")
e=Entry(width=55,borderwidth=2)
e.grid(row=0,column=0,columnspan=3)
def Buttonclick(number):
    current=e.get( )
    e.delete(0,END)
    e.insert(1,str(current)+str(number))

def ButtonClear():
    e.delete(0,END)
    
def Buttonequal():
    global fn
    first_number=e.get()
    e.delete(0,END)
    fn=int(first_number)
    e.delete(0,END)
    result=(fn*1.8)+32
    e.insert(END,str(result))
     
button_style = {"bg": "black", "fg": "red", "padx": 50, "pady": 50}        



button1=Button(text=1,padx=50,pady=50,command=lambda:Buttonclick(1)).grid(row=1,column=0)
button2=Button(text=2,padx=50,pady=50,command=lambda:Buttonclick(2)).grid(row=1,column=1)
button3=Button(text=3,padx=50,pady=50,command=lambda:Buttonclick(3)).grid(row=1,column=2)
button4=Button(text=4,padx=50,pady=50,command=lambda:Buttonclick(4)).grid(row=2,column=0)
button5=Button(text=5,padx=50,pady=50,command=lambda:Buttonclick(5)).grid(row=2,column=1)
button6=Button(text=6,padx=50,pady=50,command=lambda:Buttonclick(6)).grid(row=2,column=2)
button7=Button(text=7,padx=50,pady=50,command=lambda:Buttonclick(7)).grid(row=3,column=0)
button8=Button(text=8,padx=50,pady=50,command=lambda:Buttonclick(8)).grid(row=3,column=1)
button9=Button(text=9,padx=50,pady=50,command=lambda:Buttonclick(9)).grid(row=3,column=2)
button0=Button(text=0,padx=50,pady=50,command=lambda:Buttonclick(0)).grid(row=4,column=0)
buttonclear=Button(text="cla" ,padx=50,pady=50,command=ButtonClear).grid(row=4,column=2)
buttonequal=Button(text= '=',padx=50,pady=50,command=Buttonequal).grid(row=4,column=1)
buttonF=Button(text='F',padx=50,pady=50).grid(row=5,column=1)



window.mainloop()