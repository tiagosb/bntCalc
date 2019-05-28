# -*- coding:utf-8 -*-

try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk
except:
    print("Ops.. não foi possivel executar a aplicação")

app = tk.Tk()


app.columnconfigure(0, weight=1)
app.columnconfigure(1, weight=1)
app.columnconfigure(2, weight=1)
app.columnconfigure(3, weight=1)

app.rowconfigure(0, weight=1)
app.rowconfigure(1, weight=1)
app.rowconfigure(2, weight=1)
app.rowconfigure(3, weight=1)

btn0 = tk.Button(app, text="0")
btn1 = tk.Button(app, text="1")
btn2 = tk.Button(app, text="2")
btn3 = tk.Button(app, text="3")
btn4 = tk.Button(app, text="4")
btn5 = tk.Button(app, text="5")
btn6 = tk.Button(app, text="6")
btn7 = tk.Button(app, text="7")
btn8 = tk.Button(app, text="8")
btn9 = tk.Button(app, text="9")
btnMais = tk.Button(app, text="+")
btnMenos = tk.Button(app, text="-")
btnVezes = tk.Button(app, text="*")
btnDivisao = tk.Button(app, text="/")
btnIgual = tk.Button(app, text="=")
btnPonto = tk.Button(app, text=".")
btnLimpar = tk.Button(app, text="C")
btnDel = tk.Button(app, text="Del")

btn1.grid(row=2, column=0, sticky="wens")
btn2.grid(row=2, column=1, sticky="wens")
btn3.grid(row=2, column=2, sticky="wens")

btn4.grid(row=1, column=0, sticky="wens")
btn5.grid(row=1, column=1, sticky="wens")
btn6.grid(row=1, column=2, sticky="wens")
btnMenos.grid(row=1, column=3, sticky="wens")

btn7.grid(row=0, column=0, sticky="wens")
btn8.grid(row=0, column=1, sticky="wens")
btn9.grid(row=0, column=2, sticky="wens")
btnDivisao.grid(row=0, column=3, sticky="wens")

btn0.grid(row=3, column=0, sticky="wens")
btnPonto.grid(row=3, column=1, sticky="wens")
btnMais.grid(row=3, column=3, sticky="wens")
btnIgual.grid(row=3, column=2, sticky="wens")
btnVezes.grid(row=2, column=3, sticky="wens")

app.mainloop()
