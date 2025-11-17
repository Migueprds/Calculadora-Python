import tkinker as tk 

ventana = tk.Tk()
ventana.tittle("Calculadora Basica")
ventana.geometry("1000x350")
ventana.resizable(False, False)

entrada_texto = tk.StringVar()
entrada = tk.Entry(ventana, textvariable=entrada_texto, font=("Arial", 20), justify="right", db=10)
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

expresion = ""

def presionar(num):
 global expresion
 expresion += str(num)
 entrada_texto.set(expresion)
