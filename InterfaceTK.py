from tkinter import *

jan = Tk()
jan.title('TELA DE LOGIN')
jan.geometry('700x500')
jan.configure(bg='white')
jan.resizable(width=False, height=False)
ladodireito = Frame(jan, width=350, height=500, bg='MIDNIGHTBLUE', relief='raised')
ladodireito.pack(side=RIGHT)
ladoesquerdo = Frame(jan, width=340, height=500, bg='black', relief='raised')
ladoesquerdo.pack(side=LEFT)
jan.mainloop()
