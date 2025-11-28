import tkinter as tk 

ventana = tk.Tk()
ventana.title("Calculadora Cientifica")
ventana.geometry("450x650")
ventana.resizable(False, False)

entrada_texto = tk.StringVar()
entrada = tk.Entry(ventana, textvariable=entrada_texto, font=("Arial", 20), justify="right", bd=10)
entrada.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

expresion = ""

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
        resultado = str(eval(expresion))
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

ventana.mainloop()
