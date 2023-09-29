#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 17:25:59 2023

@author: Ayaan
"""
# name="Hi my name is Ayaan"
# print(name.split("a"))
# print(name.split(" ")[4])
from tkinter import*
from PIL import ImageTk, Image
from tkinter import filedialog
import os
from tkinter import messagebox
import webbrowser
root=Tk()
root.title("Html Editor")
root.minsize(650,650)
root.maxsize(650,650)
open_img=ImageTk.PhotoImage(Image.open("open.png"))
save=ImageTk.PhotoImage(Image.open("save.png"))
close=ImageTk.PhotoImage(Image.open("run.png"))
file_name=""
def open_file():
    global file_name
    global file
    text_area.delete(1.0,END)
    new_name.delete(0,END)
    html_file=filedialog.askopenfilename(title="open html file",filetypes=(("html files","*.html"),))
    print(html_file)
    file_name=html_file
    file=os.path.basename(file_name)
    real_file=file.split(".")[0]
    print(real_file)
    new_name.insert(END, real_file)
    text_file=open(file,"r")
    content=text_file.read()
    text_area.insert(END,content)
    text_file.close()
open_button=Button(root,image=open_img,command=open_file)
open_button.place(relx=0.03,rely=0.03)
def save_file():
    global file_name
    if file_name == "":
        file_name=new_name.get()+".txt"
    text_file=open(file_name,"w")
    content= text_area.get(1.0,END)
    text_file.write(content)
    messagebox.showinfo("Success","Your changes have been saved!")
save_button=Button(root,image=save,command=save_file)
save_button.place(relx=0.1,rely=0.03)
def run_file():
    global file
    webbrowser.open_new("file://"+file)
save_as_button=Button(root,image=close,command=run_file)
save_as_button.place(relx=0.17,rely=0.03)
name=Label(root, text="File name:")
name.place(relx=0.4,rely=0.03)
new_name=Entry(root)
new_name.insert(0,"")
new_name.place(relx=0.5,rely=0.03)
text_area=Text(root, height=45, width=90)
text_area.place(relx=0.5,rely=0.54,anchor=CENTER)
root.mainloop()