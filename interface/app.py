import tkinter as tk
from tkinter import messagebox

from .configuracao import criar_configuracao
from .resultados import criar_resultados
from funcoes import *


def iniciar_interface():
    janela = tk.Tk()

    janela.title("PA & PG LAB")
    janela.geometry("1000x700")
    janela.minsize(900, 650)
    frame_principal = tk.Frame(janela, bg="#F3F4F6")

    frame_principal.pack(fill="both", expand=True, padx=20, pady=20)

    titulo = tk.Label(
        frame_principal,
        text="PA & PG LAB",
        font=("Segoe UI", 26, "bold"),
        bg="#F3F4F6",
        fg="#1F2937",
    )

    titulo.pack(pady=(25, 5))

    calculadora = tk.Label(
        frame_principal,
        text="Calculadora de Progressões",
        font=("Segoe UI", 11),
        bg="#F3F4F6",
        fg="#6B7280",
    )

    calculadora.pack(pady=(0, 25))

    frame_conteudo = tk.Frame(frame_principal, bg="#F3F4F6")

    frame_conteudo.pack(fill="both", expand=True)

    configuracao = criar_configuracao(frame_conteudo)

    def calcular():
        tipo = configuracao["tipo"].get()
        usar_meta = configuracao["usar_meta"].get()

        primeiro = configuracao["entry_primeiro"].get()
        razao = configuracao["entry_razao"].get()
        termos = configuracao["entry_termos"].get()

        if not verifica_numero(primeiro):
            messagebox.showerror("Erro", "Primeiro termo inválido.")
            return

        if not verifica_numero(razao):
            messagebox.showerror("Erro", "Razão inválida.")
            return

        if not verifica_numero(termos):
            messagebox.showerror("Erro", "Meta inválida." if usar_meta else "Quantidade de termos inválida.")
            return

        if not usar_meta and not verifica_numero_natural(termos):
            messagebox.showerror("Erro", "A quantidade de termos deve ser maior que zero.")
            return

        primeiro = int(primeiro)
        razao = int(razao)
        termos = int(termos)

        if tipo == "PA":
            if usar_meta:
                calculado = calculo_meta_pa(primeiro, razao, termos)
            else:
                calculado = calculo_pa(primeiro, razao, termos)

        else:
            if usar_meta:
                calculado = calculo_meta_pg(primeiro, razao, termos)
            else:
                calculado = calculo_pg(primeiro, razao, termos)

        if calculado is None:
            resultado["label_sequencia"].config(
                text="Não é possível alcançar essa meta."
            )
            resultado["label_soma"].config(text="")
            resultado["label_ultimo"].config(text="")
            resultado["label_termos"].config(text="")
            return

        sequencia, soma = calculado

        resultado["label_sequencia"].config(
            text=f"Sequência: {sequencia}"
        )

        resultado["label_soma"].config(
            text=f"Soma: {soma}"
        )

        resultado["label_ultimo"].config(
            text=f"Último termo: {sequencia[-1]}"
        )

        if usar_meta:
            resultado["label_termos"].config(
                text=f"Termos necessários: {len(sequencia)}"
            )
        else:
            resultado["label_termos"].config(text="")

    configuracao["botao_calcular"].config(command=calcular)
    resultado = criar_resultados(frame_conteudo)

    janela.mainloop()
