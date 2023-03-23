import tkinter as Tk
import random
import os
import string

def generate_pass():
    lenght = int(lenght_ent.get())
    password_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_chars) for long in range(lenght))

    btn_save = Tk.Button(text='Сохранить пароль', command=save_pass)
    btn_save.place(x=100, y=225)
    return password 

def save_pass():
    lenght = int(lenght_ent.get())
    amount = int(pasamount_ent.get())
    with open('passwords_user.txt', 'w') as file:
        for count in range(amount):
            password = generate_pass()
            file.write(password + '\n')


root = Tk.Tk()
root.geometry('300x300')
root.configure(background='#1F75FE')
root.title('Password Generator')


info_lbl = Tk.Label(text='Сгенерируйте пароль!\n Введите длинну пароля в окно ввода!', background='#1F75FE', fg='#FFFFFF')
info_lbl.place(x=50, y=50)
pasamount_lbl = Tk.Label(text='Введите количество экземпляров паролей', background='#1F75FE', fg='#FFFFFF')
pasamount_lbl.place(x=50, y=125)

lenght_ent = Tk.Entry()
lenght_ent.place(x=90, y=95)
pasamount_ent = Tk.Entry()
pasamount_ent.place(x=90, y=155)

confirm_btn = Tk.Button(text='Генерация', background='#1F75FE', fg='#FFFFFF', command=generate_pass)
confirm_btn.place(x=115,y=180)


root.mainloop()