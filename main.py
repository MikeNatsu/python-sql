from tkinter import *
import sqlite3

root = Tk()
root.geometry('600x450')
root.title("Formulario de registro")


nombrec=StringVar()
Email=StringVar()
Ciudad=StringVar()
Matricula=StringVar()



def database():
    nombre=nombrec.get()
    email=Email.get()
    ciudad=Ciudad.get()
    matricula=Matricula.get()
    conn = sqlite3.connect('Form.db')
    with conn:
      cursor=conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS People (nombrec TEXT,Email TEXT,Ciudad TEXT,Matricula TEXT)')
    cursor.execute('INSERT INTO People (nombrec,Email,Ciudad,Cedula) VALUES(?,?,?,?)',(nombre,email,ciudad,matricula,))
    conn.commit()

label_0 = Label(root, text="Formulario de Registro", width=20,font=("bold", 20))
label_0.place(x=90,y=53)

label_1 = Label(root, text="Nombre Completo", width=20,font=("bold", 10))
label_1.place(x=80, y=130)

entry_1 = Entry(root,textvar=nombrec)
entry_1.place(x=240, y=130)

label_2 = Label(root, text="Email", width=20,font=("bold", 10))
label_2.place(x=68, y=180)

entry_2 = Entry(root,textvar=Email)
entry_2.place(x=240, y=180)

label_3 = Label(root, text="Matricula", width=20,font=("bold", 10))
label_3.place(x=68, y=230)

entry_3 = Entry(root,textvar=Matricula)
entry_3.place(x=240, y=230)

label_4 = Label(root, text="Ciudad",width=20,font=("bold", 10))
label_4.place(x=70,y=280)
 
list1 = ['Santo Domingo','Santiago','Samaná','Punta Cana','Puesto Plata','Bonao'];
 
droplist=OptionMenu(root,Ciudad, *list1)
droplist.config(width=18)
Ciudad.set('Selecciona tu ciudad') 
droplist.place(x=240,y=280)


Button(root, text='Guardar',width=20,bg='cyan',fg='black',command=database).place(x=180,y=380)

root.mainloop()