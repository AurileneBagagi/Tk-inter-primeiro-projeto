from tkinter import *
import sqlite3
from tkinter import messagebox

class Interface():
    #=================================FRAME DO MENU PRINCIPAL===================================
    def __init__(self, projeto):
        self.menu_Principal= Frame(projeto, width=800, height=400)
        self.menu_Principal.place(x=0, y=0)
        self.menu_Principal["bg"]="RosyBrown1"
        Label(self.menu_Principal, text="BEM-VINDO(A) AO SISTEMA DE CONTROLE ACADÊMICO SIMPLIFICADO", font="arial 12", bg="RosyBrown1").place(x=110, y=15)
        Label(self.menu_Principal, text= "Escolha uma opção: ", font="10", bg="RosyBrown1").place(x=15, y=50)
        Button(self.menu_Principal, text="IR PARA MENU DO PROFESSOR", width=50, height=2, bg="PaleTurquoise2", command=self.chama_professor).place(x=15,y=100)
        Button(self.menu_Principal, text="IR PARA MENU DAS DISCIPLINAS", width=50, height=2, bg="PaleTurquoise2",command=self.chama_disciplinas).place(x=15, y=150)
        Button(self.menu_Principal, text="IR PARA MENU DO ALUNO", width=50, height=2, bg="PaleTurquoise2",command=self.chama_aluno).place(x=15, y=200)
        Button(self.menu_Principal, text="IR PARA MENU DAS TURMAS", width=50, height=2, bg="PaleTurquoise2",command=self.chama_Turma).place(x=15, y=250)
        Button(self.menu_Principal, text="IR PARA MENU DOS RELATORIOS", width=50, height=2, bg="PaleTurquoise2",command=self.chama_relatorios).place(x=15, y=300)
    #================================FRAME DO MENU PROFESSOR=====================================
        self.menu_Profe = Frame(projeto, width=800, height=400)
        self.menu_Profe.place(x=0, y=3000)
        self.menu_Profe["bg"] = "RosyBrown1"
        Label(self.menu_Profe, text="BEM-VINDO(A) AO MENU DO PROFESSOR",font="arial 12", bg="RosyBrown1").place(x=250, y=15)
        Label(self.menu_Profe, text="Escolha uma opção: ", font="10", bg="RosyBrown1").place(x=15, y=50)
        Button(self.menu_Profe, text="ADCIONAR PROFESSOR", width=50, height=2, bg="PaleTurquoise2",command=self.botao_add).place(x=15, y=100)
        Button(self.menu_Profe, text="CONSULTAR DADOS DO PROFESSOR", width=50, height=2, bg="PaleTurquoise2", command=self.botao_cons).place(x=15, y=150)
        Button(self.menu_Profe, text="ATUALIZAR DADOS DO PROFESSOR", width=50, height=2, bg="PaleTurquoise2", command=self.botao_atu).place(x=15,y=200)
        Button(self.menu_Profe, text="REMOVER PROFESSOR", width=50, height=2, bg="PaleTurquoise2", command=self.botao_rem).place(x=15, y=250)
        Button(self.menu_Profe, text="CONSULTAR TODOS OS PROFESSORES", width=50, height=2, bg="PaleTurquoise2", command=self.mostrar_todos).place(x=15, y=300)
        Button(self.menu_Profe, text="VOLTAR PARA O MENU PRINCIPAL", width=50, height=2, bg="lightskyblue2", command=self.voltar_professor).place(x=15, y=350)

    # ================================FRAME DAS DISCIPLINAS=====================================
        self.menu_Dis = Frame(projeto, width=800, height=400)
        self.menu_Dis.place(x=0, y=3000)
        self.menu_Dis["bg"] = "RosyBrown1"
        Label(self.menu_Dis, text="BEM-VINDO(A) AO MENU DAS DISCIPLINA", font="arial 12", bg="RosyBrown1").place(x=230,y=15)
        Label(self.menu_Dis, text="Escolha uma opção: ", font="10", bg="RosyBrown1").place(x=15, y=50)
        Button(self.menu_Dis, text="ADCIONAR DISCIPLINA", width=50, height=2, bg="PaleTurquoise2",command=self.botao_add_dis).place(x=15, y=100)
        Button(self.menu_Dis, text="CONSULTAR DISCIPLINA", width=50, height=2, bg="PaleTurquoise2", command=self.botao_con_dis).place(x=15, y=150)
        Button(self.menu_Dis, text="ATUALIZAR DADOS DA DISCIPLINA", width=50, height=2, bg="PaleTurquoise2",command=self.botao_att_dis).place(x=15, y=200)
        Button(self.menu_Dis, text="REMOVER DISCIPLINA", width=50, height=2, bg="PaleTurquoise2",command=self.botao_rem_dis).place(x=15, y=250)
        Button(self.menu_Dis, text="CONSULTAR TODOS AS DISCIPLINAS", width=50, height=2, bg="PaleTurquoise2", command=self.mostrar_todas_dis).place(x=15, y=300)
        Button(self.menu_Dis, text="VOLTAR PARA O MENU PRINCIPAL", width=50, height=2, bg="PaleTurquoise2", command=self.voltar_disciplinas).place(x=15, y=350)
    # ================================FRAME DO MENU ALUNO=====================================
        self.menu_Aluno = Frame(projeto, width=800, height=600)
        self.menu_Aluno.place(x=0, y=3000)
        self.menu_Aluno["bg"] = "RosyBrown1"
        Label(self.menu_Aluno, text="BEM-VINDO(A) AO MENU DO ALUNO", font="arial 12", bg="RosyBrown1").place(x=250,y=15)
        Label(self.menu_Aluno, text="Escolha uma opção: ", font="10", bg="RosyBrown1").place(x=15, y=50)
        Button(self.menu_Aluno, text="ADCIONAR ALUNO", width=50, height=2, bg="PaleTurquoise2", command = self.botao_add_al).place(x=15, y=100)
        Button(self.menu_Aluno, text="CONSULTAR ALUNO", width=50, height=2, bg="PaleTurquoise2", command= self.botao_con_al).place(x=15, y=150)
        Button(self.menu_Aluno, text="ATUALIZAR DADOS DO ALUNO", width=50, height=2, bg="PaleTurquoise2", command=self.botao_att_al).place(x=15, y=200)
        Button(self.menu_Aluno, text="REMOVER ALUNO", width=50, height=2, bg="PaleTurquoise2", command= self.botao_rem_al).place(x=15, y=250)
        Button(self.menu_Aluno, text="CONSULTAR TODOS OS ALUNOS", width=50, height=2, bg="PaleTurquoise2", command=self.mostrar_todos_al).place(x=15, y=300)
        Button(self.menu_Aluno, text="VOLTAR PARA O MENU PRINCIPAL", width=50, height=2, bg="PaleTurquoise2", command=self.voltar_aluno).place(x=15, y=350)
    # ================================FRAME DO MENU DA TURMA=====================================
        self.menu_Turma = Frame(projeto, width=800, height=400)
        self.menu_Turma.place(x=0, y=3000)
        self.menu_Turma["bg"] = "RosyBrown1"
        Label(self.menu_Turma, text="BEM-VINDO(A) AO MENU DA TURMA", font="arial 12", bg="RosyBrown1").place(x=250,y=15)
        Label(self.menu_Turma, text="Escolha uma opção: ", font="10", bg="RosyBrown1").place(x=15, y=50)
        Button(self.menu_Turma, text="ADCIONAR TURMA", width=50, height=2, bg="PaleTurquoise2", command=self.botao_ok_turma).place(x=15, y=100)
        Button(self.menu_Turma, text="CONSULTAR TURMA", width=50, height=2, bg="PaleTurquoise2", command=self.botao_con_turma).place(x=15, y=150)
        Button(self.menu_Turma, text="ATUALIZAR DADOS DA TURMA", width=50, height=2, bg="PaleTurquoise2", command=self.botao_att_turma).place(x=15, y=200)
        Button(self.menu_Turma, text="REMOVER TURMA", width=50, height=2, bg="PaleTurquoise2", command=self.botao_rem_turma).place(x=15, y=250)
        Button(self.menu_Turma, text="CONSULTAR TODOS AS TURMAS", width=50, height=2, bg="PaleTurquoise2", command=self.botao_most_turma).place(x=15, y=300)
        Button(self.menu_Turma, text="VOLTAR PARA O MENU PRINCIPAL", width=50, height=2, bg="PaleTurquoise2", command=self.voltar_Turma).place(x=15, y=350)
    # ================================FRAME DOS RELATORIOS=====================================
        self.menu_Rela = Frame(projeto, width=800, height=400)
        self.menu_Rela.place(x=0, y=3000)
        self.menu_Rela["bg"] = "RosyBrown1"
        Label(self.menu_Rela, text="BEM-VINDO(A) AO MENU DOS RELATORIOS", font="arial 12", bg="RosyBrown1").place(x=230,y=15)
        Label(self.menu_Rela, text="Escolha uma opção: ", font="10", bg="RosyBrown1").place(x=15, y=50)
        Button(self.menu_Rela, text="IMPRIMIR ATA DE EXERCICIO", width=50, height=2, bg="PaleTurquoise2", command=self.botao_con_turma).place(x=15, y=100)
        Button(self.menu_Rela, text="IMPRIMIR ATA DE TURMA POR PROFESSOR (TODAS AS TURMAS)", width=50, height=2, bg="PaleTurquoise2", command=self.botao_mostrar_profes).place(x=15, y=150)
        Button(self.menu_Rela, text="IMPRIMIR ATA DE TURMA POR PROFESSOR (POR SEMESTRE)", width=50, height=2, bg="PaleTurquoise2").place(x=15, y=200)
        Button(self.menu_Rela, text="IMPRIMIR ATA DE TURMA POR ALUNO (TODAS AS TURMAS)", width=50, height=2, bg="PaleTurquoise2", command=self.botao_mostrar_alun_t).place(x=15, y=250)
        Button(self.menu_Rela, text="IMPRIMIR ATA DE TURMA POR ALUNO (POR SEMESTRE)", width=50, height=2, bg="PaleTurquoise2").place(x=15, y=300)
        Button(self.menu_Rela, text="VOLTAR PARA O MENU PRINCIPAL", width=50, height=2,bg="PaleTurquoise2", command=self.voltar_relatorios).place(x=15, y=350)
# ================================INTERAÇÃO DO MENU PRINCIPAL COM OS BOTÕES=====================================
    def chama_professor(self):
        self.menu_Profe.place(x=0, y=0)
        self.menu_Principal.place(x=0, y=3000)
    def chama_disciplinas(self):
        self.menu_Dis.place(x=0, y=0)
        self.menu_Principal.place(x=0, y=3000)
    def chama_aluno(self):
        self.menu_Aluno.place(x=0,y=0)
        self.menu_Principal.place(x=0, y=3000)
    def chama_Turma(self):
        self.menu_Turma.place(x=0,y=0)
        self.menu_Principal.place(x=0, y=3000)
    def chama_relatorios(self):
        self.menu_Rela.place(x=0,y=0)
        self.menu_Principal.place(x=0, y=3000)
# ================================INTERAÇÃO DOS MENUS PARA VOLTAR AO MENU PRINCIPAL=====================================
    def voltar_professor(self):
        self.menu_Profe.place(x=0, y=3000)
        self.menu_Principal.place(x=0, y=0)
        Label(self.dados_prof, text="", relief="ridge", width=53, height=19, bg="RosyBrown1").place(x=-2,y=-2)
    def voltar_disciplinas(self):
        self.menu_Dis.place(x=0, y=3000)
        self.menu_Principal.place(x=0, y=0)
        Label(self.dados_prof, text="", relief="ridge", width=53, height=19, bg="RosyBrown1").place(x=-2, y=-2)
    def voltar_aluno(self):
        self.menu_Aluno.place(x=0,y=3000)
        self.menu_Principal.place(x=0, y=0)
        Label(self.dados_prof, text="", relief="ridge", width=53, height=19, bg="RosyBrown1").place(x=-2, y=-2)
    def voltar_Turma(self):
        self.menu_Turma.place(x=0,y=3000)
        self.menu_Principal.place(x=0, y=0)
        Label(self.dados_prof, text="", relief="ridge", width=53, height=19, bg="RosyBrown1").place(x=-2, y=-2)
    def voltar_relatorios(self):
        self.menu_Rela.place(x=0,y=3000)
        self.menu_Principal.place(x=0, y=0)
        Label(self.dados_prof, text="", relief="ridge", width=53, height=19, bg="RosyBrown1").place(x=-2, y=-2)
# ================================INTERAÇÃO DO MENU DO PROFESSOR=====================================
    def botao_add(self):
        return self.chama_q_prof("add")
    def botao_cons(self):
        return self.chama_q_prof("consultar")
    def botao_atu(self):
        return self.chama_q_prof("atualizar")
    def botao_rem(self):
        return self.chama_q_prof("remover")
    def chama_q_prof(self, botao):
        self.comando = botao
        if self.comando == "":
            self.dados_prof.place(x=15, y=6000)
        else:
            self.dados_prof = Frame(projeto, width=360, height=258)
            self.dados_prof["bg"] = "RosyBrown1"
            self.dados_prof.place(x=400, y=80)
            Label(self.dados_prof, text="", borderwidth=1, relief="ridge", width=50, height=16, bg="RosyBrown1").place(x=0,y=10)
            Label(self.dados_prof, text="DIGITE OS DADOS QUANDO NECESSARIO", font="arial 8 bold").place(x=55, y=0)
            Label(self.dados_prof, text="NOME DO(A) PROFESSOR(A):", font="arial 8 bold").place(x=5, y=30)
            Label(self.dados_prof, text="CPF DO(A) PROFESSOR(A):", font="arial 8 bold").place(x=5, y=80)
            Label(self.dados_prof, text="DEPARTAMENTO:", font="arial 8 bold").place(x=5, y=130)
            if self.comando == "add":
                self.nomeentry= Entry(self.dados_prof, width=55)
                self.nomeentry.place(x=5, y=50)
                self.cpfentry= Entry(self.dados_prof, width=11)
                self.cpfentry.place(x=5, y=100)
                self.depentry = Entry(self.dados_prof, width=55)
                self.depentry.place(x=5, y=150)
            if self.comando == "add":
                Button(self.dados_prof, text="ADICIONAR", width=20, height=2,bg="PaleTurquoise2", command=self.verificar_prof_j_exist).place(x=90, y=180)
            if self.comando == "consultar" or self.comando == "atualizar":
                self.cpfentry = Entry(self.dados_prof, width=11)
                self.cpfentry.place(x=5, y=100)
                Button(self.dados_prof, text="CONSULTAR", width=20, height=2, bg="PaleTurquoise2", command=self.consultar_prof).place(x=90, y=180)
            if self.comando == "atualizar":
                self.cpfentry = Entry(self.dados_prof, width=11)
                self.cpfentry.place(x=5, y=100)
                Button(self.dados_prof, text="ATUALIZAR", width=20, height=2, bg="PaleTurquoise2",command=self.consultar_prof).place(x=90, y=180)
            if self.comando == "atua":
                self.nomeentry = Entry(self.dados_prof, width=55)
                self.nomeentry.place(x=5, y=50)
                self.depentry = Entry(self.dados_prof, width=55)
                self.depentry.place(x=5, y=150)
                Button(self.dados_prof, text="CANCELAR", width=20, height=2, bg="PaleTurquoise2", command=self.cancelar).place(x=10, y=180)
                Button(self.dados_prof, text="ATUALIZAR", width=20, height=2, bg="PaleTurquoise2", command=self.atualizar_prof).place(x=170, y=180)
            if self.comando == "remover":
                self.cpfentry = Entry(self.dados_prof, width=11)
                self.cpfentry.place(x=5, y=100)
                Button(self.dados_prof, text="CANCELAR", width=20, height=2, bg="PaleTurquoise2", command=self.cancelar).place(x=10, y=180)
                Button(self.dados_prof, text="REMOVER", width=20, height=2, bg="PaleTurquoise2", command=self.remover_prof).place(x=170, y=180)
# ================================INTERAÇÃO DO BANCO DE DADOS COM TODOS OS MENUS=====================================
    def verificar_tamanho_cpf(self, ver):
        CPF = ver
        if len(ver) == 11:
            if str(ver).isnumeric():
                return str(self.cpfentry.get())
            else:
                messagebox.showerror('ERRO', 'O CPF QUE VOCÊ DIGITOU É INVALIDO')
                Label(self.dados_prof, text="", relief="ridge", width=53, height=19, bg="RosyBrown1").place(x=-2, y=-2)
                return "Invalido"
        else:
            messagebox.showerror('ERRO', 'O CPF QUE VOCÊ DIGITOU É MENOR OU MAIOR QUE 11 DIGITOS')
            Label(self.dados_prof, text="", relief="ridge", width=53, height=19, bg="RosyBrown1").place(x=-2, y=-2)
            return "Invalido"

    def cancelar(self):
        Label(self.dados_prof, text="", relief="ridge", width=53, height=19, bg="RosyBrown1").place(x=-2, y=-2)

    def verificar_tamanho_cod(self, ver):
        COD = ver
        if len(ver) == 5:
            if str(ver).isnumeric():
                return str(self.cpfentry.get())
            else:
                messagebox.showerror('ERRO', 'O CÓDIGO QUE VOCÊ DIGITOU É INVALIDO')
                Label(self.dados_prof, text="", relief="ridge", width=53, height=19, bg="RosyBrown1").place(x=-2, y=-2)
                return "Invalido"
        else:
            messagebox.showerror('ERRO', 'O CÓDIGO QUE VOCÊ DIGITOU É MENOR OU MAIOR QUE 5 DIGITOS')
            Label(self.dados_prof, text="", relief="ridge", width=53, height=19, bg="RosyBrown1").place(x=-2, y=-2)
            return "Invalido"
# ================================INTERAÇÃO DO BANCO DE DADOS COM O MENU PROFESSOR=====================================
    def verificar_prof_j_exist(self):
        dadinhos = str(self.cpfentry.get())
        cpf = self.verificar_tamanho_cpf(dadinhos)
        if cpf != "Invalido":
            dados = [str(self.nomeentry.get()).title(), cpf, str(self.depentry.get()).title()]
            conexao = sqlite3.connect("professores.db")
            curso = conexao.cursor()
            curso.execute("create table if not exists professores(NOME text, CPF text, DEPARTAMENTO text)")
            curso.execute("select * from professores where CPF = '{}'".format(dados[1]))
            while True:
                resultado = curso.fetchone()
                if resultado == None:
                    break
                messagebox.showerror('CPF JÁ EXISTE', 'O CPF que você digitou já existe, por favor adicione outro!!!')
                return self.chama_q_prof("add")
            self.banco_add_prof(dados)
        else:
            Label(self.dados_prof, text="", relief="ridge", width=53, height=19, bg="RosyBrown1").place(x=-2, y=-2)

    def banco_add_prof(self, dados):
        dados1 = dados
        conexao = sqlite3.connect("professores.db")
        curso = conexao.cursor()
        curso.execute("create table if not exists professores(NOME text, CPF text, DEPARTAMENTO text)")
        curso.execute("insert into professores(NOME, CPF, DEPARTAMENTO) values(?,?,?)", dados1)
        conexao.commit()
        curso.close()
        conexao.close()
        messagebox.showinfo('INFORMATIVO', 'O PROFESSOR(A) FOI ADICIONADO(A) COM SUCESSO!')
        Label(self.dados_prof, text="", relief="ridge", width=53, height=19, bg="RosyBrown1").place(x=-2, y=-2)

    def consultar_prof(self):
        dadinhos = str(self.cpfentry.get())
        dados = self.verificar_tamanho_cpf(dadinhos)
        if dados != "Invalido":
            conexao = sqlite3.connect("professores.db")
            curso = conexao.cursor()
            curso.execute("select * from professores where CPF = '{}'".format(dados))
            x=0
            while True:
                resultado = curso.fetchone()
                if resultado == None:
                    if x == 0:
                        messagebox.showerror('INFORMATIVO', 'O PROFESSOR(A) NÃO FOI ENCONTRADO')
                        Label(self.dados_prof, text="", relief="ridge", width=53, height=19, bg="RosyBrown1").place(x=-2,y=-2)
                        if self.comando == "add_professor":
                            return self.chama_q_turma("add_professor")
                    break
                Label(self.dados_prof, text="", borderwidth=6, relief="ridge", width=50, height=16, bg="RosyBrown1").place(x=0, y=0)
                Label(self.dados_prof, text="DADOS DO(A) PROFESSOR(A)", font="arial 10 bold").place(x=85, y=0)
                Label(self.dados_prof, text="NOME DO(A) PROFESSOR(A):", font="arial 8 bold").place(x=10, y=30)
                Label(self.dados_prof, text="CPF DO(A) PROFESSOR(A):", font="arial 8 bold").place(x=10, y=80)
                Label(self.dados_prof, text="DEPARTAMENTO:", font="arial 8 bold").place(x=10, y=130)
                Label(self.dados_prof, text= resultado[0], font="arial 10 bold", bg="RosyBrown1").place(x=10, y=50)
                Label(self.dados_prof, text= resultado[1], font="arial 10 bold", bg="RosyBrown1").place(x=10, y=100)
                Label(self.dados_prof, text= resultado[2], font="arial 10 bold", bg="RosyBrown1").place(x=10, y=150)
                x += 1
                if self.comando == "atualizar":
                    return self.chama_q_prof("atua")
                if self.comando == "add_professor":
                    Label(self.dados_prof, text="", relief="ridge", width=53, height=19, bg="RosyBrown1").place(x=-2,y=-2)
                    return self.add_profe_t()
        else:
            Label(self.dados_prof, text="", relief="ridge", width=53, height=19, bg="RosyBrown1").place(x=-2, y=-2)
            if self.comando == "add_professor":
                return self.chama_q_turma("add_professor")

    def atualizar_prof(self):
        dadinhos = str(self.cpfentry.get())
        cpf = self.verificar_tamanho_cpf(dadinhos)
        if cpf != "Invalido":
            dados = [str(self.nomeentry.get()).title(), cpf, str(self.depentry.get()).title()]
            conexao = sqlite3.connect("professores.db")
            curso = conexao.cursor()
            curso.execute("update professores set NOME = '{}' where CPF= '{}'".format(dados[0],dados[1]))
            curso.execute("update professores set DEPARTAMENTO = '{}' where CPF= '{}'".format(dados[2], dados[1]))
            messagebox.showinfo('INFORMATIVO', 'OS DADOS FORAM ATUALIZADOS COM SUCESSO!')
            Label(self.dados_prof, text="", relief="ridge", width=53, height=19, bg="RosyBrown1").place(x=-2, y=-2)
            conexao.commit()
            conexao.close()
        else:
            Label(self.dados_prof, text="", relief="ridge", width=53, height=19, bg="RosyBrown1").place(x=-2, y=-2)
    def remover_prof(self):
        cpf = str(self.cpfentry.get())
        conexao = sqlite3.connect("professores.db")
        curso = conexao.cursor()
        curso.execute("delete from professores where CPF = '{}'".format(cpf))
        print("registros apagados", curso.rowcount)
        if curso.rowcount == 1:
            conexao.commit()
            messagebox.showinfo('INFORMATIVO', 'PROFESSOR DELETADO DO SISTEMA COM SUCESSO!')
        else:
            conexao.rollback()
            messagebox.showerror('ERRO', 'OPERAÇÃO SEM SUCESSO, DIGITE UM CPF VALIDO!')
            conexao.close()
            return self.chama_q_prof("remover")
        Label(self.dados_prof, text="", relief="ridge", width=53, height=19, bg="RosyBrown1").place(x=-2, y=-2)
        conexao.close()

    def mostrar_todos(self):
        Label(self.dados_prof, text="", borderwidth=2, relief="ridge", width=50, height=17, bg="RosyBrown1").place(x=0, y=0)
        Label(self.dados_prof, text="TODOS OS PROFESSORES",font="arial 12 bold").place(x= 70, y=15)
        self.scroball = Scrollbar(self.dados_prof)
        self.listbox = Listbox(self.dados_prof, width=53, height=10, yscrollcommand=self.scroball)
        self.listbox.place(x=10,y=50)
        self.scroball.place(x=332, y=50, height=163)
        self.scroball.config(command=self.listbox.yview)
        conexao = sqlite3.connect("professores.db")
        curso = conexao.cursor()
        curso.execute("select * from professores")
        registro = curso.fetchall()
        for dado in registro:
            T = [["NOME:", dado[0]], ["DEPARTAMENTO:", dado[2]], "ttttt"]
            self.listbox.insert(END,"------------------------------------------------------------------", T[0], T[1])
        curso.close()
        conexao.close()

# ================================INTERAÇÃO DO MENU DO ALUNO=====================================
    def botao_add_al(self):
        return self.chama_q_alunos("add")

    def botao_con_al(self):
        return self.chama_q_alunos("consultar")

    def botao_att_al(self):
        return self.chama_q_alunos("atualizar")

    def botao_rem_al(self):
        return self.chama_q_alunos("remover")

    def chama_q_alunos(self, botao):
        self.comando = botao
        if self.comando == "":
            self.dados_prof.place(x=15, y=6000)
        else:
            self.dados_prof = Frame(projeto, width=360, height=258)
            self.dados_prof["bg"] = "RosyBrown1"
            self.dados_prof.place(x=400, y=80)
            Label(self.dados_prof, text="", borderwidth=1, relief="ridge", width=50, height=16,bg="RosyBrown1").place(x=0, y=10)
            Label(self.dados_prof, text="DIGITE OS DADOS QUANDO NECESSARIO", font="arial 8 bold").place(x=55, y=0)
            Label(self.dados_prof, text="NOME DO(A) ALUNO(A):", font="arial 8 bold").place(x=5, y=30)
            Label(self.dados_prof, text="CPF DO(A) ALUNO(A):", font="arial 8 bold").place(x=5, y=80)
            if self.comando == "add":
                self.nomeentry = Entry(self.dados_prof, width=55)
                self.nomeentry.place(x=5, y=50)
                self.cpfentry = Entry(self.dados_prof, width=11)
                self.cpfentry.place(x=5, y=100)
            if self.comando == "add":
                Button(self.dados_prof, text="ADICIONAR", width=20, height=2, bg="PaleTurquoise2",command=self.verificar_alun_j_exist).place(x=90, y=180)
            if self.comando == "consultar" or self.comando == "atualizar":
                self.cpfentry = Entry(self.dados_prof, width=11)
                self.cpfentry.place(x=5, y=100)
                Button(self.dados_prof, text="CONSULTAR", width=20, height=2, bg="PaleTurquoise2",command=self.consultar_alunos).place(x=90, y=180)
            if self.comando == "atualizar":
                self.cpfentry = Entry(self.dados_prof, width=11)
                self.cpfentry.place(x=5, y=100)
                Button(self.dados_prof, text="ATUALIZAR", width=20, height=2, bg="PaleTurquoise2",command=self.consultar_alunos).place(x=90, y=180)
            if self.comando == "atua":
                self.nomeentry = Entry(self.dados_prof, width=55)
                self.nomeentry.place(x=5, y=50)
                Button(self.dados_prof, text="CANCELAR", width=20, height=2, bg="PaleTurquoise2",command=self.cancelar).place(x=10, y=180)
                Button(self.dados_prof, text="ATUALIZAR", width=20, height=2, bg="PaleTurquoise2",command=self.atualizar_aluno).place(x=170, y=180)
            if self.comando == "remover":
                self.cpfentry = Entry(self.dados_prof, width=11)
                self.cpfentry.place(x=5, y=100)
                Button(self.dados_prof, text="CANCELAR", width=20, height=2, bg="PaleTurquoise2",command=self.cancelar).place(x=10, y=180)
                Button(self.dados_prof, text="REMOVER", width=20, height=2, bg="PaleTurquoise2",command=self.remover_aluno).place(x=170, y=180)

    # ================================INTERAÇÃO DO BANCO DE DADOS COM O MENU DO ALUNO=====================================
    def verificar_alun_j_exist(self):
        dadinhos = self.cpfentry.get()
        cpf = self.verificar_tamanho_cpf(dadinhos)
        if cpf != "Invalido":
            dados = [str(self.nomeentry.get()).title(), cpf]
            conexao = sqlite3.connect("alunos.db")
            curso = conexao.cursor()
            curso.execute("create table if not exists alunos(NOME text, CPF text)")
            curso.execute("select * from alunos where CPF = '{}'".format(dados[1]))
            while True:
                resultado = curso.fetchone()
                if resultado == None:
                    break
                messagebox.showerror('CPF JÁ EXISTE', 'O CPF que você digitou já existe, por favor adicione outro!!!')
                return self.chama_q_alunos("add")
            self.banco_add_aluno(dados)
        else:
            Label(self.dados_prof, text="", relief="ridge", width=53, height=19, bg="RosyBrown1").place(x=-2, y=-2)


    def banco_add_aluno(self, dados):
        dados1 = dados
        conexao = sqlite3.connect("alunos.db")
        curso = conexao.cursor()
        curso.execute("create table if not exists alunos(NOME text, CPF text)")
        curso.execute("insert into alunos(NOME, CPF) values(?,?)", dados1)
        conexao.commit()
        curso.close()
        conexao.close()
        messagebox.showinfo('INFORMATIVO', 'O ALUNO(A) FOI ADICIONADO(A) COM SUCESSO!')
        Label(self.dados_prof, text="", relief="ridge", width=53, height=19, bg="RosyBrown1").place(x=-2, y=-2)

    def consultar_alunos(self):
        dadinhos = self.cpfentry.get()
        dados = self.verificar_tamanho_cpf(dadinhos)
        if dados != "Invalido":
            conexao = sqlite3.connect("alunos.db")
            curso = conexao.cursor()
            curso.execute("select * from alunos where CPF = '%s'" % dados)
            x = 0
            while True:
                resultado = curso.fetchone()
                if resultado == None:
                    if x == 0:
                        messagebox.showerror('INFORMATIVO', 'O ALUNO(A) NÃO FOI ENCONTRADO')
                        Label(self.dados_prof, text="", relief="ridge", width=53, height=19, bg="RosyBrown1").place(x=-2,y=-2)
                        if self.comando == "add_alunos":
                            return self.chama_q_turma("add_alunos")
                    break
                Label(self.dados_prof, text="", borderwidth=6, relief="ridge", width=50, height=16,
                      bg="RosyBrown1").place(x=0, y=0)
                Label(self.dados_prof, text="DADOS DO(A) ALUNO(A)", font="arial 10 bold").place(x=85, y=0)
                Label(self.dados_prof, text="NOME DO(A) ALUNO(A):", font="arial 8 bold").place(x=10, y=30)
                Label(self.dados_prof, text="CPF DO(A) ALUNO(A):", font="arial 8 bold").place(x=10, y=80)
                Label(self.dados_prof, text=str(resultado[0]).title(), font="arial 10 bold", bg="RosyBrown1").place(x=10, y=50)
                Label(self.dados_prof, text=resultado[1], font="arial 10 bold", bg="RosyBrown1").place(x=10, y=100)
                x += 1
                if self.comando == "atualizar":
                    return self.chama_q_alunos("atua")
                if self.comando == "add_alunos":
                    Label(self.dados_prof, text="", relief="ridge", width=53, height=19, bg="RosyBrown1").place(x=-2,y=-2)
                    return self.add_alunos_t()
        else:
            Label(self.dados_prof, text="", relief="ridge", width=53, height=19, bg="RosyBrown1").place(x=-2, y=-2)
            if self.comando == "add_alunos":
                return self.chama_q_turma("add_alunos")

    def atualizar_aluno(self):
        dadinhos = str(self.cpfentry.get())
        cpf = self.verificar_tamanho_cpf(dadinhos)
        if cpf != "Invalido":
            dados = [str(self.nomeentry.get()), cpf]
            conexao = sqlite3.connect("alunos.db")
            curso = conexao.cursor()
            curso.execute("update alunos set NOME = '{}' where CPF= '{}'".format(dados[0], dados[1]))
            messagebox.showinfo('INFORMATIVO', 'OS DADOS FORAM ATUALIZADOS COM SUCESSO!')
            Label(self.dados_prof, text="", relief="ridge", width=53, height=19, bg="RosyBrown1").place(x=-2, y=-2)
            conexao.commit()
            conexao.close()
        else:
            Label(self.dados_prof, text="", relief="ridge", width=53, height=19, bg="RosyBrown1").place(x=-2, y=-2)

    def remover_aluno(self):
        cpf = self.cpfentry.get()
        conexao = sqlite3.connect("alunos.db")
        curso = conexao.cursor()
        curso.execute("delete from alunos where CPF = '{}'".format(cpf))
        print("registros apagados", curso.rowcount)
        if curso.rowcount == 1:
            conexao.commit()
            messagebox.showinfo('INFORMATIVO', 'ALUNO(A) DELETADO DO SISTEMA COM SUCESSO!')
        else:
            conexao.rollback()
            messagebox.showerror('ERRO', 'OPERAÇÃO SEM SUCESSO, DIGITE UM CPF VALIDO!')
            conexao.close()
            return self.chama_q_alunos("remover")
        Label(self.dados_prof, text="", relief="ridge", width=53, height=19, bg="RosyBrown1").place(x=-2, y=-2)
        conexao.close()

    def mostrar_todos_al(self):
        Label(self.dados_prof, text="", borderwidth=2, relief="ridge", width=50, height=17, bg="RosyBrown1").place(x=0, y=0)
        Label(self.dados_prof, text="TODOS OS ALUNOS",font="arial 12 bold").place(x= 90, y=15)
        self.scroball = Scrollbar(self.dados_prof)
        self.listbox = Listbox(self.dados_prof, width=53, height=10, yscrollcommand=self.scroball)
        self.listbox.place(x=10,y=50)
        self.scroball.place(x=332, y=50, height=163)
        self.scroball.config(command=self.listbox.yview)
        conexao = sqlite3.connect("alunos.db")
        curso = conexao.cursor()
        curso.execute("select * from alunos")
        registro = curso.fetchall()
        for dado in registro:
            T = ["NOME:", str(dado[0]).title()]
            self.listbox.insert(END,"------------------------------------------------------------------", T)

    # ================================INTERAÇÃO DO MENU DA DISCIPLINAS=====================================
    def botao_add_dis(self):
        return self.chama_q_disci("add")
    def botao_con_dis(self):
        return self.chama_q_disci("consultar")
    def botao_att_dis(self):
        return self.chama_q_disci("atualizar")
    def botao_rem_dis(self):
        return self.chama_q_disci("remover")
    def chama_q_disci(self, botao):
        self.comando = botao
        if self.comando == "":
            self.dados_prof.place(x=15, y=6000)
        else:
            self.dados_prof = Frame(projeto, width=360, height=258)
            self.dados_prof["bg"] = "RosyBrown1"
            self.dados_prof.place(x=400, y=80)
            Label(self.dados_prof, text="", borderwidth=1, relief="ridge", width=50, height=16, bg="RosyBrown1").place(x=0,y=10)
            Label(self.dados_prof, text="DIGITE OS DADOS QUANDO NECESSARIO", font="arial 8 bold").place(x=55, y=0)
            Label(self.dados_prof, text="NOME DA DISCIPLINAS:", font="arial 8 bold").place(x=5, y=30)
            Label(self.dados_prof, text="CÓDIGO DA DISCIPLINA:", font="arial 8 bold").place(x=5, y=80)
            if self.comando == "add":
                self.nomeentry= Entry(self.dados_prof, width=55)
                self.nomeentry.place(x=5, y=50)
                self.cpfentry= Entry(self.dados_prof, width=5)
                self.cpfentry.place(x=5, y=100)
                Button(self.dados_prof, text="ADICIONAR", width=20, height=2,bg="PaleTurquoise2", command=self.verificar_dis_j_exist).place(x=90, y=180)
            if self.comando == "consultar" or self.comando == "atualizar":
                self.cpfentry = Entry(self.dados_prof, width=5)
                self.cpfentry.place(x=5, y=100)
                Button(self.dados_prof, text="CONSULTAR", width=20, height=2, bg="PaleTurquoise2", command=self.consultar_dis).place(x=90, y=180)
            if self.comando == "atualizar":
                self.cpfentry = Entry(self.dados_prof, width=5)
                self.cpfentry.place(x=5, y=100)
                Button(self.dados_prof, text="ATUALIZAR", width=20, height=2, bg="PaleTurquoise2",command=self.consultar_dis).place(x=90, y=180)
            if self.comando == "atua":
                self.nomeentry = Entry(self.dados_prof, width=55)
                self.nomeentry.place(x=5, y=50)
                Button(self.dados_prof, text="CANCELAR", width=20, height=2, bg="PaleTurquoise2", command=self.cancelar).place(x=10, y=180)
                Button(self.dados_prof, text="ATUALIZAR", width=20, height=2, bg="PaleTurquoise2", command=self.atualizar_dis).place(x=170, y=180)
            if self.comando == "remover":
                self.cpfentry = Entry(self.dados_prof, width=5)
                self.cpfentry.place(x=5, y=100)
                Button(self.dados_prof, text="CANCELAR", width=20, height=2, bg="PaleTurquoise2", command=self.cancelar).place(x=10, y=180)
                Button(self.dados_prof, text="REMOVER", width=20, height=2, bg="PaleTurquoise2", command=self.remover_dis).place(x=170, y=180)

    # ================================INTERAÇÃO DO BANCO DE DADOS COM O MENU DO ALUNO=====================================
    def verificar_dis_j_exist(self):
        dadinhos = self.cpfentry.get()
        dis = self.verificar_tamanho_cod(dadinhos)
        if dis != "Invalido":
            dados = [str(self.nomeentry.get()).title(), dis]
            conexao = sqlite3.connect("disciplinas.db")
            curso = conexao.cursor()
            curso.execute("create table if not exists disciplinas(NOME text, CODIGO text)")
            curso.execute("select * from disciplinas where CODIGO = '{}'".format(dados[1]))
            while True:
                resultado = curso.fetchone()
                if resultado == None:
                    break
                messagebox.showerror('CODIGO DA DISCIPLINA JÁ EXISTE', 'O CODIGO que você digitou já existe, por favor adicione outro!!!')
                return self.chama_q_disci("add")
            self.banco_add_dis(dados)
        else:
            Label(self.dados_prof, text="", relief="ridge", width=53, height=19, bg="RosyBrown1").place(x=-2, y=-2)

    def banco_add_dis(self, dados):
        dados1 = dados
        conexao = sqlite3.connect("disciplinas.db")
        curso = conexao.cursor()
        curso.execute("create table if not exists disciplinas(NOME text, CODIGO text)")
        curso.execute("insert into disciplinas(NOME, CODIGO) values(?,?)", dados1)
        conexao.commit()
        curso.close()
        conexao.close()
        messagebox.showinfo('INFORMATIVO', 'A DISCIPLINA FOI ADICIONADA COM SUCESSO!')
        Label(self.dados_prof, text="", relief="ridge", width=53, height=19, bg="RosyBrown1").place(x=-2, y=-2)

    def consultar_dis(self):
        dadinhos = self.cpfentry.get()
        dados = self.verificar_tamanho_cod(dadinhos)
        if dados != "Invalido":
            conexao = sqlite3.connect("disciplinas.db")
            curso = conexao.cursor()
            curso.execute("select * from disciplinas where CODIGO = '%s'" % dados)
            x=0
            while True:
                resultado = curso.fetchone()
                if resultado == None:
                    if x == 0:
                        messagebox.showerror('INFORMATIVO', 'A DISCIPLINA NÃO FOI ENCONTRADA')
                        Label(self.dados_prof, text="", relief="ridge", width=53, height=19, bg="RosyBrown1").place(x=-2,y=-2)
                    break
                Label(self.dados_prof, text="", borderwidth=6, relief="ridge", width=50, height=16, bg="RosyBrown1").place(x=0, y=0)
                Label(self.dados_prof, text="DADOS DA DISCIPLINA", font="arial 10 bold").place(x=85, y=0)
                Label(self.dados_prof, text="NOME DA DISCIPLINA:", font="arial 8 bold").place(x=10, y=30)
                Label(self.dados_prof, text="CÓDIGO DA DISCIPLINA:", font="arial 8 bold").place(x=10, y=80)
                Label(self.dados_prof, text= resultado[0], font="arial 10 bold", bg="RosyBrown1").place(x=10, y=50)
                Label(self.dados_prof, text= resultado[1], font="arial 10 bold", bg="RosyBrown1").place(x=10, y=100)
                x += 1
                if self.comando == "atualizar":
                    return self.chama_q_disci("atua")
                if self.comando == "add":
                    Label(self.dados_prof, text="", relief="ridge", width=53, height=19, bg="RosyBrown1").place(x=-2,y=-2)
                    return self.chama_q_turma("add_tur")
                if self.comando == "consultar_turma":
                    return resultado[0]
                if self.comando == "atualizar_turma":
                    return self.atualizar_turma()
        else:
            Label(self.dados_prof, text="", relief="ridge", width=53, height=19, bg="RosyBrown1").place(x=-2, y=-2)

    def atualizar_dis(self):
        codigo =self.cpfentry.get()
        dados = [str(self.nomeentry.get()).title(), codigo]
        conexao = sqlite3.connect("disciplinas.db")
        curso = conexao.cursor()
        curso.execute("update disciplinas set NOME = '{}' where CODIGO = '{}'".format(dados[0],dados[1]))
        messagebox.showinfo('INFORMATIVO', 'OS DADOS FORAM ATUALIZADOS COM SUCESSO!')
        Label(self.dados_prof, text="", relief="ridge", width=53, height=19, bg="RosyBrown1").place(x=-2, y=-2)
        conexao.commit()
        conexao.close()

    def remover_dis(self):
        codigo = self.cpfentry.get()
        conexao = sqlite3.connect("disciplinas.db")
        curso = conexao.cursor()
        curso.execute("delete from disciplinas where CODIGO = '{}'".format(codigo))
        print("registros apagados", curso.rowcount)
        if curso.rowcount == 1:
            conexao.commit()
            messagebox.showinfo('INFORMATIVO', 'DISCIPLINA DELETADA DO SISTEMA COM SUCESSO!')
        else:
            conexao.rollback()
            messagebox.showerror('ERRO', 'OPERAÇÃO SEM SUCESSO, DIGITE UM CÓDIGO VALIDO!')
            conexao.close()
            return self.chama_q_disci("remover")
        Label(self.dados_prof, text="", relief="ridge", width=53, height=19, bg="RosyBrown1").place(x=-2, y=-2)
        conexao.close()

    def mostrar_todas_dis(self):
        Label(self.dados_prof, text="", borderwidth=2, relief="ridge", width=50, height=17, bg="RosyBrown1").place(x=0, y=0)
        Label(self.dados_prof, text="TODAS AS DISCIPLINAS",font="arial 12 bold").place(x= 90, y=15)
        self.scroball = Scrollbar(self.dados_prof)
        self.listbox = Listbox(self.dados_prof, width=53, height=10, yscrollcommand=self.scroball)
        self.listbox.place(x=10,y=50)
        self.scroball.place(x=332, y=50, height=163)
        self.scroball.config(command=self.listbox.yview)
        conexao = sqlite3.connect("disciplinas.db")
        curso = conexao.cursor()
        curso.execute("select * from disciplinas")
        registro = curso.fetchall()
        for dado in registro:
            T = [["NOME:", str(dado[0]).title()], ["CÓDIGO:", str(dado[1]).title()]]
            self.listbox.insert(END,"------------------------------------------------------------------", T[0], T[1])

    # ================================INTERAÇÃO DO MENU DA TURMA =====================================
    def botao_ok_turma(self):
        return self.chama_q_turma("add")

    def botao_add_turma(self):
        return self.chama_q_turma("add_alunos")

    def botao_add_ptma(self):
        return self.chama_q_turma("add_professor")

    def botao_con_turma(self):
        return self.chama_q_turma("consultar_turma")

    def botao_att_turma(self):
        return self.chama_q_turma("atua_turma")

    def botao_rem_turma(self):
        return self.chama_q_turma("remover_turma")

    def botao_most_turma(self):
        return self.chama_q_turma("mostrar_turma")

    def botao_mostrar_profes(self):
        return self.chama_q_turma("mostrar_professor")

    def botao_mostrar_alun_t(self):
        return self.chama_q_turma("mostrar_aluno")

    def avisar(self):
        Label(self.dados_prof, text="", relief="ridge", width=53, height=19, bg="RosyBrown1").place(x=-2, y=-2)
        messagebox.showinfo('INFORMATIVO', 'A TURMA FOI ADICIONADA COM SUCESSO!')

    def chama_q_turma(self, botao):
        self.comando = botao
        if self.comando == "":
            self.dados_prof.place(x=15, y=6000)
        else:
            self.dados_prof = Frame(projeto, width=360, height=258)
            self.dados_prof["bg"] = "RosyBrown1"
            self.dados_prof.place(x=400, y=80)
            Label(self.dados_prof, text="", borderwidth=1, relief="ridge", width=50, height=16, bg="RosyBrown1").place(x=0, y=10)
            Label(self.dados_prof, text="DIGITE OS DADOS QUANDO NECESSARIO", font="arial 8 bold").place(x=55, y=0)
            Label(self.dados_prof, text="CÓDIGO DA TURMA:", font="arial 8 bold").place(x=5, y=30)
            Label(self.dados_prof, text="PERIODO:", font="arial 8 bold").place(x=120, y=30)
            Label(self.dados_prof, text="CODIGO DA DISCIPLINA:", font="arial 8 bold").place(x=190, y=30)
            Label(self.dados_prof, text="CPF DO PROFESSOR:", font="arial 8 bold").place(x=5, y=80)
            Label(self.dados_prof, text="CPF DO ALUNO:", font="arial 8 bold").place(x=5, y=130)
            if self.comando == "add":
                self.CODTURentry = Entry(self.dados_prof, width=3)
                self.CODTURentry.place(x=5, y=50)
                self.CODDentry = Entry(self.dados_prof, width=6)
                self.CODDentry.place(x=120, y=50)
                self.cpfentry = Entry(self.dados_prof, width=5)
                self.cpfentry.place(x=190, y=50)
                Button(self.dados_prof, text="ADICIONAR TURMA", width=20, height=2, bg="PaleTurquoise2", command=self.consultar_dis).place(x=90, y=180)
            if self.comando == "add_tur":
                Label(self.dados_prof, text="", relief="ridge", width=53, height=19, bg="RosyBrown1").place(x=-2, y=-2)
                return self.verificar_tur_j_exist()
            if self.comando == "add_professor":
                self.cpfentry = Entry(self.dados_prof, width=11)
                self.cpfentry.place(x=5, y=100)
                Button(self.dados_prof, text="CONCLUIDO", width=20, height=2, bg="PaleTurquoise2",command=self.botao_add_turma).place(x=10, y=180)
                Button(self.dados_prof, text="ADICIONAR PROFESSOR A TURMA", width=20, height=2, bg="PaleTurquoise2",command=self.consultar_prof).place(x=170, y=180)
            if self.comando == "add_alunos":
                self.cpfentry = Entry(self.dados_prof, width=11)
                self.cpfentry.place(x=5, y=150)
                Button(self.dados_prof, text="CONCLUIDO", width=20, height=2, bg="PaleTurquoise2",command=self.avisar).place(x=10, y=180)
                Button(self.dados_prof, text="ADICIONAR ALUNO NA TURMA", width=20, height=2, bg="PaleTurquoise2",command=self.consultar_alunos).place(x=170, y=180)
            if self.comando == "consultar_turma":
                self.CODTURentry = Entry(self.dados_prof, width=3)
                self.CODTURentry.place(x=5, y=50)
                Button(self.dados_prof, text="CONSULTAR TURMA", width=20, height=2, bg="PaleTurquoise2",command=self.consultar_turma).place(x=90, y=180)
            if self.comando == "atua_turma":
                self.CODTURentry = Entry(self.dados_prof, width=3)
                self.CODTURentry.place(x=5, y=50)
                Button(self.dados_prof, text="ATUALIZAR TURMA", width=20, height=2, bg="PaleTurquoise2",command=self.consultar_turma).place(x=90, y=180)
            if self.comando == "atualizar_turma":
                self.CODDentry = Entry(self.dados_prof, width=6)
                self.CODDentry.place(x=120, y=50)
                self.cpfentry = Entry(self.dados_prof, width=5)
                self.cpfentry.place(x=190, y=50)
                Button(self.dados_prof, text="CANCELAR", width=20, height=2, bg="PaleTurquoise2",command=self.cancelar).place(x=10, y=180)
                Button(self.dados_prof, text="ATUALIZAR TURMA", width=20, height=2, bg="PaleTurquoise2",command=self.consultar_dis).place(x=170, y=180)
            if self.comando == "remover_turma":
                self.CODTURentry = Entry(self.dados_prof, width=3)
                self.CODTURentry.place(x=5, y=50)
                Button(self.dados_prof, text="CANCELAR", width=20, height=2, bg="PaleTurquoise2", command=self.cancelar).place(x=10, y=180)
                Button(self.dados_prof, text="REMOVER TURMA", width=20, height=2, bg="PaleTurquoise2", command=self.consultar_turma).place(x=170, y=180)
            if self.comando == "mostrar_turma":
                return self.mostrar_todas_turm()
            if self.comando == "mostrar_professor":
                self.cpfentry = Entry(self.dados_prof, width=11)
                self.cpfentry.place(x=5, y=100)
                Button(self.dados_prof, text="CONSULTAR TURMAS", width=20, height=2, bg="PaleTurquoise2",command=self.mostrar_todas_turm_prof).place(x=90, y=180)
            if self.comando == "mostrar_aluno":
                self.cpfentry = Entry(self.dados_prof, width=11)
                self.cpfentry.place(x=5, y=150)
                Button(self.dados_prof, text="CONSULTAR TURMAS", width=20, height=2, bg="PaleTurquoise2",command=self.mostrar_todas_turm_alun).place(x=90, y=180)

    def verificar_tur_j_exist(self):
        tur = str(self.CODTURentry.get()).title()
        dados = [tur, self.CODDentry.get(), self.cpfentry.get()]
        conexao = sqlite3.connect("TURMAS.db")
        curso = conexao.cursor()
        curso.execute("Create table if not exists DADOS(CODIGO_TURMA  text,PERIODO text, CODIGO_DISCIPLINA text)")
        curso.execute("select * from DADOS where CODIGO_TURMA = '%s'" %dados[0])
        while True:
            resultado = curso.fetchone()
            if resultado == None:
                break
            messagebox.showerror('CODIGO DA TURMA JÁ EXISTE', 'O CODIGO que você digitou já existe, por favor adicione outro!!!')
            return self.chama_q_turma("add")
        self.add_turma(dados)

    def add_turma(self, dado):
        dados = dado
        conexao = sqlite3.connect("TURMAS.db")
        curso = conexao.cursor()
        curso.execute("Create table if not exists DADOS(CODIGO_TURMA  text,PERIODO text, CODIGO_DISCIPLINA text)")
        curso.execute("Create table if not exists Alunos(CODIGO_TURMA  text, CPF_ALUNOS text)")
        curso.execute("Create table if not exists PROFESSORES(CODIGO_TURMA  text,CPF_PROFESSORES text)")
        curso.execute("insert into DADOS(CODIGO_TURMA, PERIODO, CODIGO_DISCIPLINA) values(?,?,?)", dados)
        conexao.commit()
        curso.close()
        conexao.close()
        messagebox.showwarning('ATENÇÃO','DADOS DA TURMA ADCIONADO COM SUCESSO:\nCaso queira adcionar outro professor a turma, DIGITE O CPF e pressione o botão "ADCIONAR!\nCaso não queira mais adicionar professores a turma, pressione apenas o botão "CONCLUIDO"\n O MESMO FUNCIONA PARA ALUNO')
        return self.chama_q_turma("add_professor")

    def add_profe_t(self):
        dados = [str(self.CODTURentry.get()).title(), self.cpfentry.get()]
        conexao = sqlite3.connect("TURMAS.db")
        curso = conexao.cursor()
        curso.execute("insert into PROFESSORES(CODIGO_TURMA, CPF_PROFESSORES) values(?,?)", dados)
        conexao.commit()
        curso.close()
        conexao.close()
        messagebox.showinfo('INFORMATIVO', 'PROFESSOR ADICIONADO A TURMA')
        return self.chama_q_turma("add_professor")

    def add_alunos_t(self):
        dados = [str(self.CODTURentry.get()).title(), self.cpfentry.get()]
        conexao = sqlite3.connect("TURMAS.db")
        curso = conexao.cursor()
        curso.execute("insert into Alunos(CODIGO_TURMA, CPF_ALUNOS) values(?,?)", dados)
        conexao.commit()
        curso.close()
        conexao.close()
        messagebox.showinfo('INFORMATIVO', 'ALUNO ADICIONADO A TURMA!')
        return self.chama_q_turma("add_alunos")

    def consultar_turma(self):
        Label(self.dados_prof, text="", borderwidth=2, relief="ridge", width=50, height=17, bg="RosyBrown1").place(x=0,y=0)
        Label(self.dados_prof, text="DADOS DA TURMA", font="arial 12 bold").place(x=90, y=15)
        self.scroball = Scrollbar(self.dados_prof)
        self.listbox = Listbox(self.dados_prof, width=53, height=10, yscrollcommand=self.scroball)
        self.listbox.place(x=10, y=50)
        self.scroball.place(x=332, y=50, height=163)
        self.scroball.config(command=self.listbox.yview)
        codigo = str(self.CODTURentry.get()).title()
        conexao = sqlite3.connect("TURMAS.db")
        curso = conexao.cursor()
        curso.execute("select * from DADOS where CODIGO_TURMA = '%s'" %codigo)
        x = 0
        while True:
            resultado = curso.fetchone()
            if resultado == None:
                if x == 0:
                    Label(self.dados_prof, text="", relief="ridge", width=53, height=19, bg="RosyBrown1").place(x=-2, y=-2)
                    messagebox.showerror('INFORMATIVO', 'A TURMA NÃO FOI ENCONTRADA')
                break
            x += 1
            curso.execute("select * from PROFESSORES where CODIGO_TURMA = '%s'" % codigo)
            resultadop = curso.fetchall()
            curso.execute("select * from Alunos where CODIGO_TURMA = '%s'" % codigo)
            resultadoa = curso.fetchall()
            self.disciplina = self.consultar_dis_t(resultado[2])
            i = [["TURMA:", resultado[0]], ["PERIODO:", resultado[1]], ["DISCIPLINA:",str(self.disciplina).title()]]
            self.listbox.insert(END, i[0], i[1], i[2], "---------------------PROFESSORES(AS)------------------------------", )
            for professor in resultadop:
                self.professor = self.consultar_prof_t(str(professor[1]))
                p = [["PROFESSO(A):", str(self.professor).title()], "------------------------------------------------------------------"]
                self.listbox.insert(END, p[0])
            self.listbox.insert(END, "----------------------------ALUNOS(AS)---------------------------")
            for aluno in resultadoa:
                self.alunos = self.consultar_alunos_TUR(aluno[1])
                p = [["ALUNO(A):",str(self.alunos).title()], "------------------------------------------------------------------"]
                self.listbox.insert(END, p[0],p[1])
            if self.comando == "atua_turma":
                return self.chama_q_turma("atualizar_turma")
            if self.comando == "remover_turma":
                return self.remover_turma()

    def consultar_dis_t(self, dado):
        dados = dado
        conexao = sqlite3.connect("disciplinas.db")
        curso = conexao.cursor()
        curso.execute("select * from disciplinas where CODIGO = '%s'" % dados)
        x=0
        while True:
            resultado = curso.fetchone()
            if resultado == None:
                if x == 0:
                    Label(self.dados_prof, text="", relief="ridge", width=53, height=19, bg="RosyBrown1").place(x=-2,y=-2)
                break
            x += 1
            return resultado[0]

    def consultar_alunos_TUR(self, cpf):
        dados = cpf
        conexao = sqlite3.connect("alunos.db")
        curso = conexao.cursor()
        curso.execute("select * from alunos where CPF = '%s'" % dados)
        x = 0
        while True:
            resultado = curso.fetchone()
            if resultado == None:
                if x == 0:
                    Label(self.dados_prof, text="", relief="ridge", width=53, height=19, bg="RosyBrown1").place(x=-2, y=-2)
                break
            x += 1
            return resultado[0]

    def consultar_prof_t(self, cpf):
        dados = cpf
        conexao = sqlite3.connect("professores.db")
        curso = conexao.cursor()
        curso.execute("select * from professores where CPF = '{}'".format(dados))
        x=0
        while True:
            resultado = curso.fetchone()
            if resultado == None:
                if x == 0:
                    Label(self.dados_prof, text="", relief="ridge", width=53, height=19, bg="RosyBrown1").place(x=-2,y=-2)
                break
            x += 1
            return resultado[0]

    def atualizar_turma(self):
        dados = [str(self.CODTURentry.get()).title(), self.CODDentry.get(), self.cpfentry.get()]
        conexao = sqlite3.connect("TURMAS.db")
        curso = conexao.cursor()
        curso.execute("update DADOS set PERIODO = '{}' where CODIGO_TURMA = '{}'".format(dados[1], dados[0]))
        curso.execute("update DADOS set CODIGO_DISCIPLINA = '{}'  where CODIGO_TURMA = '{}'".format(dados[2], dados[0]))
        Label(self.dados_prof, text="", relief="ridge", width=53, height=19, bg="RosyBrown1").place(x=-2, y=-2)
        messagebox.showwarning('INFORMATIVO','TURMA ATUALIZADA COM SUCESSO:\nCaso não queira mais adicionar professores a turma, pressione o botão "CONCLUIDO"\nCaso queira adcionar outro professor a turma, Digte o CPF do professor(a) e pressione o outro botão, o mesmo funciona pararr ALUNO!')
        conexao.commit()
        conexao.close()
        return self.chama_q_turma("add_professor")

    def remover_turma(self):
        codigo = str(self.CODTURentry.get()).title()
        conexao = sqlite3.connect("TURMAS.db")
        curso = conexao.cursor()
        curso.execute("delete from DADOS where CODIGO_TURMA = '{}'".format(codigo))
        curso.execute("delete from PROFESSORES where CODIGO_TURMA = '{}'".format(codigo))
        curso.execute("delete from Alunos where CODIGO_TURMA = '{}'".format(codigo))
        print("registros apagados", curso.rowcount)
        if curso.rowcount > 0:
            conexao.commit()
            Label(self.dados_prof, text="", relief="ridge", width=53, height=19, bg="RosyBrown1").place(x=-2, y=-2)
            messagebox.showinfo('INFORMATIVO', 'TURMA DELETADA DO SISTEMA COM SUCESSO!')
        else:
            conexao.rollback()
            Label(self.dados_prof, text="", relief="ridge", width=53, height=19, bg="RosyBrown1").place(x=-2, y=-2)
            messagebox.showerror('ERRO', 'OPERAÇÃO SEM SUCESSO, DIGITE UM CÓDIGO VALIDO!')
            conexao.close()
            return self.chama_q_turma("remover_turma")
        conexao.close()

    def mostrar_todas_turm(self):
        Label(self.dados_prof, text="", borderwidth=2, relief="ridge", width=50, height=17, bg="RosyBrown1").place(x=0,y=0)
        Label(self.dados_prof, text="TODAS AS TURMA", font="arial 12 bold").place(x=90, y=15)
        self.scroball = Scrollbar(self.dados_prof)
        self.listbox = Listbox(self.dados_prof, width=53, height=10, yscrollcommand=self.scroball)
        self.listbox.place(x=10,y=50)
        self.scroball.place(x=332, y=50, height=163)
        self.scroball.config(command=self.listbox.yview)
        conexao = sqlite3.connect("TURMAS.db")
        curso = conexao.cursor()
        curso.execute("select * from DADOS")
        registro = curso.fetchall()
        for dado in registro:
            self.disciplina = self.consultar_dis_t(dado[2])
            i = [["TURMA:", dado[0]], ["PERIODO:", dado[1]], ["DISCIPLINA:", str(self.disciplina).title()],"------------------------------------------------------------------"]
            self.listbox.insert(END, i[0], i[1], i[2], i[3])

    def mostrar_todas_turm_prof(self):
        Label(self.dados_prof, text="", borderwidth=2, relief="ridge", width=50, height=17, bg="RosyBrown1").place(x=0,y=0)
        Label(self.dados_prof, text="TODAS AS TURMA DO PROFESSOR", font="arial 12 bold").place(x=40, y=15)
        self.scroball = Scrollbar(self.dados_prof)
        self.listbox = Listbox(self.dados_prof, width=53, height=10, yscrollcommand=self.scroball)
        self.listbox.place(x=10,y=50)
        self.scroball.place(x=332, y=50, height=163)
        self.scroball.config(command=self.listbox.yview)
        cpf = self.cpfentry.get()
        conexao = sqlite3.connect("TURMAS.db")
        curso = conexao.cursor()
        curso.execute("select * from PROFESSORES where CPF_PROFESSORES = '{}'".format(cpf))
        registro = curso.fetchall()
        if len(registro) > 0:
            for dados in registro:
                curso.execute("select * from DADOS where CODIGO_TURMA = '{}'".format(dados[0]))
                registro1 = curso.fetchall()
                for dado in registro1:
                    self.disciplina = self.consultar_dis_t(dado[2])
                    i = [["TURMA:", dado[0]], ["PERIODO:", dado[1]], ["DISCIPLINA:", str(self.disciplina).title()],"------------------------------------------------------------------"]
                    self.listbox.insert(END, i[0], i[1], i[2], i[3])
        else:
            messagebox.showerror('INFORMATIVO', 'O PROFESSOR(A) NÃO FOI ENCONTRADO')
            Label(self.dados_prof, text="", relief="ridge", width=53, height=19, bg="RosyBrown1").place(x=-2, y=-2)

    def mostrar_todas_turm_alun(self):
        Label(self.dados_prof, text="", borderwidth=2, relief="ridge", width=50, height=17, bg="RosyBrown1").place(x=0,y=0)
        Label(self.dados_prof, text="TODAS AS TURMA DO ALUNO", font="arial 12 bold").place(x=70, y=15)
        self.scroball = Scrollbar(self.dados_prof)
        self.listbox = Listbox(self.dados_prof, width=53, height=10, yscrollcommand=self.scroball)
        self.listbox.place(x=10,y=50)
        self.scroball.place(x=332, y=50, height=163)
        self.scroball.config(command=self.listbox.yview)
        cpf = self.cpfentry.get()
        conexao = sqlite3.connect("TURMAS.db")
        curso = conexao.cursor()
        curso.execute("select * from Alunos where CPF_ALUNOS = '{}'".format(cpf))
        registro = curso.fetchall()
        if len(registro) > 0:
            for dados in registro:
                curso.execute("select * from DADOS where CODIGO_TURMA = '{}'".format(dados[0]))
                registro1 = curso.fetchall()
                for dado in registro1:
                    self.disciplina = self.consultar_dis_t(dado[2])
                    i = [["TURMA:", dado[0]], ["PERIODO:", dado[1]], ["DISCIPLINA:", str(self.disciplina).title()],"------------------------------------------------------------------"]
                    self.listbox.insert(END, i[0], i[1], i[2], i[3])
        else:
            messagebox.showerror('INFORMATIVO', 'O ALUNO(A) NÃO FOI ENCONTRADO')
            Label(self.dados_prof, text="", relief="ridge", width=53, height=19, bg="RosyBrown1").place(x=-2, y=-2)

# ================================INTERAÇÃO DA INTERFACE COM OO=====================================
projeto = Tk()
projeto.title("2º PARTE DO PROJETO- AURILENE SILVA BAGAGI")
projeto.geometry("800x400+200+80")
Interface(projeto)
projeto.mainloop()
