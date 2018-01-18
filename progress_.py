import requests,re,os
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import messagebox,filedialog
from codechef_codes import code,codechef_solutions
from codechef import get_rating
from tkinter import ttk
directory="/"

	#print(name)
root = Tk()
root.title("Codechef Crawler")
top=Frame(root)
bottom=Frame(root).pack(side=BOTTOM)
top.pack()
text=Text(bottom, height=10, bg="blue", bd=3, fg='white')
root.geometry("400x450")
def callback():
    if messagebox.askyesno('Verify', 'Do you Really Want to quit?'):
        top.quit()

def show_rating():
	text.delete(1.0,END)
	handle = var.get()
	if handle == '':
		messagebox.showerror('Error','Please Enter the Handle of codechef')
		return
	string=get_rating(handle)
	text.insert(INSERT, string)

def open_dir():
	global directory
	directory = filedialog.askdirectory()
	text.delete(1.0,END)
	text.insert(INSERT,directory)

def download_solution():
	if handle == '':
		messagebox.showerror('Error','Please Enter the Handle of codechef')
		return
	codechef_solutions(text,'modi_0505')
	#for x in range(100):text.insert(INSERT,str(x)+'\n')

Label(top, text="Codechef Handle",font=3).grid(row=0)

var1=IntVar()
codes=Checkbutton(top, text='Download all codes as Contest Wise', variable=var1).grid(row=1, column=0,stick=W,pady=4)

var=StringVar()
e=Entry(top, textvariable=var,width=15)
e.grid(row=0, column=1)
handle="*"

def showme():
	global handle
	#handle=var.get()
	text.insert(INSERT, handle)
	#code(handle,directory)
	
	#text.insert(0.0,handle)



Button(top, text='Directory',command=open_dir).grid(row=4,column=0, sticky=W, pady=4)
Button(top, text='Display Rating',command=show_rating).grid(row=6, column=0)
Button(top, text='Download', command=download_solution).grid(row=5, column=0,sticky=W, pady=10)
Button(top, text='Quit',command=callback).grid(row=5, sticky=E, column=1, padx=5, pady=4)
Button(top, text='show me',command=showme).grid(row=7,column=0, sticky=W, pady=4)
#codechef_solutions(handle, directory)


#print("HAN",handle,'\n','DIRE=',directory,flush=True)

text.pack()
#var =IntVar()
#c2=Checkbutton(top, text='female', variable=IntVar()).grid(row=20,column=77)
'''
Radiobutton(top, text='GfG', variable=var, value=1).pack(anchor=W)
Radiobutton(top, text='MIT', variable=var, value=2).pack(anchor=W)
#messagebox.showinfo('information', 'Created in python')
#ttk.Button(top,text="hello shubham").grid()
'''
top.mainloop()