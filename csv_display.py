import tkinter as tk
from tkinter import ttk
import csv

root=tk.Tk()
root.geometry('1024x512')
root.resizable(0,0)
root.config(bg='black')
file=open('abc.csv','r',newline='',encoding='UTF-32')
b=csv.reader(file)
frame=tk.Frame(root,bg='black',padx=120)
frame.grid(row=0,column=0)
can=ttk.Scrollbar(frame,orient='vertical')
can.grid(row=0,column=4,sticky='nswe')
cnt=0
lis=[i for i in b]
for i in lis:
	tex=tk.Label(frame,text=i[0],fg='black',font=('lucida console',12))
	tex.grid(row=cnt,column=0,padx=20,pady=10)
	tex=tk.Label(frame,text=i[1],fg='black',font=('lucida console',12))
	tex.grid(row=cnt,column=1,padx=20,pady=10)
	tex=tk.Label(frame,text=i[2],fg='black',font=('lucida console',12))
	tex.grid(row=cnt,column=2,padx=20,pady=10)
	tex=tk.Label(frame,text=i[3],fg='black',font=('lucida console',12))
	tex.grid(row=cnt,column=3,padx=20,pady=10)
	cnt+=1

else:
	mb=tk.Label(frame,text=f'total : {cnt} Members',fg='cyan',font=('lucida console',12))
	mb.grid(row=cnt+1,column=0)
	cnt=0










file.close()
root.mainloop()