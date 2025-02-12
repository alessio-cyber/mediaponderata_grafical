import tkinter as tk
import json
import os

window = tk.Tk()
window.geometry("450x400")
window.title("media_ponderata - v0.3")
window.resizable(False, False)
window.configure(background="#1a1a1a", border=50)

FILE_NAME = os.path.expanduser("~") + "\\AppData\\Roaming\\Mp_Gui\\users.txt"
FOLDER = os.path.expanduser("~") + "\\AppData\\Roaming\\Mp_Gui"
dizionario = {}

utente = tk.StringVar()
media_attuale = tk.DoubleVar()
crediti_attuali = tk.DoubleVar()
voto_nuovo = tk.DoubleVar()
crediti_nuovo = tk.DoubleVar()
risultato = tk.DoubleVar()
lista = tk.StringVar()

utente.set("")
media_attuale.set("")
crediti_attuali.set("")
voto_nuovo.set("")
crediti_nuovo.set("")
risultato.set("")
lista.set("")

def LOAD_DATA():
    global dizionario
    if not os.path.exists(FOLDER):
        os.makedirs(FOLDER)
    if not os.path.exists(FILE_NAME): #Creazione del file se non esiste
        file=open(FILE_NAME, "w+")
        file.close()
 
    check=open(FILE_NAME, "r")
    if check.read(1)!='': #File non vuoto
        with open(FILE_NAME, "r") as file_for_json:
            dizionario = json.load(file_for_json)
    check.close()

def SAVE_DATA():
    with open(FILE_NAME, "w") as file:
        json.dump(dizionario, file, indent=4)

def CALC():
    username = utente.get()
    if not username:
        risultato.set("utente assente!")
        return
    
    MED = media_attuale.get()
    CRED = crediti_attuali.get()
    NEWVOTO = voto_nuovo.get()
    NEWCRED = crediti_nuovo.get()

    if CRED + NEWCRED == 0:
        risultato.set("Error crediti")
        return
    
    if(NEWVOTO < 18 or NEWVOTO > 30):
        risultato.set("voto[18 =< x <= 30]")
        return
    
    if(NEWCRED < 4 or NEWCRED > 16):
        risultato.set("crediti[4 =< x <= 16]")
        return

    risultato_val = (MED * CRED + NEWVOTO * NEWCRED) / (CRED + NEWCRED)
    risultato.set(round(risultato_val, 2))

    dizionario[username] = {"media": media_attuale.get(), "crediti": crediti_attuali.get()}
    SAVE_DATA()

def DELETE():
    media_attuale.set("")
    crediti_attuali.set("")
    voto_nuovo.set("")
    crediti_nuovo.set("")
    risultato.set("")

def NEWOP():
    username = utente.get()
    if not username:
        risultato.set("utente assente!")
        return
    
    media_attuale.set(risultato.get())
    crediti_attuali.set(crediti_attuali.get()+crediti_nuovo.get())

    dizionario[username] = {"media": media_attuale.get(), "crediti": crediti_attuali.get()}
    SAVE_DATA()

    voto_nuovo.set("")
    crediti_nuovo.set("")
    risultato.set("")

def LOAD():
    username = utente.get()
    if username in dizionario:
        media_attuale.set(dizionario[username]["media"])
        crediti_attuali.set(dizionario[username]["crediti"])
    else:
        risultato.set("utente sconosciuto")

def show():
    global dizionario
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r+") as file:
            if os.path.getsize(FILE_NAME)>0:
                dizionario = json.load(file)
                username_formattati = "\n".join(
                    f"User: {user} | Media: {info['media']} | Crediti: {info['crediti']}"
                    for user, info in dizionario.items())
                lista.set(username_formattati)

tk.Label(window, text='user:', font=('calibre', 12, 'bold'), bg='#1a1a1a', fg='white').grid(row=0, column=0, padx=(10,10), sticky="WE")
tk.Entry(window, textvariable=utente, bg="#9966ff" ,font=('calibre', 12, 'bold')).grid(row=0, column=1,)

tk.Label(window, text='media attuale:', font=('calibre', 12, 'bold'), bg='#1a1a1a', fg='white').grid(row=1, column=0, padx=(10,10) ,sticky="WE")
tk.Entry(window, textvariable=media_attuale, bg="#9966ff", font=('calibre', 12, 'bold')).grid(row=1, column=1)

tk.Label(window, text='crediti attuali:', font=('calibre', 12, 'bold'), bg='#1a1a1a', fg='white').grid(row=2, column=0, padx=(10,10), sticky="WE")
tk.Entry(window, textvariable=crediti_attuali, bg="#9966ff", font=('calibre', 12, 'bold')).grid(row=2, column=1)

tk.Label(window, text='nuovo voto:', font=('calibre', 12, 'bold'), bg='#1a1a1a', fg='white').grid(row=3, column=0, padx=(10,10), sticky="WE")
tk.Entry(window, textvariable=voto_nuovo, bg="#9966ff", font=('calibre', 12, 'bold')).grid(row=3, column=1)

tk.Label(window, text='nuovi crediti:', font=('calibre', 12, 'bold'), bg='#1a1a1a', fg='white').grid(row=4, column=0, padx=(10,10), sticky="WE")
tk.Entry(window, textvariable=crediti_nuovo, bg="#9966ff", font=('calibre', 12, 'bold')).grid(row=4, column=1)


tk.Button(window, text='EXE', bg='#1a1a1a', fg='#009900' ,command=CALC, font=('calibre', 12, 'bold'), width=10).grid(row=5, column=0, padx=(10,10), pady=(10,10), sticky="WE")
tk.Button(window, text='DEL', bg='#1a1a1a', fg='#b30000', command=DELETE, font=('calibre',12,'bold'), width=10).grid(row=5, column=1, padx=(10,10), pady=(10,10), sticky="WE")
tk.Button(window, text='NEW', bg='#1a1a1a', fg='#0033cc', command=NEWOP ,font=('calibre',12,'bold'), width=10).grid(row=6, column=0, padx=(10,10), pady=(10,10), sticky="WE")
tk.Button(window, text='LOAD', bg='#1a1a1a', fg='#800080', command=LOAD, font=('calibre',12,'bold'), width=10).grid(row=6, column=1, padx=(10,10), pady=(10,10), sticky="WE")

tk.Label(window, text="media aggiornata:", justify="left", font=('calibre', 12, 'bold'), bg='#1a1a1a', fg='white').grid(row=7, column=0, padx=(10,10), pady=(5,5))
tk.Label(window, textvariable=risultato, justify="left" ,font=('calibre', 12, 'bold')).grid(row=7, column=1, padx=(10,10), pady=(5,5))

tk.Label(window, textvariable=lista, justify="left" ,font=('calibre',10,'bold'), bg='#1a1a1a', fg='white').grid(row=8, column=0, columnspan=2 ,padx=(10,10), pady=(5,5))
show()

LOAD_DATA()
if __name__ == "__main__":
    window.mainloop()