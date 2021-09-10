import tkinter as tk
from tkinter import ttk
import csv

root=tk.Tk()
root.geometry('1024x512')
root.resizable(0,0)
root.config(bg='black')
file=open('abc.csv','r',newline='',encoding='UTF-32')
b=csv.reader(file)
fr1=tk.Frame(root,bg='black')
fr1.grid(row=0,column=0,columnspan=10)
cav=tk.Canvas(fr1)
cav.grid(row=0,column=0)
can=ttk.Scrollbar(fr1,orient='vertical',command=cav.yview)
can.grid(row=0,column=4,sticky='ns')

cav.configure(yscrollcommand=can.set)

frame=tk.Frame(cav,bg='black',padx=180)
frame.grid(row=0,column=0)
cav.create_window((0,0),window=frame,anchor='nw')
cav.bind('<Configure>',lambda e: cav.configure(scrollregion=cav.bbox('all'),width=1000,height=510))


lam=tk.Label(frame,text='The Homicide Crew',fg='cyan',bg='black',padx=5,pady=5,font=('garamond bold',24),borderwidth=2,relief='groove')
lam.grid(row=0,column=0,columnspan=4,padx=20,pady=10,sticky='nswe')

cnt=1
lis=[i for i in b]
print(len(lis)-1)
for i in lis:
	tex=tk.Label(frame,text=i[0],fg='cyan',bg='black',padx=5,pady=5,font=('lucida console',12),borderwidth=2,relief='groove')
	tex.grid(row=cnt,column=0,padx=20,pady=10,sticky='nswe')
	tex=tk.Label(frame,text=i[1],fg='cyan',bg='black',padx=5,pady=5,font=('lucida console',12),borderwidth=2,relief='groove')
	tex.grid(row=cnt,column=1,padx=20,pady=10,sticky='nswe')
	tex=tk.Label(frame,text=i[2],fg='cyan',bg='black',padx=5,pady=5,font=('lucida console',12),borderwidth=2,relief='groove')
	tex.grid(row=cnt,column=2,padx=20,pady=10,sticky='nswe')
	tex=tk.Label(frame,text=i[3],fg='cyan',bg='black',padx=5,pady=5,font=('lucida console',12),borderwidth=2,relief='groove')
	tex.grid(row=cnt,column=3,padx=20,pady=10,sticky='nswe')
	cnt+=1

else:
	mb=tk.Label(frame,text=f'total : {cnt-2} Members',fg='cyan',font=('lucida console',12),bg='black') #-2 : -1 bcoz cnt=1 , -1 title
	mb.grid(row=cnt+1,column=1,columnspan=2,pady=10)
	cnt=1










file.close()
root.mainloop()