from tkinter import *

def save_info():
    name_info = name.get()
    birth_info = birth.get()
    org_info = org.get()
    tlp_info = tlp.get()
    mail_info = mail.get()

    print(name_info, birth_info, org_info, tlp_info, mail_info)

    file = open('user.txt', 'w')

    file.write('Name: ' + name_info)
    file.write('\n')
    file.write('Birthday: ' + birth_info)
    file.write('\n')
    file.write('Organization: ' + org_info)
    file.write('\n')
    file.write('Tel. No: ' + tlp_info)
    file.write('\n')
    file.write('Mail: ' + mail_info)
    file.close()

root = Tk()

root.title('Registration fishing competition')

root.geometry('500x300')

Label(root, text='Registration', font='helvetica, 15').grid(row=0, column=3)

name_user = Label(root, text='Name')
name_user.grid(row=1, column=2)

birth_user = Label(root, text='Birthday')
birth_user.grid(row=2, column=2)

org_user = Label(root, text='Organization')
org_user.grid(row=3, column=2)

tlp_user = Label(root, text='Tel. number')
tlp_user.grid(row=4, column=2)

mail_user = Label(root, text='Email')
mail_user.grid(row=5, column=2)

name = StringVar()
birth = StringVar()
org = StringVar()
tlp = StringVar()
mail = StringVar()

name_box = Entry(root, textvariable=name)
name_box.grid(row=1, column=3)
birth_box = Entry(root, textvariable=birth)
birth_box.grid(row=2, column=3)

org_box = Entry(root, textvariable=org)
org_box.grid(row=3, column=3)

tlp_box = Entry(root, textvariable=tlp)
tlp_box.grid(row=4, column=3)

mail_box = Entry(root, textvariable=mail)
mail_box.grid(row=5, column=3)

button = Button(root, text='Submit', command=save_info)
button.grid(row=6, column=4)

root.mainloop()
