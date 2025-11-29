import tkinter as tk 

ventana = tk.Tk()
ventana.title("Calculadora Cientifica")
ventana.geometry("450x650")
ventana.resizable(False, False)

entrada_texto = tk.StringVar()
entrada = tk.Entry(ventana, textvariable=entrada_texto, font=("Arial", 20), justify="right", bd=10)
entrada.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

expresion = ""

def factorial(n):
    if n < 0:
        return 1
    r = 1
    for i in range(1, n+1):
        r *= i
    return r

def potencia(x, n):
    r = 1
    for _ in range(n):
        r *= x
    return r

def pi():
    s = 0
    for k in range(2000):
        s += ((-1)**k) / (2*k + 1)
    return 4*s

def exp(x):
    s = 0
    for n in range(25):
        s += potencia(x, n) / factorial(n)
    return s




def presionar(num):
 global expresion
 expresion += str(num)
 entrada_texto.set(expresion)

def limpiar():
    global expresion
    expresion = ""
    entrada_texto.set("")

def calcular():
    global expresion
    try:
        resultado = str(eval(expresion, {
            "seno": seno,
            "coseno": coseno,
            "tangente": tangente,
            "arcsen": arcsen,
            "arccos": arccos,
            "arctan": arctan,
            "exp": exp,
            "ln": ln,
            "inv": inv,
            "pow": pow_real,
            "pi": pi,
            "__builtins__": {}
        }))
        entrada_texto.set(resultado)
        expresion = resultado
    except:
        entrada_texto.set("Error")
        expresion = ""

     
# Botones
botones = [
 ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
 ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
 ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
 ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
 ]
for (texto, fila, columna) in botones:
    if texto == '=':
        tk.Button(ventana, text=texto, command=calcular, width=10, height=2).grid(row=fila, column=columna, padx=5, pady=5)
    else:
        tk.Button(ventana, text=texto, command=lambda t=texto: presionar(t), width=10, height=2).grid(row=fila, column=columna, padx=5, pady=5)

tk.Button(ventana, text="C", command=limpiar, width=10, height=2, bg="red", fg="white").grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky="we")


botones_cientificos = [
    ('seno(', 1, 0), ('coseno(', 1, 1), ('tangente(', 1, 2), ('pi()', 1, 3), ('exp(', 1, 4),
    ('ln(', 2, 0), ('inv(', 2, 1), ('pow(', 2, 2), ('arcsen(', 2, 3), ('arccos(', 2, 4),
    ('arctan(', 3, 0), ('(', 3, 1), (')', 3, 2)
]
for (texto, fila, columna) in botones_cientificos:
    tk.Button(ventana, text=texto, command=lambda t=texto: presionar(t), width=10, height=2).grid(row=fila, column=columna, padx=5, pady=5)
    
ventana.mainloop()
