import tkinter as tk
from os.path import basename, splitext
import os
from tkinter import ANCHOR, Frame, Listbox, END, Radiobutton
from turtle import color



class Application(tk.Tk):

    nazev = basename(splitext(basename(__file__.capitalize()))[0])
    nazev = "Směnárna"
    

    def __init__(self):

        self.seznam_men()
        super().__init__(className=self.nazev)

        self.title(self.nazev)
        self.bind("<Escape>", self.quit)
        self.protocol("WM_DELETE_WINDOW", self.quit)



        #info
        self.varEntry = tk.IntVar()
        #1
        self.var_nakup = tk.Variable()
        #2
        self.var_prodej = tk.Variable()
        #3
        self.var_pocet = tk.Variable()
        #4      
        self.var_celkove = tk.Variable()
        #5
        self.var_proved = tk.StringVar()
        self.var_proved.set("Prodej")


        
        tabulka = (self.register(self.callback))

        self.entry = tk.Entry(self, validate="all", validatecommand=(tabulka, '%P'), width = 5, textvariable = self.varEntry)
        self.entry.grid(row = 1, column = 1)


        self.btn_preved = tk.Button(self, text = "Proveď", command = self.preved, width = 14, border = 4, background = "#555555")
        self.btn_preved.grid(row = 2, column = 1)


        self.btn_quit = tk.Button(self, text = "Zavřít", command = self.quit)
        self.btn_quit.grid(row = 3, column = 1)
        
        
        self.lbl_na = tk.Label(self, text = "Tržní cena: ")
        self.lbl_na.grid(row = 5, column = 1, sticky = "w")
        
        self.lbl_nakup = tk.Label(self, textvariable = self.var_nakup)
        self.lbl_nakup.grid(row = 5, column = 2)


        self.lbl_pro = tk.Label(self, text = "Prodejní cena: ")
        self.lbl_pro.grid(row = 6, column = 1, sticky = "w") 
        
        self.lbl_prodej = tk.Label(self, textvariable = self.var_prodej)
        self.lbl_prodej.grid(row = 6, column = 2)


        self.lbl_nas = tk.Label(self, text = "Počet: ")
        self.lbl_nas.grid(row = 7, column = 1, sticky = "w")
        
        self.lbl_pocet = tk.Label(self, textvariable = self.var_pocet)
        self.lbl_pocet.grid(row = 7, column = 2)


        self.lbl_vys = tk.Label(self, text = "Celkově: ")
        self.lbl_vys.grid(row = 8, column = 1, sticky = "w")
        
        self.lbl_vysledek = tk.Label(self, textvariable = self.var_celkove)
        self.lbl_vysledek.grid(row = 8, column = 2)


        self.listbox = Listbox(self, width = 20, height= 16)
        self.listbox.grid(row = 4, column = 1, pady = 5)
        self.listbox.bind("<ButtonRelease-1>", self.klik)
        


        proved = [("Prodej", "prodej"), ("Nákup", "nakup")] 
        
        self.frame = Frame(self)
        self.frame.grid(row = 1, column = 2)
        
        for text, proved in proved: 
            b = Radiobutton(self.frame, text = text, variable = self.var_proved, value = proved)
            b.pack()

        for i in range(0, len(self.listek)):
            self.listbox.insert(END, self.listek[i][0])



    def klik(self, event):
        
        index = self.listbox.curselection()[0]
        self.var_nakup.set(self.listek[index][3])
        self.var_prodej.set(self.listek[index][2])
        self.var_pocet.set(self.listek[index][1])



    def callback(self, P):
        
        if str.isdigit(P) or P == "":
            return True

        else:
            return False
    


    def preved(self):
        
        for i in range(0, len(self.listek)):
            if self.listek[i][0] == self.listbox.get(ANCHOR):
                poloha = i

        self.nasobek = self.listek[poloha][1]
        self.pocet = self.varEntry.get()
        
        proved = self.var_proved.get()
        if proved == "prodej":
            self.cislo = self.listek[poloha][2]
        
        else:
            self.cislo = self.listek[pozice][3]
        self.vysledek = self.pocet // float(self.nasobek) * float(self.cislo)
        self.var_celkove.set(self.vysledek)



    def seznam_men(self):
        
        if os.path.exists(f"listek.txt"):
            with open(f"listek.txt", "r") as file:
                
                listek_samotny = file.readlines()
                self.listek = []
                
                for i in range(0, len(listek_samotny)):
                    self.listek.append(listek_samotny[i].split())
  


    def quit(self, event = None):
        super().quit()


app = Application()
app.mainloop()
