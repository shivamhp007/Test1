import tkinter
from tkinter import ttk
from csv import DictWriter
import os

win = tkinter.Tk()
win.title('Student Records')
# create labels
name_var = tkinter.StringVar()
name_label = ttk.Label(win, text='Name: ')
name_label.grid(row=0, column=0, sticky=tkinter.W)
name_box = ttk.Entry(win, width=20, textvariable=name_var)
name_box.grid(row=0, column=1)

roll_no_var = tkinter.IntVar()
roll_no_label = ttk.Label(win, text='Roll No: ')
roll_no_label.grid(row=1, column=0, sticky=tkinter.W)
roll_no_box = ttk.Entry(win, width=20, textvariable=roll_no_var)
roll_no_box.grid(row=1, column=1)

age_var = tkinter.IntVar()
age_label = ttk.Label(win, text='Age: ')
age_label.grid(row=2, column=0, sticky=tkinter.W)
age_box = ttk.Entry(win, width=20, textvariable=age_var)
age_box.grid(row=2, column=1)

gender_var = tkinter.StringVar()
gender_label = ttk.Label(win, text='Gender: ')
gender_label.grid(row=3, column=0, sticky=tkinter.W)
gender_box = ttk.Combobox(win, text='gender', width=18, textvariable=gender_var, state='readonly')
gender_box['value'] = ('male', 'women', 'other')
gender_box.current(0)
gender_box.grid(row=3, column=1)

view1 = tkinter.Listbox(win, height = 6, width = 35)
view1.grid(row = 7, column = 0, rowspan = 6, columnspan = 2, )


def insert():
    name = name_var.get()
    age = age_var.get()
    roll_no = roll_no_var.get()
    gender = gender_var.get()

    with open('file_detail.csv', 'a', newline='\n') as f:
        csv_writer = DictWriter(f, fieldnames=['NAME', 'ROLL_NO', 'AGE', 'GENDER'])
        if os.stat('file_detail.csv').st_size == 0:
            csv_writer.writeheader()
        csv_writer.writerow({
            'NAME': name,
            'ROLL_NO': roll_no,
            'AGE': age,
            'GENDER': gender,
        })
    name_box.delete(0, tkinter.END)
    roll_no_box.delete(0, tkinter.END)
    age_box.delete(0, tkinter.END)


def delete():
    op = []
    with open('file_detail.csv', 'r+', newline="\n") as f:
        t = f.readlines()
        to_delete = roll_no_var.get()
        print(to_delete)
        # f.seek(0)
        for line in t:
            if str(line.split(",")[1]) != str(to_delete):
                with open ("new_file.csv",'a',newline='\n') as g:
                    g.write(line)
                # f.write(line)
                g.truncate()
        os.remove("file_detail.csv")
        os.rename("new_file.csv","file_detail.csv")
        f.truncate()
    name_box.delete(0, tkinter.END)
    roll_no_box.delete(0, tkinter.END)
    age_box.delete(0, tkinter.END)
    return op


def update():
    with open('file_detail.csv', 'a', newline="\n") as f:
        t = f.read()
        # op = []
        roll_no = roll_no_var.get()
        age_update = age_var.get()
        # print(age_update)
        # f.seek(0)
        for line in t.split('\n'):
            if roll_no in line.split(",")[1]:
                line[2] = age_update
                # if str(to_delete) not in i:
                f.writelines(line)
        f.truncate()
    name_box.delete(0, tkinter.END)
    roll_no_box.delete(0, tkinter.END)
    age_box.delete(0, tkinter.END)


def search():
    op = []
    with open('file_detail.csv', 'r+', newline="\n") as f:
        t = f.read()
        to_search = roll_no_var.get()
        for line in t.split('\n'):
            for i in line.split(","):
                if i == to_search:
                    op.append(line)
        f.truncate()
    name_box.delete(0, tkinter.END)
    roll_no_box.delete(0, tkinter.END)
    age_box.delete(0, tkinter.END)
    print(op)


Insert_button = ttk.Button(win, text="INSERT", command=insert)
Insert_button.grid(row=6, column=0)

Delete_button = ttk.Button(win, text="DELETE", command=delete)
Delete_button.grid(row=6, column=1)

Update_button = ttk.Button(win, text="UPDATE", command=update)
Update_button.grid(row=6, column=2)

Search_button = ttk.Button(win, text="Search", command=search)
Search_button.grid(row=6, column=3)


win.mainloop()