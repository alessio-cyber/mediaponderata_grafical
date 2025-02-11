import tkinter as tk

window = tk.Tk()
window.geometry("450x400")
window.title("media ponderata - prototipo")
window.resizable(False, False)
window.configure(background="#1a1a1a", border=50)


media_attuale = tk.DoubleVar()
crediti_attuali = tk.DoubleVar()
voto_nuovo = tk.DoubleVar()
crediti_nuovo = tk.DoubleVar()
risultato = tk.DoubleVar()

media_attuale.set("")
crediti_attuali.set("")
voto_nuovo.set("")
crediti_nuovo.set("")
risultato.set("")




def CALC():
    MED = media_attuale.get()
    CRED = crediti_attuali.get()
    NEWVOTO = voto_nuovo.get()
    NEWCRED = crediti_nuovo.get()

    if CRED + NEWCRED == 0:
        risultato.set("Error crediti")
        return

    risultato_val = (MED * CRED + NEWVOTO * NEWCRED) / (CRED + NEWCRED)
    risultato.set(round(risultato_val, 2))


def DELETE():
    media_attuale.set("")
    crediti_attuali.set("")
    voto_nuovo.set("")
    crediti_nuovo.set("")
    risultato.set("")


def NEWOP():
    media_attuale.set(risultato.get())
    crediti_attuali.set(crediti_attuali.get()+crediti_nuovo.get())
    voto_nuovo.set("")
    crediti_nuovo.set("")
    risultato.set("")





tk.Label(window, text='media attuale:', justify="left", bg="#1a1a1a", fg="white", font=('calibre', 12, 'bold')).grid(row=0, column=0, padx=(10,10), pady=(5,5))
tk.Entry(window, textvariable=media_attuale, font=('calibre', 12, 'normal')).grid(row=0, column=1)

tk.Label(window, text='crediti attuali:', justify="left", bg="#1a1a1a", fg="white", font=('calibre', 12, 'bold')).grid(row=1, column=0, padx=(10,10), pady=(5,5))
tk.Entry(window, textvariable=crediti_attuali, font=('calibre', 12, 'normal')).grid(row=1, column=1)

tk.Label(window, text='nuovo voto:', justify="left", bg="#1a1a1a", fg="white", font=('calibre', 12, 'bold')).grid(row=2, column=0, padx=(10,10), pady=(5,5))
tk.Entry(window, textvariable=voto_nuovo, font=('calibre', 12, 'normal')).grid(row=2, column=1)

tk.Label(window, text='nuovi crediti:', justify="left", bg="#1a1a1a", fg="white", font=('calibre', 12, 'bold')).grid(row=3, column=0, padx=(10,10), pady=(5,5))
tk.Entry(window, textvariable=crediti_nuovo, font=('calibre', 12, 'normal')).grid(row=3, column=1)

tk.Button(window, text='EXE', bg='green' ,command=CALC, font=('calibre', 12, 'bold'), width=10).grid(row=4, column=0, padx=10, pady=10, sticky="WE")
tk.Button(window, text='DEL', bg='red', command=DELETE, font=('calibre',12,'bold'), width=10).grid(row=4, column=1, padx=10, pady=10 ,sticky="WE")
tk.Button(window, text='NEW', bg='blue', command=NEWOP ,font=('calibre',12,'bold'), width=10).grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="WE")

tk.Label(window, text="media aggiornata:", justify="left", bg="#1a1a1a", fg="white", font=('calibre', 12, 'bold')).grid(row=6, column=0, padx=(10,10), pady=(5,5))
tk.Label(window, textvariable=risultato, justify="left", bg="#1a1a1a", fg="white", font=('calibre', 12, 'bold')).grid(row=6, column=1, padx=(10,10), pady=(5,5))





if __name__ == "__main__":
    window.mainloop()