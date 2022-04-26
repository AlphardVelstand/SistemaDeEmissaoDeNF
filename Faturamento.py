import sys
from tkinter import *

#Definindo nome da Janela exibida
window = Tk()
#Dimensoes da janela
window.geometry("600x600")
#Tutulo
window.title("Emissor no NF Velstand Versão 0.1")

#Definindo variavel que armazena usuario e senha
usernameVar = StringVar()
passwordVar = StringVar()

def adminLogin():
    titleLabel = Label(window, text ="FATURAMENTO")
    titleLabel.grid(row=0, column=0, columnspan=2, padx=(40,0), pady=(10,0))

    loginLabel = Label(window,text="Acessando ao sistema:")
    loginLabel.grid(row=1,column=2, padx=20, pady=10)

    userLabel = Label(window, text="Usuário:")
    userLabel.grid(row=2, column=2, padx=20, pady=10)

    senhaLabel = Label(window, text="Senha:")
    senhaLabel.grid(row=3, column=2, padx=20, pady=10)

    botaoSair = Button(window, text="Sair")
    botaoSair.grid(row=4, column=2, padx=20, pady=10) #command=(sair)

    usuarioEntry = Entry(window,textvariable=usernameVar)
    usuarioEntry.grid(row=2, column=3, padx=20, pady=10)

    senhaEntry = Entry(window, textvariable=passwordVar)
    senhaEntry.grid(row=3, column=3, padx=20, pady=10)

adminLogin()
#Função sair
def sair():
    sys.exit()
#Mantendo janela aberta
window.mainloop()