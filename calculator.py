from tkinter import *
import math

screen = Tk()
screen.title("Calculator")
screen.geometry("320x447")

def click(b):
    global input
    input+=b
    output.set(input)

def clear():
    global input
    input =''
    output.set("")

def equals():
    global input
    try:
        res= eval(input)
        input=str(res)
        output.set(res)
    except:
        output.set("Invalid imput")
        input=''


#advanced functions
def toRad(x):
    x*=math.pi/180
    return x

def sin():
    global input
    try:
        res= eval(input)
        res=toRad(res)
        input=str(res)
        output.set(res)
    except:
        output.set("Invalid imput")
        input=''

def cos():
    global input
    try:
        res= eval(input)
        res=toRad(res)
        input=str(res)
        output.set(res)
    except:
        output.set("Invalid imput")
        input=''

def tan():
    global input
    try:
        res= eval(input)
        res=toRad(res)
        input=str(res)
        output.set(res)
    except:
        output.set("Invalid imput")
        input=''

def sqrt():
    global input
    try:
        res= eval(input)
        res=math.sqrt(res)
        input=str(res)
        output.set(res)
    except:
        output.set("Invalid imput")
        input=''

def log():
    global input
    try:
        res= eval(input)
        res=math.log(res)
        input=str(res)
        output.set(res)
    except:
        output.set("Invalid imput")
        input=''

output = StringVar()
input=''

result = Entry(screen, bg='light gray', font=('Segoe UI',20,'bold'),
justify='right', textvariable=output)
result.place(x=0,y=0,height =60,width=320)

#button size=64x77
#1st row
bSin = Button(screen,text='sin',font=('Segoe UI',15,'bold'), activebackground ='light gray', activeforeground = 'gray',command=sin)
bSin.place(x=0,y=60,height=77,width=64)

bRoot = Button(screen,text='sqrt',font=('Segoe UI',15,'bold'), activebackground ='light gray', activeforeground = 'gray',command=sqrt)
bRoot.place(x=64,y=60,height=77,width=64)

bOpenBrace = Button(screen,text='(',font=('Segoe UI',15,'bold'), command=lambda:click('('), activebackground ='light gray', activeforeground = 'gray')
bOpenBrace.place(x=128,y=60,height=77,width=64)

bClosedBrace = Button(screen,text=')',font=('Segoe UI',15,'bold'), command=lambda:click(')'), activebackground ='light gray', activeforeground = 'gray')
bClosedBrace.place(x=192,y=60,height=77,width=64)

bDivision = Button(screen,text='/',font=('Segoe UI',15,'bold'), command=lambda:click('/'), activebackground ='light gray', activeforeground = 'gray')
bDivision.place(x=256,y=60,height=77,width=64)

#2nd row
bCos = Button(screen,text='cos',font=('Segoe UI',15,'bold'), activebackground ='light gray', activeforeground = 'gray',command=cos)
bCos.place(x=0,y=137,height=77,width=64)

b7 = Button(screen,text='7',font=('Segoe UI',15,'bold'), command=lambda:click('7'), activebackground ='light gray', activeforeground = 'gray')
b7.place(x=64,y=137,height=77,width=64)

b8 = Button(screen,text='8',font=('Segoe UI',15,'bold'), command=lambda:click('8'), activebackground ='light gray', activeforeground = 'gray')
b8.place(x=128,y=137,height=77,width=64)

b9 = Button(screen,text='9',font=('Segoe UI',15,'bold'), command=lambda:click('9'), activebackground ='light gray', activeforeground = 'gray')
b9.place(x=192,y=137,height=77,width=64)

bMul = Button(screen,text='x',font=('Segoe UI',15,'bold'), command=lambda:click('x'), activebackground ='light gray', activeforeground = 'gray')
bMul.place(x=256,y=137,height=77,width=64)

#3rd row
bTan = Button(screen,text='tan',font=('Segoe UI',15,'bold'), activebackground ='light gray', activeforeground = 'gray',command=tan)
bTan.place(x=0,y=214,height=77,width=64)

b4 = Button(screen,text='4',font=('Segoe UI',15,'bold'), command=lambda:click('4'), activebackground ='light gray', activeforeground = 'gray')
b4.place(x=64,y=214,height=77,width=64)

b5 = Button(screen,text='5',font=('Segoe UI',15,'bold'), command=lambda:click('5'), activebackground ='light gray', activeforeground = 'gray')
b5.place(x=128,y=214,height=77,width=64)

b6 = Button(screen,text='6',font=('Segoe UI',15,'bold'), command=lambda:click('6'), activebackground ='light gray', activeforeground = 'gray')
b6.place(x=192,y=214,height=77,width=64)

bSub = Button(screen,text='-',font=('Segoe UI',15,'bold'), command=lambda:click('-'), activebackground ='light gray', activeforeground = 'gray')
bSub.place(x=256,y=214,height=77,width=64)

#4th row
bln = Button(screen,text='ln',font=('Segoe UI',15,'bold'), activebackground ='light gray', activeforeground = 'gray',command=log)
bln.place(x=0,y=291,height=77,width=64)

b1 = Button(screen,text='1',font=('Segoe UI',15,'bold'), command=lambda:click('1'), activebackground ='light gray', activeforeground = 'gray')
b1.place(x=64,y=291,height=77,width=64)

b2 = Button(screen,text='2',font=('Segoe UI',15,'bold'), command=lambda:click('2'), activebackground ='light gray', activeforeground = 'gray')
b2.place(x=128,y=291,height=77,width=64)

b3 = Button(screen,text='3',font=('Segoe UI',15,'bold'), command=lambda:click('3'), activebackground ='light gray', activeforeground = 'gray')
b3.place(x=192,y=291,height=77,width=64)

bAdd = Button(screen,text='+',font=('Segoe UI',15,'bold'), command=lambda:click('+'), activebackground ='light gray', activeforeground = 'gray')
bAdd.place(x=256,y=291,height=77,width=64)

#5th row
bPower = Button(screen,text='x^y',font=('Segoe UI',15,'bold'), command=lambda:click('x^y'), activebackground ='light gray', activeforeground = 'gray')
bPower.place(x=0,y=368,height=77,width=64)

bC = Button(screen,text='C',font=('Segoe UI',15,'bold'),activebackground ='light gray', activeforeground = 'gray',command=clear)
bC.place(x=64,y=368,height=77,width=64)

b0 = Button(screen,text='0',font=('Segoe UI',15,'bold'), command=lambda:click('0'), activebackground ='light gray', activeforeground = 'gray')
b0.place(x=128,y=368,height=77,width=64)

bDot = Button(screen,text='.',font=('Segoe UI',15,'bold'), command=lambda:click('.'), activebackground ='light gray', activeforeground = 'gray')
bDot.place(x=192,y=368,height=77,width=64)

bEq = Button(screen,text='=',font=('Segoe UI',15,'bold'), command=equals, activebackground ='light gray', activeforeground = 'gray')
bEq.place(x=256,y=368,height=77,width=64)

screen.mainloop()
