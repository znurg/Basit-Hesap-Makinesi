import tkinter as tk

pencere = tk.Tk()
pencere.title("HESAP MAKİNESİ")
pencere.geometry("350x350")
pencere.resizable(False, False)
pencere.config(bg="azure")

ekran = tk.Entry(pencere, fg="black", bg="white", font="Times 17 italic", width=20, borderwidth=5)
ekran.pack()

def sayi_gir(sayi):
    islem = ekran.get()
    ekran.delete(0, tk.END)
    ekran.insert(0, islem + str(sayi))

def islem_gir(matematik):
    islem = ekran.get()
    ekran.delete(0, tk.END)
    ekran.insert(0, islem + str(matematik))

def esittir():
    islem = ekran.get()
    ekran.delete(0, tk.END)
    try:
        islem = islem.replace('X', '*')
        cevap = str(eval(islem))
        ekran.insert(0, cevap)
    except Exception as e:
        ekran.insert(0, "HATA")
def temizle():
    ekran.delete(0, tk.END)

buton1 = tk.Button(pencere, text="1", padx=20, pady=20, fg="black", bg="LightSkyBlue1", command=lambda: sayi_gir(1))
buton1.place(x=15, y=45)
buton2 = tk.Button(pencere, text="2", padx=20, pady=20, fg="black", bg="LightSkyBlue1", command=lambda: sayi_gir(2))
buton2.place(x=80, y=45)
buton3 = tk.Button(pencere, text="3", padx=20, pady=20, fg="black", bg="LightSkyBlue1", command=lambda: sayi_gir(3))
buton3.place(x=145, y=45)
buton4 = tk.Button(pencere, text="4", padx=20, pady=20, fg="black", bg="LightSkyBlue1", command=lambda: sayi_gir(4))
buton4.place(x=15, y=120)
buton5 = tk.Button(pencere, text="5", padx=20, pady=20, fg="black", bg="LightSkyBlue1", command=lambda: sayi_gir(5))
buton5.place(x=80, y=120)
buton6 = tk.Button(pencere, text="6", padx=20, pady=20, fg="black", bg="LightSkyBlue1", command=lambda: sayi_gir(6))
buton6.place(x=145, y=120)
buton7 = tk.Button(pencere, text="7", padx=20, pady=20, fg="black", bg="LightSkyBlue1", command=lambda: sayi_gir(7))
buton7.place(x=15, y=195)
buton8 = tk.Button(pencere, text="8", padx=20, pady=20, fg="black", bg="LightSkyBlue1", command=lambda: sayi_gir(8))
buton8.place(x=80, y=195)
buton9 = tk.Button(pencere, text="9", padx=20, pady=20, fg="black", bg="LightSkyBlue1", command=lambda: sayi_gir(9))
buton9.place(x=145, y=195)
buton0 = tk.Button(pencere, text="0", padx=20, pady=20, fg="black", bg="LightSkyBlue1", command=lambda: sayi_gir(0))
buton0.place(x=15, y=270)
buton_virgul = tk.Button(pencere, text=".", padx=20, pady=20, fg="black", bg="LightSkyBlue1", command=lambda: sayi_gir("."))
buton_virgul.place(x=80, y=270)
buton_esittir = tk.Button(pencere, text="=", padx=20, pady=20, fg="black", bg="LightSkyBlue1", command=esittir)
buton_esittir.place(x=145, y=270)

buton_topla = tk.Button(pencere, text="+", padx=30, pady=10, fg="black", bg="thistle", command=lambda: islem_gir("+"))
buton_topla.place(x=250, y=45)
buton_cikar = tk.Button(pencere, text="-", padx=30, pady=10, fg="black", bg="thistle", command=lambda: islem_gir("-"))
buton_cikar.place(x=250, y=100)
buton_carp = tk.Button(pencere, text="*", padx=30, pady=10, fg="black", bg="thistle", command=lambda: islem_gir("*"))
buton_carp.place(x=250, y=170)
buton_bol = tk.Button(pencere, text="/", padx=30, pady=10, fg="black", bg="thistle", command=lambda: islem_gir("/"))
buton_bol.place(x=250, y=230)
buton_sil = tk.Button(pencere, text="C", padx=30, pady=10, fg="black", bg="thistle", command=temizle)
buton_sil.place(x=250, y=290)


pencere.mainloop()