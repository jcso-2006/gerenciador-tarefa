import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class GerenciadorDeTarefas:
    def __init__(self, master):
        self.master = master
        master.title("Gerenciador de Tarefas")

        self.rotina = {}
        self.atividades = []

        self.create_widgets()

    def create_widgets(self):
        # Rotina
        self.rotina_label = tk.Label(self.master, text="Rotina (Ex: trabalho: 9:00 - 17:00)")
        self.rotina_label.grid(row=0, column=0, columnspan=2, pady=(10, 0))

        self.rotina_entry = tk.Entry(self.master, width=50)
        self.rotina_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        self.definir_rotina_button = tk.Button(self.master, text="Definir Rotina", command=self.definir_rotina)
        self.definir_rotina_button.grid(row=2, column=0, columnspan=2, pady=5)

        # Atividades
        self.atividade_label = tk.Label(self.master, text="Atividade")
        self.atividade_label.grid(row=3, column=0, pady=5)

        self.atividade_entry = tk.Entry(self.master)
        self.atividade_entry.grid(row=3, column=1, padx=10, pady=5)

        self.inicio_label = tk.Label(self.master, text="Início (Ex: 18:00)")
        self.inicio_label.grid(row=4, column=0, pady=5)

        self.inicio_entry = tk.Entry(self.master)
        self.inicio_entry.grid(row=4, column=1, padx=10, pady=5)

        self.fim_label = tk.Label(self.master, text="Fim (Ex: 19:00)")
        self.fim_label.grid(row=5, column=0, pady=5)

        self.fim_entry = tk.Entry(self.master)
        self.fim_entry.grid(row=5, column=1, padx=10, pady=5)

        self.adicionar_atividade_button = tk.Button(self.master, text="Adicionar Atividade", command=self.adicionar_atividade)
        self.adicionar_atividade_button.grid(row=6, column=0, columnspan=2, pady=5)

        self.mostrar_agenda_button = tk.Button(self.master, text="Mostrar Agenda", command=self.mostrar_agenda)
        self.mostrar_agenda_button.grid(row=7, column=0, columnspan=2, pady=5)

        self.agenda_text = tk.Text(self.master, height=15, width=50)
        self.agenda_text.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

    def definir_rotina(self):
        rotina_str = self.rotina_entry.get()
        try:
            key, value = rotina_str.split(": ")
            self.rotina[key] = value
            messagebox.showinfo("Sucesso", "Rotina definida com sucesso!")
        except ValueError:
            messagebox.showerror("Erro", "Formato inválido. Use: atividade: hora_início - hora_fim")

    def adicionar_atividade(self):
        atividade = self.atividade_entry.get()
        inicio = self.inicio_entry.get()
        fim = self.fim_entry.get()
        try:
            datetime.strptime(inicio, "%H:%M")
            datetime.strptime(fim, "%H:%M")
            self.atividades.append({'atividade': atividade, 'inicio': inicio, 'fim': fim})
            messagebox.showinfo("Sucesso", "Atividade adicionada com sucesso!")
            self.atividade_entry.delete(0, tk.END)
            self.inicio_entry.delete(0, tk.END)
            self.fim_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Erro", "Formato de horário inválido. Use HH:MM")

    def organizar_atividades(self):
        try:
            self.atividades.sort(key=lambda x: datetime.strptime(x['inicio'], "%H:%M"))
        except ValueError:
            messagebox.showerror("Erro", "Erro na organização das atividades.")
    
    def mostrar_agenda(self):
        self.organizar_atividades()  # Organiza as atividades antes de exibir

        self.agenda_text.delete(1.0, tk.END)
        self.agenda_text.insert(tk.END, "Rotina diária:\n")
        for chave, valor in self.rotina.items():
            self.agenda_text.insert(tk.END, f"{chave}: {valor}\n")
        self.agenda_text.insert(tk.END, "\nAtividades organizadas:\n")
        for atividade in self.atividades:
            self.agenda_text.insert(tk.END, f"{atividade['inicio']} - {atividade['fim']}: {atividade['atividade']}\n")

if __name__ == "__main__":
    root = tk.Tk()
    gerenciador = GerenciadorDeTarefas(root)
    root.mainloop()
