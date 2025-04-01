import tkinter as tk
from tkinter import messagebox
import random

num = random.randint(0, 1000)
resposta = ""

def tentativa():
    global resposta
    
    x = numero.get()
    try:
        x = int(x) 
    except ValueError:
        messagebox.showwarning("Erro", "Insira um número inteiro válido.")
        return
    if x == num:
        resposta = "Você acertou!"
    else:
        if x > num:
            resposta = "Você errou, o número é menor"
        elif x < num:
            resposta = "Você errou, o número é maior"
            
    resposta_label.config(text=resposta)

janela = tk.Tk()
janela.geometry("500x500")
janela.title("Advinhe o número")

text_label = tk.Label(janela, text="Advinhe o número entre 0 e 1000", font=("Helvetica", 20))
text_label.pack(padx=40, pady=40)

numero = tk.Entry(janela, font=("Helvetica", 14))
numero.pack(pady=20)

resposta_label = tk.Label(janela, text=f"{resposta}", font=("Helvetica", 20))
resposta_label.pack(pady=20)

submit_button = tk.Button(janela, text="Enviar", font=("Helvetica", 14), command = tentativa)
submit_button.pack()

janela.mainloop()