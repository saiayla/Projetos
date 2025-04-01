import random
import string
import tkinter as tk
from tkinter import messagebox

def gerar_palavra():
    with open("forca\br-sem-acentos.txt", "r", encoding="utf-8") as p:
        palavras = [linha.strip().lower() for linha in p.readlines()] 
    return random.choice(palavras)

def letra_in_palavra(palavra, letra):
    return letra in palavra

def atualizar_display():
    palavra_oculta = ""
    for letra in palavra:
        if letra in letras_corretas:
            palavra_oculta += letra
        else:
            palavra_oculta += "_"
    palavra_label.config(text=palavra_oculta)
    vidas_label.config(text=f"Vidas restantes: {vidas - tentativas_erradas}")

def jogar():
    global tentativas_erradas
    
    letra = letra_entry.get().lower()  
    if len(letra) != 1 or not letra.isalpha():
        messagebox.showwarning("Entrada inválida", "Por favor, insira apenas uma letra válida.")
        return

    if letra in letras_corretas or letra in letras_erradas:
        messagebox.showinfo("Aviso", "Você já tentou essa letra.")
        return

    if letra_in_palavra(palavra, letra):  
        letras_corretas.append(letra)
        atualizar_display()
        if all(letra in letras_corretas for letra in palavra):  
            messagebox.showinfo("Você venceu!", "Parabéns! Você descobriu a palavra!")
            janela.quit()  
    else:
        tentativas_erradas += 1
        letras_erradas.append(letra)
        atualizar_display()

        if tentativas_erradas >= vidas:  
            messagebox.showinfo("Você perdeu!", "Você perdeu todas as suas vidas. A palavra era: " + palavra)
            janela.quit()  

    letra_entry.delete(0, tk.END)  

palavra = gerar_palavra()
vidas = 10  
tentativas_erradas = 0
letras_corretas = []  
letras_erradas = []  

janela = tk.Tk()
janela.geometry("400x500")
janela.title("Jogo da Forca")

palavra_label = tk.Label(janela, text="", font=("Helvetica", 24))
palavra_label.pack(padx=40, pady=60)

vidas_label = tk.Label(janela, text=f"Vidas restantes: {vidas - tentativas_erradas}", font=("Helvetica", 14))
vidas_label.pack(padx=10, pady=10)

letra_entry = tk.Entry(janela, font=("Helvetica", 14), width=5)
letra_entry.pack(padx=10, pady=10)

submeter_button = tk.Button(janela, text="Tentar", font=("Helvetica", 14), command=jogar)
submeter_button.pack(padx=20, pady=20)

atualizar_display()

janela.mainloop()
