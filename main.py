import tkinter as tk
from tkinter import ttk


def calcular():
    try:
        valor = float(entrada.get())
        resultado.set(valor)
    except ValueError:
        resultado.set("Erro: Digite um número válido")

# Janela principal
root = tk.Tk()
root.title("Calculadora De Altura")
root.geometry("400x200")

# Criação de um estilo personalizado para o botão ttk
style = ttk.Style()
style.configure("Estilo.TButton", font=("Helvetica", 12), padding=10, foreground="#333", background="#CCC", borderwidth=2)

# Variáveis para armazenar entrada e resultado
entrada = ttk.Entry(root)
resultado = tk.StringVar()

# Layout
ttk.Label(root, text="Calculadora De Altura", font=("Helvetica", 16)).pack(pady=10)
entrada.pack(pady=10)

# Usando o estilo personalizado para o botão ttk
calcular_button = ttk.Button(root, text="Calcular Altura", command=calcular, style="Estilo.TButton")
calcular_button.pack(pady=10)

ttk.Label(root, text="A Sua altura é:").pack(pady=5)
resultado_label = ttk.Label(root, textvariable=resultado)
resultado_label.pack(pady=5)

# Iniciar loop
root.mainloop()
