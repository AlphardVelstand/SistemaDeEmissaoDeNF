import sys
from tkinter import *

#Definindo nome da Janela exibida
window = Tk()
#Dimensoes da janela
window.geometry("800x650")
#Tutulo
window.title("Emissor no NF Velstand Versão 0.1")

#Definindo variavel que armazena usuario e senha
usernameVar = StringVar()
passwordVar = StringVar()

quantidadeVar = StringVar()

#Definindo variavel que armazena os dados do produto no cadastro
addItemNomeVar = StringVar()
addValorVar = StringVar()
addTipoVar = StringVar()
addDataVar = StringVar()
addTipoServVar = StringVar() #Tipo do serviço selecionado na combo box

#####################################
#combobox lista de itens de serviço
options=["Topo de bolo", "Lembrancinhas", "Rosas de Papel"]
itemVariable = StringVar()
itemVariable.set = (options[0])

##############################################################################################
def adminLogin():
    titleLabel = Label(window, text ="SISTEMA DE FATURAMENTO", font="arial 20", fg="red")
    titleLabel.grid(row=0, column=0, columnspan=4, padx=(40,0), pady=(10,0))

    loginLabel = Label(window,text="Acessando ao sistema:", font="arial 10")
    loginLabel.grid(row=1,column=2, padx=(50,0), columnspan=2, pady=10)

    userLabel = Label(window, text="Usuário:")
    userLabel.grid(row=2, column=2, padx=20, pady=10)

    senhaLabel = Label(window, text="Senha:")
    senhaLabel.grid(row=3, column=2, padx=20, pady=10)

    usuarioEntry = Entry(window,textvariable=usernameVar)
    usuarioEntry.grid(row=2, column=3, padx=20, pady=10)

    senhaEntry = Entry(window, textvariable=passwordVar, show="*")
    senhaEntry.grid(row=3, column=3, padx=20, pady=10)

    loginButton = Button(window,text="Acessar", width=8, height=2)
    loginButton.grid(row=4, column=2, padx=20, pady=10, columnspan=2)

    botaoSair = Button(window, text="Sair", width=8, height=2)
    botaoSair.grid(row=4, column=3, padx=20, pady=10, columnspan=2) #command=(sair)
##################################################################################################
def mainWindow():#Tela de adicionar produtos / serviços
    titleLabel = Label(window, text ="SISTEMA DE FATURAMENTO", font="arial 20", fg="green")
    titleLabel.grid(row=0, column=1, columnspan=3, pady=(10,0))

    addButton = Button(window, text="Add itens", width=15, height=2)
    addButton.grid(row=1, column=0, pady=(10,0), padx=(10,0))

    botaoSair = Button(window, text="Sair", width=15, height=2)
    botaoSair.grid(row=1, column=4, pady=(10,0), padx=(10,0)) #command=(sair)

    buttonNf = Button(window, text="Gerar Nf ",width=15, height=2)
    buttonNf.grid(row=2, column=4, pady=(10,0), padx=(10,0))

#chamando o combobox com os itens do serviço
    itemsComboBoxServ = OptionMenu(window, itemVariable, *options)
    itemsComboBoxServ.grid(row=2, column=1, pady=(10,0), padx=(5,0))

    selItemLabel = Label(window,text="Selecionar Item: ", font="arial 12")
    selItemLabel.grid(row=2,column=0, pady=(10,0), padx=(5,0))

    quantidadeLabel = Label(window,text="Quantidade:", font="arial 12")
    quantidadeLabel.grid(row=2,column=2, padx=(5,0), pady=(5,0))

    quantidadeEntry = Entry(window, textvariable=quantidadeVar)
    quantidadeEntry.grid(row=2, column=3, pady=(10,0), padx=(5,0))
###################################################################################
def addItem():
    titleLabel = Label(window, text ="ADCIONAR NOVO ITEM", width=40 ,font="arial 20", fg="blue")
    titleLabel.grid(row=0, column=1, columnspan=4, pady=(10,0))

    itemNomeLabel = Label(window,text="Nome do Produto:", font="arial 10")
    itemNomeLabel.grid(row=1,column=1, pady=(10,0))

    valorProdLabel = Label(window, text="Valor:", font="arial 10")
    valorProdLabel.grid(row=1, column=2, padx=20, pady=10)

    dataProdLabel = Label(window, text="Data:", font="arial 10")
    dataProdLabel.grid(row=1, column=3, padx=20, pady=10)

#Usar a comboBox
    tipoDoProdLabel = Label(window, text="Tipo do Produto:", font="arial 10")
    tipoDoProdLabel.grid(row=1, column=4, pady=10)

    nomeProdEntry = Entry(window, textvariable=addItemNomeVar)
    nomeProdEntry.grid(row=2, column=1, padx=20, pady=10)

    valorProdEntry = Entry(window, textvariable=addValorVar)
    valorProdEntry.grid(row=2, column=2, padx=20, pady=10)

    dataProdEntry = Entry(window, textvariable=addValorVar)
    dataProdEntry.grid(row=2, column=3, padx=20, pady=10)

    salvarButton = Button(window,text="Salvar", width=8, height=2)
    salvarButton.grid(row=6, column=1, padx=20, pady=10)

    botaoSair = Button(window, text="Sair", width=8, height=2)
    botaoSair.grid(row=6, column=2, padx=20, pady=10) #command=(sair)

    limparButton = Button(window,text="limpar", width=8, height=2)
    limparButton.grid(row=6, column=3, padx=20, pady=10)

    delButton = Button(window,text="Deletar", width=8, height=2)
    delButton.grid(row=6, column=4, padx=20, pady=10)
#Chamando Tela de add Item
addItem()
#Chamando a tela main
#mainWindow()
#Chamando a tela login
#adminLogin()
#Função sair
def sair():
    sys.exit()
#Mantendo janela aberta
window.mainloop()