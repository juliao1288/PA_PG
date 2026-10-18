import tkinter as tk

janela = tk.Tk()

janela.title("PA & PG LAB")
janela.geometry("900x600")

frame_principal = tk.Frame(janela, bg="#F3F4F6")

frame_principal.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=20
)

janela.mainloop()