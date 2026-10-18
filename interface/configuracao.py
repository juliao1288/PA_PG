import tkinter as tk


def criar_configuracao(frame_conteudo):
    frame_entrada = tk.Frame(frame_conteudo, bg="#FFFFFF")

    frame_entrada.pack(side="left", fill="both", expand=True, padx=10, pady=10)

    config = tk.Label(
    frame_entrada, text="Configuração", font=("Segoe UI", 16, "bold"), bg="#FFFFFF"
    )

    config.pack(anchor="w", padx=20, pady=(15, 15))


    tipo = tk.StringVar(value="PA")

    frame_tipo = tk.Frame(frame_entrada, bg="#FFFFFF")
    frame_tipo.pack(fill="x", padx=20, pady=(0, 10))

    def selecionar_tipo(valor):
        tipo.set(valor)

        if valor == "PA":
            botao_pa.config(bg="#2563EB", fg="#FFFFFF")
            botao_pg.config(bg="#F3F4F6", fg="#374151")
        else:
            botao_pa.config(bg="#F3F4F6", fg="#374151")
            botao_pg.config(bg="#2563EB", fg="#FFFFFF")


    botao_pa = tk.Button(
        frame_tipo,
        text="PA",
        font=("Segoe UI", 11, "bold"),
        bg="#2563EB",
        fg="#FFFFFF",
        activebackground="#1D4ED8",
        activeforeground="#FFFFFF",
        relief="flat",
        bd=0,
        cursor="hand2",
        command=lambda: selecionar_tipo("PA")
    )

    botao_pa.pack(
        side="left",
        fill="x",
        expand=True,
        padx=(0, 5),
        ipady=10
    )

    botao_pg = tk.Button(
        frame_tipo,
        text="PG",
        font=("Segoe UI", 11, "bold"),
        bg="#F3F4F6",
        fg="#374151",
        activebackground="#E5E7EB",
        relief="flat",
        bd=0,
        cursor="hand2",
        command=lambda: selecionar_tipo("PG")
    )

    botao_pg.pack(
        side="left",
        fill="x",
        expand=True,
        padx=(5, 0),
        ipady=10
    )


    usar_meta = tk.BooleanVar(value=False)

    def alternar_meta():
        usar_meta.set(not usar_meta.get())

        if usar_meta.get():
            botao_meta.config(
                bg="#2563EB",
                fg="#FFFFFF"
            )
            label_termos.config(text="Meta da soma: ")
        else:
            botao_meta.config(
                bg="#F3F4F6",
                fg="#374151"
            )
            label_termos.config(text="Quantidade de termos: ")



    botao_meta = tk.Button(
        frame_entrada,
        text="Alcançar meta",
        font=("Segoe UI", 11),
        bg="#F3F4F6",
        fg="#374151",
        activebackground="#E5E7EB",
        relief="flat",
        bd=0,
        highlightthickness=0,
        cursor="hand2",
        command=alternar_meta
    )

    botao_meta.pack(
        fill="x",
        padx=20,
        pady=(5, 15),
        ipady=8
    )

    label_primeiro = tk.Label(
        frame_entrada,
        text="Primeiro termo:",
        font=("Segoe UI", 11),
        bg="#FFFFFF"
    )

    label_primeiro.pack(anchor="w", padx=20)

    entry_primeiro = tk.Entry(
        frame_entrada,
        font=("Segoe UI", 11),
        bg="#F9FAFB",
        fg="#1F2937",
        relief="solid",
        bd=1,
        highlightthickness=1,
        highlightbackground="#D1D5DB",
        highlightcolor="#2563EB"
    )

    entry_primeiro.pack(fill="x", padx=20, pady=(5, 12), ipady=7)


    label_razao = tk.Label(
        frame_entrada,
        text="Razão:",
        font=("Segoe UI", 11),
        bg="#FFFFFF"
    )

    label_razao.pack(anchor="w", padx=20)

    entry_razao = tk.Entry(
        frame_entrada,
        font=("Segoe UI", 11),
        bg="#F9FAFB",
        fg="#1F2937",
        relief="solid",
        bd=1,
        highlightthickness=1,
        highlightbackground="#D1D5DB",
        highlightcolor="#2563EB"
    )

    entry_razao.pack(fill="x", padx=20, pady=(5, 12), ipady=7)


    label_termos = tk.Label(
        frame_entrada,
        text="Quantidade de termos:",
        font=("Segoe UI", 11),
        bg="#FFFFFF"
    )

    label_termos.pack(anchor="w", padx=20)

    entry_termos = tk.Entry(
        frame_entrada,
        font=("Segoe UI", 11),
        bg="#F9FAFB",
        fg="#1F2937",
        relief="solid",
        bd=1,
        highlightthickness=1,
        highlightbackground="#D1D5DB",
        highlightcolor="#2563EB"
    )

    entry_termos.pack(fill="x", padx=20, pady=(5, 12), ipady=7)

    botao_calcular = tk.Button(
        frame_entrada,
        text="Calcular",
        font=("Segoe UI", 12, "bold"),
        bg="#2563EB",
        fg="#FFFFFF",
        activebackground="#1D4ED8",
        activeforeground="#FFFFFF",
        relief="flat",
        bd=0,
        cursor="hand2"
    )

    botao_calcular.pack(
        fill="x",
        padx=20,
        pady=(15, 20),
        ipady=10
    )
    
    return {
        "frame": frame_entrada,
        "tipo": tipo,
        "usar_meta": usar_meta,
        "entry_primeiro": entry_primeiro,
        "entry_razao": entry_razao,
        "entry_termos": entry_termos,
        "botao_calcular": botao_calcular
    }

