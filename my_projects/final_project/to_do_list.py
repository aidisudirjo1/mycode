#!/usr/bin/python3

import tkinter
import tkinter.messagebox
import pickle

root = tkinter.Tk()
root.title("To-do List")

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_task.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Hold Up!", message="What we doing? ")    

def delete_tasks():
    try:
        task_index = listbox_task.curselection()[0]
        listbox_task.delete(task_index)
    except:
         tkinter.messagebox.showwarning(title="Wait!", message="What are we done with?")

def save_tasks():
    tasks = listbox_task.get(0, listbox_task.size())
    pickle.dump(tasks, open("task.dat","wb"))

def load_tasks():
    tasks = pickle.load(open("task.dat", "rb"))
    for task in tasks:
        listbox_task.insert(tkinter.END, task)




#GUI
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

listbox_task = tkinter.Listbox(frame_tasks, height=10, width= 55)
listbox_task.pack()

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_task.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_task.yview)


entry_task = tkinter.Entry(root, width=50)
entry_task.pack()

button_add_task = tkinter.Button(root, text="Add To Do's..", width=50, command=add_task)
button_add_task.pack()

button_delete_task = tkinter.Button(root, text="Done!", width=50, command=delete_tasks)
button_delete_task.pack()

button_save_task = tkinter.Button(root, text="Save To Do's", width=50, command=save_tasks)
button_save_task.pack()

button_load_tasks = tkinter.Button(root, text="Load", width=50, command=load_tasks)
button_load_tasks.pack()


root.mainloop() 
