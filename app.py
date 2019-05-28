# -*- coding:utf-8 -*-
import re
try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk
except:
    print("Ops.. não foi possivel executar a aplicação")

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

def controleBotoes(tecla):
    display.insert(tk.END, tecla)

def controleDisplayInput(valorSePermitido, tecla):
    return tecla in "0123456789+-*/." and not re.search("[\.\+\-\*\/][\.\+\-\*\/]", valorSePermitido) and not re.search("\d{1,}\.\d{1,}\.", valorSePermitido) and not re.search("^[\.\+\-\*\/]", valorSePermitido)

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

def calcularExpressao(evento=None):
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
displayValidacao = (app.register(controleDisplayInput), '%P', '%S')
display = tk.Entry(app, validate = "key", validatecommand = displayValidacao)
display.bind("<Return>", calcularExpressao)

btn0 = tk.Button(app, text="0", command=lambda: controleBotoes("0"))
btn1 = tk.Button(app, text="1", command=lambda: controleBotoes("1"))
btn2 = tk.Button(app, text="2", command=lambda: controleBotoes("2"))
btn3 = tk.Button(app, text="3", command=lambda: controleBotoes("3"))
btn4 = tk.Button(app, text="4", command=lambda: controleBotoes("4"))
btn5 = tk.Button(app, text="5", command=lambda: controleBotoes("5"))
btn6 = tk.Button(app, text="6", command=lambda: controleBotoes("6"))
btn7 = tk.Button(app, text="7", command=lambda: controleBotoes("7"))
btn8 = tk.Button(app, text="8", command=lambda: controleBotoes("8"))
btn9 = tk.Button(app, text="9", command=lambda: controleBotoes("9"))
btnMais = tk.Button(app, text="+", command=lambda: controleBotoes("+"))
btnMenos = tk.Button(app, text="-", command=lambda: controleBotoes("-"))
btnVezes = tk.Button(app, text="*", command=lambda: controleBotoes("*"))
btnDivisao = tk.Button(app, text="/", command=lambda: controleBotoes("/"))
btnIgual = tk.Button(app, text="=", command=calcularExpressao)
btnPonto = tk.Button(app, text=".", command=lambda: controleBotoes("."))
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
