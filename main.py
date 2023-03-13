from tkinter import*
from PIL import Image, ImageTk
import os

vobrazky = []
promeny = []

okno = Tk()

okno.geometry('600x700')
okno.title("Hamburgr konfigurace")


# nazev formu
nazev_form = Label(okno, text="Konfigurátor burgeru",width=20,font=("bold", 40))
nazev_form.pack()
# nazev burgeru
nazev_burgeru = Label(okno, text="Nazev burgeru",width=20,font=("bold", 16))
nazev_burgeru.pack()

nazev_burgeru_vstup = Entry(okno)
nazev_burgeru_vstup.pack()

# propečenost masa burgeru
propecenost = Label(okno, text="Vyberte propečenost masa",width=20,font=("bold", 16))
propecenost.pack()

propecenost_vyber = IntVar() # propecenost_vyber je variable ke který přiřazuju radiobuttony
Radiobutton(okno, text="Well-Done",padx = 5, variable=propecenost_vyber, value=1).pack()
Radiobutton(okno, text="Medium-Well",padx = 5, variable=propecenost_vyber, value=2).pack()
Radiobutton(okno, text="Medium",padx = 5, variable=propecenost_vyber, value=3).pack()
Radiobutton(okno, text="Rare",padx = 5, variable=propecenost_vyber, value=4).pack()
Radiobutton(okno, text="Medium-Rare",padx = 5, variable=propecenost_vyber, value=5).pack()
Radiobutton(okno, text="Blue-Rare",padx = 5, variable=propecenost_vyber, value=6).pack()

# druhy_zemli
druhy_zemli = ["Klasická", "Sezamová", "Bramborová", "Kaiserka", "Ciabatta"]
clicked = StringVar()
clicked.set("Klasická")
drop = OptionMenu( okno , clicked , *druhy_zemli )

zemle = Label(okno, text="Vyberte druh žemle", width=20, font=("bold", 16))
zemle.pack()
drop.pack()


# zelenina
zelenina = Label(okno, text="Vyberte si zeleninu", width =20, font=("bold", 16))
zelenina.pack()

rajce_vyber = IntVar()
salat_vyber = IntVar()
okurka_vyber = IntVar()
cibule_vyber = IntVar()

Checkbutton(okno, text="rajče",variable=rajce_vyber).pack()
Checkbutton(okno, text="salát",variable=salat_vyber).pack()
Checkbutton(okno, text="okurka",variable=okurka_vyber).pack()
Checkbutton(okno, text="cibule",variable=cibule_vyber).pack()

# omacky
omacky = ["Kečup", "Majonéza", "BBQ", "Texaský dresing"]
vyber_omacky = StringVar()
vyber_omacky.set("Kečup")
drop_omacky = OptionMenu( okno , vyber_omacky , *omacky )

omacky_text = Label(okno, text="Vyberte omačku", width=20, font=("bold", 16))
omacky_text.pack()
drop_omacky.pack()

#submit
def exit():
    okno.destroy()

def submit():
    for widgets in okno.winfo_children():
        widgets.destroy()
    with os.scandir('img/') as entries:
        for entry in entries:
            print(entry.name)
        # if .get() == True:
        #     load = Image.open(entry)
        #     render = ImageTk.PhotoImage(load)
        #     photo = Label(okno, width=100, image=render)
        #     vobrazky.append(render)
        #     photo.pack()

    Button(okno, text='Zavřít', width=20, command=exit).pack()



Button(okno, text='Submit',width=20, command=submit).pack()

okno.mainloop()
