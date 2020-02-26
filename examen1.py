import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox

PREGUNTAS = {
    1: ("Quien descubrio America?", "Cristobal Colon"),
    2: ("Por quien esta nombrado el continente americano?", "Americo Vespucio"),
    3: ("Quien fue el primer presidente estadounidense?", "George Washington"),
    4: ("En que año cayo constantinopla (B.C)", "457"),
    5: ("Elige al menos 1 presidente mexicanos", ("Benito Juarez", "Porfirio Diaz")),
}

PADY = (0, 10)
PADX = (0, 10)


class Checkbutton(ttk.Checkbutton):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.variable = tk.IntVar()
        self.configure(variable=self.variable)

    def isSelected(self) -> bool:
        return self.variable.get() == 1


def calificar():
    respuesta1 = entry_pregunta1.get()
    respuesta2 = entry_pregunta2.get()
    respuesta3 = radio_var.get()
    respuesta4 = radio_var2.get()
    respuestas5 = [
        checkbutton1.isSelected(),
        checkbutton2.isSelected(),
        checkbutton3.isSelected(),
        checkbutton4.isSelected(),
        checkbutton5.isSelected(),
    ]
    print(respuestas5)


root = tk.Tk()
root.columnconfigure(0, weight=1)
root.minsize(640, 480)

frame = ttk.Frame(root)
frame.configure(padding=10)
frame.grid(column=0, row=0)

label_top = ttk.Label(frame, text="Examen de Historia Universal")
label_top.grid(column=0, row=0, columnspan=99, pady=PADY)

label_pregunta1 = ttk.Label(frame, text=PREGUNTAS[1][0], anchor=tk.W)
entry_pregunta1 = ttk.Entry(frame)
label_pregunta1.grid(column=0, row=1, pady=PADY, padx=PADX, sticky="NSWE")
entry_pregunta1.grid(column=1, row=1, pady=PADY, columnspan=99)

label_pregunta2 = ttk.Label(frame, text=PREGUNTAS[2][0], anchor=tk.W)
entry_pregunta2 = ttk.Entry(frame)
label_pregunta2.grid(column=0, row=2, pady=PADY, padx=PADX, sticky="NSWE")
entry_pregunta2.grid(column=1, row=2, pady=PADY, columnspan=99)

frame2 = ttk.Frame(root)
frame2.configure(padding=10)
frame2.grid(column=0, row=1)

label_pregunta3 = ttk.Label(frame2, text=PREGUNTAS[3][0])
label_pregunta3.grid(column=0, row=0, columnspan=99, pady=PADY)
radio_var = tk.StringVar(value="Enrique Peña Nieto")
radiobutton1 = ttk.Radiobutton(
    frame2, variable=radio_var, text="Enrique Peña Nieto", value="Enrique Peña Nieto"
)
radiobutton2 = ttk.Radiobutton(
    frame2, variable=radio_var, text="Barack Obama", value="Barack Obama"
)
radiobutton3 = ttk.Radiobutton(
    frame2, variable=radio_var, text=PREGUNTAS[3][1], value=PREGUNTAS[3][1]
)
radiobutton1.grid(column=0, row=1, padx=PADX, pady=PADY)
radiobutton2.grid(column=1, row=1, padx=PADX, pady=PADY)
radiobutton3.grid(column=2, row=1, padx=PADX, pady=PADY)

label_pregunta4 = ttk.Label(frame2, text=PREGUNTAS[4][0])
label_pregunta4.grid(column=0, row=2, columnspan=99, pady=PADY)
radio_var2 = tk.StringVar(value="420")
radiobutton4 = ttk.Radiobutton(frame2, variable=radio_var2, text="420", value="420")
radiobutton5 = ttk.Radiobutton(frame2, variable=radio_var2, text="928", value="928")
radiobutton6 = ttk.Radiobutton(
    frame2, variable=radio_var2, text=PREGUNTAS[4][1], value=PREGUNTAS[4][1]
)
radiobutton4.grid(column=0, row=3, padx=PADX)
radiobutton5.grid(column=1, row=3, padx=PADX)
radiobutton6.grid(column=2, row=3, padx=PADX)

frame3 = ttk.Frame(root)
frame3.configure(padding=10)
frame3.grid(column=0, row=2)

label_pregunta5 = ttk.Label(frame3, text=PREGUNTAS[5][0])
label_pregunta5.grid(column=0, row=0, columnspan=99, pady=PADY)

checkbutton1 = Checkbutton(frame3, text="George Washington")
checkbutton2 = Checkbutton(frame3, text="Pedro Caza")
checkbutton3 = Checkbutton(frame3, text="Barack Obama")
checkbutton4 = Checkbutton(frame3, text=PREGUNTAS[5][1][0])
checkbutton5 = Checkbutton(frame3, text=PREGUNTAS[5][1][1])

checkbutton1.grid(column=0, row=1, padx=PADX, pady=PADY)
checkbutton2.grid(column=1, row=1, padx=PADX, pady=PADY)
checkbutton3.grid(column=2, row=1, padx=PADX, pady=PADY)
checkbutton4.grid(column=3, row=1, padx=PADX, pady=PADY)
checkbutton5.grid(column=4, row=1, padx=PADX, pady=PADY)

frame4 = ttk.Frame(root)
frame4.configure(padding=10)
frame4.grid(column=0, row=3)

calificar = ttk.Button(frame4, text="Calificar", command=calificar)
calificar.grid()

root.mainloop()


main()
