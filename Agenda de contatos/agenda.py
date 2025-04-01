import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

contatos = []

def adicionar():
    nome_valor = nome.get()
    tel_valor = tel.get()
    
    if len(tel_valor) != 9 or not tel_valor.isdigit():
        messagebox.showwarning("Erro", "Insira um número de telefone válido.")
    else:
        if nome_valor in contatos and tel_valor in contatos:
            messagebox.showwarning("Erro", "Contato já existe.")
            
        else:
            contatos.append({'nome': nome_valor, 'telefone': tel_valor})
            messagebox.showinfo("Sucesso", "Nome e telefone adicionados com sucesso!")
            nome.delete(0, tk.END)
            tel.delete(0, tk.END)
            mostrar_contatos()
        
def mostrar_contatos():
    for widget in lista_contatos.winfo_children():
        widget.destroy()
    for contato in contatos:
        contato_frame = tk.Frame(lista_contatos)
        contato_frame.pack(pady=5, fill="x")
        
        texto_contato = tk.Label(contato_frame, text=f"{contato['nome']} - {contato['telefone']}", font=("Arial", 10))
        texto_contato.pack(side="left", padx=10)
        
        remove_btn = ttk.Button(contato_frame, text="Remover", command=lambda c=contato: remover(c))
        remove_btn.pack(side="right", padx=10)

def remover(contato):
    contatos.remove(contato)
    mostrar_contatos()

janela = tk.Tk()
janela.geometry("500x500")
janela.title("Agenda de contatos")

frame = tk.Frame(janela, bg="#579AB9", width=500, height=500)
frame.pack(expand=True, fill=tk.BOTH)

title_lable = tk.Label(frame, text="Agenda de contatos", font=("Arial", 20))
title_lable.pack(padx=10, pady=10)

nome_label = tk.Label(frame, bg="#579AB9", text="Nome:", font=("Arial", 12))
nome_label.pack()
nome = tk.Entry(frame)
nome.pack(pady= 10, padx=10)

tel_label = tk.Label(frame, bg="#579AB9", text="Telefone:", font=("Arial", 12))
tel_label.pack()
tel = tk.Entry(frame)
tel.pack(pady= 10, padx=10)

submit = ttk.Button(frame, text="Adicionar", command = adicionar)
submit.pack(pady= 20, padx=20)

contato_label = tk.Label(frame, text="Contatos:", font=("Arial", 12))
contato_label.pack(pady=20)
lista_contatos = tk.Frame(frame)
lista_contatos.pack(padx=20, pady=20, fill="both", expand=True)

janela.mainloop()