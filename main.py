from tkinter import*
from PIL import Image, ImageTk
import os

okno = Tk()
okno.geometry('600x700')
# propecenost_vyber je variable ke který přiřazuju radiobuttony
propecenost_vyber = StringVar()
clicked = StringVar()
rajce_vyber = StringVar()
salat_vyber = StringVar()
okurka_vyber = StringVar()
cibule_vyber = StringVar()
vyber_omacky = StringVar()

inputy = [
    propecenost_vyber,
    rajce_vyber,
    salat_vyber,
    okurka_vyber,
    cibule_vyber,
    vyber_omacky
]
transform = {
    "Kečup": "kecup",
    "Majonéza": "majoneza",
    "BBQ": "bbq",
    "Texaský dresing": "texas",
    "Klasická": "zemle",
    "Sezamová": "sezamova",
    "Bramborová": "bramborova",
    "Kaiserka": "kaiserka",
    "Ciabatta": "ciabatta",
    "well_done": "well_done",
    "medium_well": "medium_well",
    "medium": "medium",
    "rare": "rare",
    "medium_rare": "medium_rare",
    "blue_rare": "blue_rare",
    "rajce": "rajce",
    "salat": "salat",
    "okurka": "okurka",
    "cibule": "cibule"
}

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

Radiobutton(okno, text="Well-Done",padx = 5, variable=propecenost_vyber, value="well_done").pack()
Radiobutton(okno, text="Medium-Well",padx = 5, variable=propecenost_vyber, value="medium_well").pack()
Radiobutton(okno, text="Medium",padx = 5, variable=propecenost_vyber, value="medium").pack()
Radiobutton(okno, text="Rare",padx = 5, variable=propecenost_vyber, value="rare").pack()
Radiobutton(okno, text="Medium-Rare",padx = 5, variable=propecenost_vyber, value="medium_rare").pack()
Radiobutton(okno, text="Blue-Rare",padx = 5, variable=propecenost_vyber, value="blue_rare").pack()

# druhy_zemli
druhy_zemli = ["Klasická", "Sezamová", "Bramborová", "Kaiserka", "Ciabatta"]
clicked.set("Klasická")
drop = OptionMenu( okno , clicked , *druhy_zemli )

zemle = Label(okno, text="Vyberte druh žemle", width=20, font=("bold", 16))
zemle.pack()
drop.pack()


# zelenina
zelenina = Label(okno, text="Vyberte si zeleninu", width =20, font=("bold", 16))
zelenina.pack()


Checkbutton(okno, text="rajče",variable=rajce_vyber, onvalue="rajce", offvalue="").pack()
Checkbutton(okno, text="salát",variable=salat_vyber, onvalue="salat", offvalue="").pack()
Checkbutton(okno, text="okurka",variable=okurka_vyber, onvalue="okurka", offvalue="").pack()
Checkbutton(okno, text="cibule",variable=cibule_vyber, onvalue="cibule", offvalue="").pack()

# omacky
omacky = ["Kečup", "Majonéza", "BBQ", "Texaský dresing"]
vyber_omacky.set("Kečup")
drop_omacky = OptionMenu( okno, vyber_omacky, *omacky)

omacky_text = Label(okno, text="Vyberte omačku", width=20, font=("bold", 16))
omacky_text.pack()
drop_omacky.pack()

#submit
def exit():
    okno.destroy()



def submit():
    for widgets in okno.winfo_children():
        widgets.destroy()

    top = Image.open(f"img/{transform[clicked.get()]}_vrsek.png")
    bottom = Image.open(f"img/{transform[clicked.get()]}_spodek.png")
    top = ImageTk.PhotoImage(top)
    bottom = ImageTk.PhotoImage(bottom)
    top_label = Label(okno, image=top, height=70)
    bottom_label = Label(okno, image=bottom, height=70)
    top_label.image = top
    bottom_label.image = bottom
    top_label.pack()
    for input in inputy:
        if input.get() != 0 and input.get() != '':
            load = Image.open(f"img/{transform[input.get()]}.png")
            render = ImageTk.PhotoImage(load)
            photo = Label(okno, height=70, image=render)
            photo.image = render
            photo.pack()
    bottom_label.pack()

    Button(okno, text='Zavřít', width=20, command=exit).pack()



Button(okno, text='Submit',width=20, command=submit).pack()

okno.mainloop()
