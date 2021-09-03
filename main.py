
from conversores import conversor
from tkinter import *

def validaInt (value) :
    try:
        int(value)
        return True
    except ValueError:
        print('O valor informado não é um numero inteiro')
        return False

def getValueForConvert():
    value = input.get()
    if (validaInt(value)):
        bina = conversor.convertendoPorBase(int(value), 2)
        octal = conversor.convertendoPorBase(int(value), 8)

        resposta = f'''
        Valor Informador: {value}
        Binario: {bina}
        Octal: {octal}
        '''
        resultados['text'] = resposta

janela = Tk()
janela.title("Converter decimal")
janela.geometry("200x200")
informacao = Label(janela, text="Informe um valor")
informacao.grid(column=0, row=0, padx=10, pady=10)

input = Entry(janela)
input.grid(column=0, row=1, padx=10, pady=10)


botao = Button(janela, text="Converter", command=getValueForConvert)
botao.grid(column=0, row=2, padx=10, pady=10)
resultados = Label(janela)
resultados.grid(column=0, row=3, padx=10, pady=10)
janela.mainloop()