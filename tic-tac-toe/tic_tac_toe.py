from tkinter import*
window=Tk()
window.title('one tic tac toe')

window.configure(background='#000000')
n=1
tic=[['' for r in range(3)]for c in range(3) ]
t=''
def update(num):
    global n
    global tic
    if n==1 or n==3 or n==5 or n==7 or n==9:
        t='X'
    else:
        t='O'
    num.config(text=t)
    check(num,t)
   
   
    n=n+1
def refresh():
    global tic
    global n
    n=1
    t=''
    tic=[['' for r in range(3)]for c in range(3) ]
    button1.config(text='')
    button2.config(text='')
    button3.config(text='')
    button4.config(text='')
    button5.config(text='')
    button6.config(text='')
    button7.config(text='')
    button8.config(text='')
    button9.config(text='')
   
def check(num,t):
     global tic
     
     global n
     if num==button1:
         tic[0][0]=t
     elif num==button2:
         tic[0][1]=t
     elif num==button3:
         tic[0][2]=t
     elif num==button4:
         tic[1][0]=t
     elif num==button5:
        tic[1][1]=t
     elif num==button6:
         tic[1][2]=t
     elif num==button7:
         tic[2][0]=t
     elif num==button8:
         tic[2][1]=t
     else:
         tic[2][2]=t
     print(tic)    
     if (tic[0][0]==tic[0][1]==tic[0][2]=='X' or tic[1][0]==tic[1][1]==tic[1][2]=='X' or tic[2][0]==tic[2][1]==tic[2][2]=='X' or tic[0][0]==tic[1][1]==tic[2][2]=='X' or tic[0][2]==tic[1][1]==tic[2][0]=='X' or tic[0][0]==tic[1][0]==tic[2][0]=='X' or tic[0][1]==tic[1][1]==tic[2][1]=='X' or tic[0][2]==tic[1][2]==tic[2][2]=='X') or(tic[0][0]==tic[0][1]==tic[0][2]=='O' or tic[1][0]==tic[1][1]==tic[1][2]=='O' or tic[2][0]==tic[2][1]==tic[2][2]=='O' or tic[0][0]==tic[1][1]==tic[2][2]=='O' or tic[0][2]==tic[1][1]==tic[2][0]=='O' or tic[0][0]==tic[1][0]==tic[2][0]=='O' or tic[0][1]==tic[1][1]==tic[2][1]=='O' or tic[0][2]==tic[1][2]==tic[2][2]=='O')  :
         
         
         
         
          root=Tk()
          root.geometry('250x250')
          intro=Label(root,text='GAME OVER',font=('Times New Roman',20),fg='white',bg='black')
          root.configure(background='#000000')
          intro.pack()
         
          buttonrefresh=Button(master=root,text='CLICK TO REFRESH',font=('Times New Roman', 10), bg='#DAE0E2',command=refresh)
          buttonrefresh.pack()
         
                               
start=Label(window,text='TIC TAC TOE',font=('Times New Roman',20),fg='white',bg='black')
start.grid(column=0,row=3)

middle=Label(window,text='1st player enters X and 2nd player enters O',font=('Times New Roman',20),fg='white',bg='black')
middle.grid(column=0,row=4)
button1=Button(text='',font=('Times New Roman', 20),width=4, bg='#DAE0E2',command=lambda:update(button1))
button2=Button(text='',font=('Times New Roman', 20),width=4, bg='#DAE0E2',command=lambda:update(button2))
button3=Button(text='',font=('Times New Roman', 20),width=4, bg='#DAE0E2',command=lambda:update(button3))
button4=Button(text='',font=('Times New Roman', 20),width=4, bg='#DAE0E2',command=lambda:update(button4))
button5=Button(text='',font=('Times New Roman', 20),width=4, bg='#DAE0E2',command=lambda:update(button5))
button6=Button(text='',font=('Times New Roman', 20),width=4, bg='#DAE0E2',command=lambda:update(button6))
button7=Button(text='',font=('Times New Roman', 20),width=4, bg='#DAE0E2',command=lambda:update(button7))
button8=Button(text='',font=('Times New Roman', 20),width=4, bg='#DAE0E2',command=lambda:update(button8))
button9=Button(text='',font=('Times New Roman', 20),width=4, bg='#DAE0E2',command=lambda:update(button9))
button10=Button(text='refresh',font=('Times New Roman', 20),width=5,fg='black',bg='white',command=refresh)
button10.grid(column=0,row=5)
button1.grid(column=2,row=3)
button2.grid(column=3,row=3)
button3.grid(column=4,row=3)
button4.grid(column=2,row=4)
button5.grid(column=3,row=4)
button6.grid(column=4,row=4)
button7.grid(column=2,row=5)
button8.grid(column=3,row=5)
button9.grid(column=4,row=5)
window.mainloop()
