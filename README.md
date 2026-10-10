# 📊 PA & PG LAB

## 🎓 Informações Acadêmicas
* **Projeto:** Projeto 1 - PA e PG
* **Disciplina:** Matemática Discreta
* **Professor:** Alireza Mohebi Ashtiani

---

## 📝 Descrição do Projeto

O **PA & PG LAB** é um sistema modular desenvolvido em Python para cálculo, simulação e validação de **Progressões Aritméticas (PA)** e **Progressões Geométricas (PG)**.

O projeto foi construído seguindo boas práticas de arquitetura modular (`main.py` para a interface interativa no terminal e `funcoes.py` para o motor matemático e tratamento de dados), permitindo que as funções de cálculo sejam facilmente reaproveitadas em futuros desenvolvimentos web (APIs REST) ou interfaces gráficas.

---

## 🛠️ Estrutura de Arquivos

* `main.py`: Menu principal interativo via linha de comando (CLI) com tratamento e exibição dos resultados.
* `funcoes.py`: Módulo contendo os algoritmos matemáticos e validadores de entrada. Todas as funções possuem docstrings completas e tipagem de dados (*type hints*).

---

## ⚙️ Funcionalidades

1. **Progressão Aritmética (PA):**
   * Cálculo e exibição da sequência dos $N$ primeiros termos.
   * Soma acumulada dos termos.

2. **Progressão Geométrica (PG):**
   * Cálculo e exibição da sequência dos $N$ primeiros termos.
   * Soma acumulada dos termos.

3. **Cálculo da Meta:**
   * Determinação do número exato de termos e da soma final necessários para ultrapassar uma meta estipulada.
   * Tratamento direcional para progressões crescentes e decrescentes/negativas.

4. **Validação Rigorosa de Entradas:**
   * Verificação de valores inteiros, números naturais ($>0$) e restrição para razões iguais a zero.

---

## 🚀 Como Executar

### Pré-requisitos
* Python 3.9 ou superior instalado.

### Passo a Passo

1. Clone o repositório:
   ```bash
   git clone [https://github.com/juliao1288/PA_PG](https://github.com/juliao1288/PA_PG)