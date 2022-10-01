from distutils.command.build import build
import re
from tkinter import *
from tkinter import ttk
from unittest import result


cor1="#3b3b3b" #preta
cor2="#feffff" #branco
cor3="#38576b" #azul
cor4="#eceff1" #cizenta
cor5="#eceff1" #cizenta
cor6="#ffab40" #laranja


janela =Tk()
janela.title("Calculadora")
janela.geometry("235x310")

janela.config(bg=cor5)

#tela da calculadora
frame_tela = Frame(janela, width=220, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

#corpo da calculadora
frame_corpo = Frame(janela, width=235, height=268, bg=cor6)
frame_corpo.grid(row=1, column=0)

#variavel todos os valores
todos_valores=""

#criando função
def entrar_valores(event):
    global todos_valores
    todos_valores = todos_valores + str(event) 
    

    #passando o valor para a tela da calculadora
    valor_texto.set(todos_valores) #mesmo que print


#função para calcular 

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    print(resultado)

    valor_texto.set(str(resultado))
    todos_valores=""
    

        




#criando label

valor_texto = StringVar()

app_label = Label(frame_tela, textvariable=valor_texto, width=21, bg=cor3, fg=cor2, font=("Ive 13 bold"), height=3, padx=2, relief=FLAT, ancho="e" )
app_label.place(x=0, y=0)


#função limpar tela
def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")
   


#criando botoes

b_1=Button(frame_corpo, command=limpar_tela, text="C", width=11, height=2, bg=cor4, font=("Ive 13 bold"), relief=RAISED, overrelief=RIDGE) 
b_1.place(x=0, y=0)
#font para a letra dentro do botão
#relief para trazer a letra mais para a frente
#overreief descreve o que apresentar quando o mause passar por cima

b_2=Button(frame_corpo, command=lambda:entrar_valores("%"), text="%", width=5, height=2, bg=cor4, font=("Ive 13 bold"), relief=RAISED, overrelief=RIDGE)
b_2.place(x=120, y=0)

b_3=Button(frame_corpo, command=lambda:entrar_valores("/"), text="/", width=5, height=2, bg=cor5, fg=cor3, font=("Ive 13 bold"), relief=RAISED, overrelief=RIDGE) #fg é cor da letra
b_3.place(x=180, y=0)



b_4=Button(frame_corpo, command=lambda:entrar_valores("7"), text="7", width=5, height=2, bg=cor5, fg=cor3, font=("Ive 13 bold"), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)

b_5=Button(frame_corpo, command=lambda:entrar_valores("8"), text="8", width=5, height=2, bg=cor5, fg=cor3, font=("Ive 13 bold"), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y =52)

b_6=Button(frame_corpo, command=lambda:entrar_valores("9"), text="9", width=5, height=2, bg=cor5, fg=cor3, font=("Ive 13 bold"), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=52)

b_7=Button(frame_corpo, command=lambda:entrar_valores("*"), text="*", width=5, height=2, bg=cor5, fg=cor3, font=("Ive 13 bold"), relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=52)



b_8=Button(frame_corpo, command=lambda:entrar_valores("4"), text="4", width=5, height=2, bg=cor5, fg=cor3, font=("Ive 13 bold"), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)

b_9=Button(frame_corpo, command=lambda:entrar_valores("5"), text="5", width=5, height=2, bg=cor5, fg=cor3, font=("Ive 13 bold"), relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=104)

b_10=Button(frame_corpo, command=lambda:entrar_valores("6"), text="6", width=5, height=2, bg=cor5, fg=cor3, font=("Ive 13 bold"), relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=104)

b_11=Button(frame_corpo, command=lambda:entrar_valores("-"), text="-", width=5, height=2, bg=cor5, fg=cor3, font=("Ive 13 bold"), relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=104)



b_12=Button(frame_corpo, command=lambda:entrar_valores("1"), text="1", width=5, height=2, bg=cor5, fg=cor3, font=("Ive 13 bold"), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)

b_13=Button(frame_corpo, command=lambda:entrar_valores("2"), text="2", width=5, height=2, bg=cor5, fg=cor3, font=("Ive 13 bold"), relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=156)

b_14=Button(frame_corpo, command=lambda:entrar_valores("3"), text="3", width=5, height=2, bg=cor5, fg=cor3, font=("Ive 13 bold"), relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=156)

b_15=Button(frame_corpo, command=lambda:entrar_valores("+"), text="+", width=5, height=2, bg=cor5, fg=cor3, font=("Ive 13 bold"), relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=156)


b_16=Button(frame_corpo, command=lambda:entrar_valores("0"), text="0", width=11, height=2, bg=cor4, fg=cor3,  font=("Ive 13 bold"), relief=RAISED, overrelief=RIDGE) 
b_16.place(x=0, y=208)

b_17=Button(frame_corpo, command=lambda:entrar_valores("."), text=".", width=5, height=2, bg=cor4, fg=cor3, font=("Ive 13 bold"), relief=RAISED, overrelief=RIDGE)
b_17.place(x=118, y=208)

b_18=Button(frame_corpo, command=calcular, text="=", width=5, height=2, bg=cor5, fg=cor3, font=("Ive 13 bold"), relief=RAISED, overrelief=RIDGE) #fg é cor da letra
b_18.place(x=177, y=208)




janela.mainloop()

