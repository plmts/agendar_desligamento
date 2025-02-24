import os
import tkinter as tk
from tkinter import messagebox

def agendar_desligamento(tempo):
    segundos = tempo * 60
    confirmacao = messagebox.askyesno("Desligando...", f"Tem certeza que deseja desligar o computador em {tempo} minutos? ")
    if confirmacao:
        messagebox.showinfo("Agendamento", f"O computador será desligado em {tempo} minutos.")
        os.system(f"shutdown -s -t {segundos}")

def cancelar_desligamento():
    messagebox.showinfo("Cancelamento", "Cancelando o desligamento.")
    os.system("shutdown -a" if os.name == "nt" else "shutdown -c")

def agendar():
    try:
        minutos = int(entry_minutos.get())
        agendar_desligamento(minutos)
    except ValueError:
        messagebox.showinfo("Erro", "Por favor, insira um número válido.")


def criar_interface():
    global entry_minutos
    root = tk.Tk()
    root.title("Desligamento Automático.")
    root.geometry("300x200")

    tk.Label(root, text="Em quantos minutos deseja deseligar o computador? ").pack(pady=10)
    entry_minutos = tk.Entry(root)
    entry_minutos.pack(pady=5)

    tk.Button(root, text="Agendar", command=agendar).pack(pady=5)
    tk.Button(root, text="Cancelar", command=cancelar_desligamento).pack(pady=5)
    tk.Button(root, text="Sair", command=root.quit).pack(pady=5)

    root.mainloop()


if __name__ == "__main__":
    criar_interface()