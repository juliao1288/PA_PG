import tkinter as tk


def criar_resultados(frame_conteudo):
    frame_resultado = tk.Frame(frame_conteudo, bg="#FFFFFF")

    frame_resultado.pack(side="right", fill="both", expand=True, padx=10, pady=10)

    frame_resultado.pack_propagate(False)

    result = tk.Label(
        frame_resultado, text="Resultados", font=("Segoe UI", 16, "bold"), bg="#FFFFFF"
    )

    result.pack(anchor="w", padx=20, pady=20)

    label_sequencia = tk.Label(
        frame_resultado,
        text="Sequência: —",
        font=("Segoe UI", 11),
        bg="#FFFFFF",
        anchor="w",
        justify="left",
        wraplength=350,
    )

    label_sequencia.pack(fill="x", padx=20, pady=(15, 10))

    label_ultimo = tk.Label(
        frame_resultado,
        text="Último termo: —",
        font=("Segoe UI", 11),
        bg="#FFFFFF",
        anchor="w",
    )

    label_ultimo.pack(fill="x", padx=20, pady=(0, 10))

    label_soma = tk.Label(
        frame_resultado,
        text="Soma: —",
        font=("Segoe UI", 11, "bold"),
        bg="#FFFFFF",
        anchor="w",
    )
    label_soma.pack(fill="x", padx=20)

    label_termos = tk.Label(
        frame_resultado,
        text="",
        font=("Segoe UI", 12, "bold"),
        bg="white",
        fg="#1F2937",
        anchor="w"
    )

    label_termos.pack(fill="x", padx=20, pady=(10, 0))

    return {
        "frame": frame_resultado,
        "label_sequencia": label_sequencia,
        "label_soma": label_soma,
        "label_ultimo": label_ultimo,
        "label_termos": label_termos
    }
