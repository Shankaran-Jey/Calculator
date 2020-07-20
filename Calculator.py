from tkinter import *
root = Tk()
root.title("Calculator")
root.resizable(0,0)


global Flag,x,Answer
x = " "
Answer = 0
Flag = "True"

Top = Entry(root,width = 16, font = ("Verdana 25"),border = 0,background = "#ffffff",foreground = "#000000")
Top.grid(row = 0,column = 0,columnspan = 4)
Bottom = Entry(root,width = 16, font = ("Verdana 25"),border = 0,background = "#ffffff",foreground = "#000000")
Bottom.grid(row = 1,column = 0,columnspan = 4)


def button_clear():
    Top.delete(0,END)
    Bottom.delete(0,END)
    
def button_click(Charecter):
    global  Answer,Flag,x
    current = Top.get()
    Top.delete(0,END)
    Display =(str(current) + str(Charecter))
    Top.insert(0,Display)

    if (Flag == "True"):
      Answer= Top.get()

    if(x == "Addition")  and (Flag == "False"):
       A = Top.get()
       Display = float(A) + float(Answer)
      
    if(x == "Subtraction")  and (Flag == "False"):
       A = Top.get()
       Display = float(Answer) - float(A)
       
    if(x == "Multiplication") and (Flag == "False"):
       A = Top.get()
       Display = float(Answer) * float(A)
       
    if(x == "Division") and (Flag == "False"):
       A = Top.get()
       Display = float(Answer)/float(A)
    Bottom.delete(0,END)
    Bottom.insert(0,Display)   
     

def math(operation):
    global Flag,Answer,x
    Answer = Bottom.get()
    Flag = "False"
    Top.delete(0,END)
    x = operation
    
def button_equals():
    global Answer,Flag
    Answer = Bottom.get()
    Top.delete(0,END)
    Bottom.delete(0,END)
    Bottom.insert(0,Answer)
    Answer = 0
    Flag = "True"
    
# DEFINING BUTTONS

Button_0 = Button(root,text="0",background = "black",foreground = "White",font = ("Verdana"),relief = GROOVE,border = 1,padx = 40,pady = 20,command=lambda: button_click(0))

Button_1 = Button(root,text="1",background = "black",foreground = "White",font = ("Verdana"),relief = GROOVE,border = 1,padx = 40,pady = 20,command=lambda: button_click(1))
Button_2 = Button(root,text="2",background = "black",foreground = "White",font = ("Verdana"),relief = GROOVE,border = 1,padx = 40,pady = 20,command=lambda: button_click(2))
Button_3 = Button(root,text="3",background = "black",foreground = "White",font = ("Verdana"),relief = GROOVE,border = 1,padx = 40,pady = 20,command=lambda: button_click(3))

Button_4 = Button(root,text="4",background = "black",foreground = "White",font = ("Verdana"),relief = GROOVE,border = 1,padx = 40,pady = 20,command=lambda: button_click(4))
Button_5 = Button(root,text="5",background = "black",foreground = "White",font = ("Verdana"),relief = GROOVE,border = 1,padx = 40,pady = 20,command=lambda: button_click(5))
Button_6 = Button(root,text="6",background = "black",foreground = "White",font = ("Verdana"),relief = GROOVE,border = 1,padx = 40,pady = 20,command=lambda: button_click(6))

Button_7 = Button(root,text="7",background = "black",foreground = "White",font = ("Verdana"),relief = GROOVE,border = 1,padx = 40,pady = 20,command=lambda: button_click(7))
Button_8 = Button(root,text="8",background = "black",foreground = "White",font = ("Verdana"),relief = GROOVE,border = 1,padx = 40,pady = 20,command=lambda: button_click(8))
Button_9 = Button(root,text="9",background = "black",foreground = "White",font = ("Verdana"),relief = GROOVE,border = 1,padx = 40,pady = 20,command=lambda: button_click(9))

Button_addition       =   Button(root,text="+",background = "black",foreground = "White",font = ("Verdana"),relief = GROOVE,border = 1,padx = 38,pady = 20,command=lambda: math("Addition"))
Button_subtraction    =   Button(root,text="_",background = "black",foreground = "White",font = ("Verdana"),relief = GROOVE,border = 1,padx = 40,pady = 20,command=lambda: math("Subtraction"))
Button_division       =   Button(root,text="/",background = "black",foreground = "White",font = ("Verdana"),relief = GROOVE,border = 1,padx = 42,pady = 20,command=lambda: math("Division"))
Button_multiplication =   Button(root,text="*",background = "black",foreground = "White",font = ("Verdana"),relief = GROOVE,border = 1,padx = 40,pady = 20,command=lambda: math("Multiplication"))

Button_Equal =   Button(root,text="=",background = "black",foreground = "White",font = ("Verdana"),relief = GROOVE,border = 1,padx = 38.5,pady = 20,command= button_equals)
Button_Clear =   Button(root,text="Clear",background = "black",foreground = "White",font = ("Verdana"),relief = GROOVE,border = 1,padx = 20,pady = 20,command= button_clear)

# DISPLAYING BUTTONS

Button_0.grid(row=5 ,column=1)

Button_1.grid(row=4 ,column=0)
Button_2.grid(row=4 ,column=1)
Button_3.grid(row=4 ,column=2) 

Button_4.grid(row=3 ,column=0)
Button_5.grid(row=3 ,column=1) 
Button_6.grid(row=3 ,column=2)

Button_7.grid(row=2 ,column=0)
Button_8.grid(row=2 ,column=1)
Button_9.grid(row=2 ,column=2)

Button_addition.grid(row=2 ,column=3)
Button_subtraction.grid(row=3 ,column=3)
Button_division.grid(row=4 ,column=3)
Button_multiplication.grid(row=5 ,column=3)

Button_Equal.grid(row=5 ,column=0)
Button_Clear.grid(row=5 ,column=2)





root.mainloop()
