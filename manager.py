import tkinter
import tkinter.messagebox
import pickle

root = tkinter.Tk()
root.title("Task Manager 5600")


wrapper = tkinter.Frame(root)
wrapper.pack()

tasks_box = tkinter.Listbox(wrapper, height=15, width=50)
tasks_box.pack(side=tkinter.LEFT)

entry_task = tkinter.Entry(root, width=50)
entry_task.pack()

scrollbar = tkinter.Scrollbar(wrapper)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

tasks_box.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=tasks_box.yview)


# load tasks
def pre_load_tasks():
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        tasks_box.delete(0, tkinter.END)
        for task in tasks:
            tasks_box.insert(tkinter.END, task)
    #if no tasks.dat file
    except:
        dat_file = pickle.dump((), open("tasks.dat", "wb"))

pre_load_tasks()


def add_task():
    task = entry_task.get()
    if task:
        tasks_box.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="NO", message="Empty?")

def delete_task():
    try:
        task = tasks_box.curselection()[0]
        tasks_box.delete(task)
    except:
        tkinter.messagebox.showwarning(title="WHAT", message="Choose a task to delete.")


def save_task():
    tasks = tasks_box.get(0, tasks_box.size())
    pickle.dump(tasks, open("tasks.dat", "wb"))




add_task_btn = tkinter.Button(root, text="Add task", width=43, command=add_task)

delete_task_btn = tkinter.Button(root, text="Delete task", width=43, command=delete_task)

save_task_btn = tkinter.Button(root, text="Save tasks", width=43, command=save_task)

add_task_btn.pack()
delete_task_btn.pack()
save_task_btn.pack()



root.mainloop()

