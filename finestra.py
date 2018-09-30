from tkinter import *
from tkinter import messagebox
def uscire():
    a=messagebox.askyesno(title="Uscire",message="Vuoi davvero uscire")
    if a==True:
        fin.destroy()

fin=Tk()
fin.title("Reverse string")
fin.config(width=600, height=400, bg="aliceblue")
barra = Menu(fin)
barramenu = Menu(barra)
barramenu.add_command(label="Exit",command=uscire)
barra.add_cascade(label="Menu",menu=barramenu)
fin.config(menu=barra)
c=Label(fin, text="Inserire testo: ",font=("Microsoft New Tai Lue",16),bg="aliceblue",).grid(row=1,column=1)
f=StringVar()
c1=Entry(fin,width=50,textvariable=f,font=("Microsoft New Tai Lue",11)).grid(row=1,column=2)
c2=Label(fin,text="Testo invertito:",font=("Microsoft New Tai Lue",16),bg="aliceblue").grid(row=3,column=1)

def reverse():
    v=f.get()
    a=len(v)
    d=""
    while a>0:
        a-=1
        d=d+v[a]
    h=StringVar()
    c3=Label(fin,text="",font=("Microsoft New Tai Lue",14),textvariable=h,anchor="w",bg="aliceblue").grid(row=3,column=2)
    if v=="":
        h.set("Errore, reinserire testo")
    else:h.set(d)

c4=Button(fin,text="Clicca qui",command=reverse,font=("Microsoft New Tai Lue",11),bg="azure").grid(row=3,column=3)
fin.mainloop()


