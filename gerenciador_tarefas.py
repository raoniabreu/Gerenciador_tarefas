import tkinter as tk
from tkinter import messagebox

# estado global das tarefas
tarefas = []

# função para carregar tarefas de um arquivo
def carregar_tarefas():
    global tarefas
    try:
        with open("tarefas.txt", "r") as f:
            tarefas = [t.strip() for t in f.readlines()]
        return tarefas
    except FileNotFoundError:
        return []

# função para salvar tarefas no arquivo
def salvar_tarefas():
    with open("tarefas.txt", "w") as f:
        for tarefa in tarefas:
            f.write(tarefa + "\n")

# função para adicionar uma nova tarefa
def adicionar_tarefa():
    global tarefas
    tarefa = entrada_tarefa.get().strip()
    if tarefa:
        tarefas.append(tarefa)
        lista_tarefas.insert(tk.END, tarefa)
        entrada_tarefa.delete(0, tk.END)
        salvar_tarefas()
    else:
        messagebox.showwarning("Aviso", "Digite uma tarefa.")

# função para apagar a tarefa selecionada
def apagar_tarefa():
    global tarefas
    sel = lista_tarefas.curselection()
    if not sel:
        messagebox.showwarning("Aviso", "Selecione uma tarefa para apagar!")
        return
    idx = sel[0]
    tarefa = tarefas[idx]
    if messagebox.askyesno("Confirmação", f"Apagar tarefa: {tarefa}?"):
        lista_tarefas.delete(idx)
        tarefas.pop(idx)
        salvar_tarefas()

# função para fechar o programa
def fechar_programa():
    if messagebox.askyesno("Confirmação", "Deseja realmente fechar o programa?"):
        root.destroy()

# Configuração da janela principal
root = tk.Tk()
root.title("Gerenciador de Tarefas")
root.geometry("600x450")
root.config(bg="#f0f4f7")  # cor de fundo suave

# lista de tarefas
tarefas = carregar_tarefas()

# título
titulo = tk.Label(root, text="📋 Gerenciador de Tarefas", font=("Arial", 18, "bold"), bg="#f0f4f7", fg="#333")
titulo.pack(pady=10)

# entrada de texto
entrada_tarefa = tk.Entry(root, width=40, font=("Arial", 12), relief="solid", bd=1)
entrada_tarefa.pack(pady=10, ipady=5)

# frame dos botões
frame_botoes = tk.Frame(root, bg="#f0f4f7")
frame_botoes.pack(pady=5)

btn_adicionar = tk.Button(frame_botoes, text="➕ Adicionar", command=adicionar_tarefa, font=("Arial", 12, "bold"),
                          bg="#4CAF50", fg="white", activebackground="#45a049", width=12, relief="flat")
btn_adicionar.grid(row=0, column=0, padx=5)

btn_apagar = tk.Button(frame_botoes, text="🗑️ Apagar", command=apagar_tarefa, font=("Arial", 12, "bold"),
                       bg="#f44336", fg="white", activebackground="#e53935", width=12, relief="flat")
btn_apagar.grid(row=0, column=1, padx=5)

btn_fechar = tk.Button(frame_botoes, text="❌ Fechar", command=fechar_programa, font=("Arial", 12, "bold"),
                       bg="#607d8b", fg="white", activebackground="#546e7a", width=12, relief="flat")
btn_fechar.grid(row=0, column=2, padx=5)

# frame da lista + scrollbars
frame_lista = tk.Frame(root, bg="#f0f4f7")
frame_lista.pack(pady=15, fill=tk.BOTH, expand=True)

scrollbar_y = tk.Scrollbar(frame_lista, orient=tk.VERTICAL)
scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

scrollbar_x = tk.Scrollbar(frame_lista, orient=tk.HORIZONTAL)
scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

lista_tarefas = tk.Listbox(
    frame_lista, 
    width=70, height=15, 
    font=("Arial", 12),
    yscrollcommand=scrollbar_y.set, 
    xscrollcommand=scrollbar_x.set,
    relief="solid", bd=1, fg="#333", selectbackground="#4CAF50", activestyle="none"
)
lista_tarefas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar_y.config(command=lista_tarefas.yview)
scrollbar_x.config(command=lista_tarefas.xview)

# carrega tarefas já existentes no Listbox
for t in tarefas:
    lista_tarefas.insert(tk.END, t)

# executa a janela
root.mainloop()
