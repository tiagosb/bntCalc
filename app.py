# -*- coding:utf-8 -*-
import re
try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

app = tk.Tk()
app.title("BntCalc")
app.option_add("*Font", "Verdana 14 normal")
app.option_add("*Entry.Font", "Verdana 22 normal")
app.option_add("*Label.Font", "Verdana 25 bold")

app.columnconfigure(0, weight=1)
app.columnconfigure(1, weight=1)
app.columnconfigure(2, weight=1)
app.columnconfigure(3, weight=1)

app.rowconfigure(0, weight=0)
app.rowconfigure(1, weight=2)
app.rowconfigure(2, weight=1)
app.rowconfigure(3, weight=1)
app.rowconfigure(4, weight=1)
app.rowconfigure(5, weight=1) 
app.rowconfigure(6, weight=1)

def controle_botoes(tecla):
    display.insert(tk.END, tecla)

def controle_display_input(valor_se_permitido, tecla):
    #Evita a entrada de caracteres invalidos
    tecla_valida = tecla in "0123456789+-*/."
    
    #Evita operador ao lado de operador
    posicao_operador_valida = not re.search("[\.\+\-\*\/][\.\+\-\*\/]", valor_se_permitido)
    
    #Evita ponto decimal ao lado de ponto decimal
    ponto_decimal_valido = not re.search("\d{1,}\.\d{1,}\.", valor_se_permitido)  

    #Evita iniciar com operador ou ponto decimal
    inicio_valido = not re.search("^[\.\+\-\*\/]", valor_se_permitido)

    return tecla_valida and posicao_operador_valida and ponto_decimal_valido and inicio_valido

#resolve multiplicação e divisão
def resolvePrecedencia(expressao):
    _expressao = expressao
    for i in range(0, len(expressao)):
        try:
            if expressao[i] == "*":
                expressao[i] = str( float(expressao[i-1]) * float(expressao[i+1]) )
                expressao.pop(i+1)
                expressao.pop(i-1)
                return expressao
            elif expressao[i] == "/":
                expressao[i] = str( float(expressao[i-1]) / float(expressao[i+1]) )
                expressao.pop(i+1)
                expressao.pop(i-1)
                return expressao
        except Exception as e:
            print("Erro", str(e))
            return _expressao

def somaEsubtracao(expressao):
    _expressao = expressao
    try:
        for i in range(0, len(expressao)):
            if expressao[i] == "+":
                expressao[i] = str(float(expressao[i-1]) + float(expressao[i+1]))
                expressao.pop(i+1)
                expressao.pop(i-1)
                return expressao
            elif expressao[i] == "-":
                expressao[i] = str(float(expressao[i-1]) - float(expressao[i+1]))
                expressao.pop(i+1)
                expressao.pop(i-1)
                return expressao
    except Exception as e:
            print("Erro", str(e))
            return _expressao

def arredonda(numero):
    decimal = re.search("\.(\d{1,})", str(numero)).group(1)
    if int(decimal) > 0:
        return round(float(numero), 2)
    return int(float(numero))

def calcular_expressao(evento=None):
    try:
        expressao = display.get()    
        if len(expressao) == 0:
            return False
        #Separa os numeros dos operadores
        elementos = []
        elemento = ''
        for i in range(0, len(expressao)):
            if expressao[i] in "+-*/":
                elementos.append(elemento)
                elemento = ''
                elementos.append(expressao[i])
            else:
                elemento += expressao[i]
        if not elemento == '':
            elementos.append(elemento)
        
        #Efetua o calculo
        while "*" in elementos or "/" in elementos:
            elementos = resolvePrecedencia(elementos)

        while "+" in elementos or "-" in elementos:
            elementos = somaEsubtracao(elementos)

        lbDisplay['text'] = str( arredonda(elementos[0]) )
    except Exception as e:
        print("Erro,",str(e))

lbDisplay = tk.Label(app, text="0", anchor="w")
displayValidacao = (app.register(controle_display_input), '%P', '%S')
display = tk.Entry(app, validate = "key", validatecommand = displayValidacao)
display.bind("<Return>", calcular_expressao)

btn0 = tk.Button(app, text="0", command=lambda: controle_botoes("0"))
btn1 = tk.Button(app, text="1", command=lambda: controle_botoes("1"))
btn2 = tk.Button(app, text="2", command=lambda: controle_botoes("2"))
btn3 = tk.Button(app, text="3", command=lambda: controle_botoes("3"))
btn4 = tk.Button(app, text="4", command=lambda: controle_botoes("4"))
btn5 = tk.Button(app, text="5", command=lambda: controle_botoes("5"))
btn6 = tk.Button(app, text="6", command=lambda: controle_botoes("6"))
btn7 = tk.Button(app, text="7", command=lambda: controle_botoes("7"))
btn8 = tk.Button(app, text="8", command=lambda: controle_botoes("8"))
btn9 = tk.Button(app, text="9", command=lambda: controle_botoes("9"))
btnMais = tk.Button(app, text="+", command=lambda: controle_botoes("+"))
btnMenos = tk.Button(app, text="-", command=lambda: controle_botoes("-"))
btnVezes = tk.Button(app, text="*", command=lambda: controle_botoes("*"))
btnDivisao = tk.Button(app, text="/", command=lambda: controle_botoes("/"))
btnIgual = tk.Button(app, text="=", command=calcular_expressao)
btnPonto = tk.Button(app, text=".", command=lambda: controle_botoes("."))
btnLimpar = tk.Button(app, text="C")
btnDel = tk.Button(app, text="Del")

lbDisplay.grid(row=1, column=0, columnspan=4, sticky="wens", padx=4, pady=4)
display.grid(row=2, column=0, columnspan=4, sticky="wens", padx=4, pady=4)

btn7.grid(row=3, column=0, sticky="wens")
btn8.grid(row=3, column=1, sticky="wens")
btn9.grid(row=3, column=2, sticky="wens")
btnDivisao.grid(row=3, column=3, sticky="wens")

btn4.grid(row=4, column=0, sticky="wens")
btn5.grid(row=4, column=1, sticky="wens")
btn6.grid(row=4, column=2, sticky="wens")
btnMenos.grid(row=4, column=3, sticky="wens")

btn1.grid(row=5, column=0, sticky="wens")
btn2.grid(row=5, column=1, sticky="wens")
btn3.grid(row=5, column=2, sticky="wens")
btnVezes.grid(row=5, column=3, sticky="wens")

btn0.grid(row=6, column=0, sticky="wens")
btnPonto.grid(row=6, column=1, sticky="wens")
btnMais.grid(row=6, column=3, sticky="wens")
btnIgual.grid(row=6, column=2, sticky="wens")
app.mainloop()
