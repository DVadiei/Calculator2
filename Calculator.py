import tkinter as tk

from math import sqrt 
try:    
    def on_click(event):
        text = event.widget.cget("text")
        
        if text == "=":
            try:
                result = eval(entry.get())
                entry.delete(0, tk.END)
                entry.insert(tk.END, str(result))
            except:
                entry.delete(0, tk.END)
                entry.insert(tk.END, "Error")      
        elif text == "%":
            entry.insert(tk.END, "/100")
        elif text == "C":
            entry.delete(0, tk.END)
        elif text == "DEL":
            entry.delete(len(entry.get())-1)
        
        else:
            entry.insert(tk.END, text)
    
    def on_radical():
        entry.insert(tk.END, "**0.5")
    def on_power():
        entry.insert(tk.END, "**")
    def paranthesis1():
        entry.insert(tk.END, "(")    
    def paranthesis2():
        entry.insert(tk.END, ")")  
    
    root = tk.Tk()
    root.title("Calculator")
    root.configure(bg='lightgray')
    
    entry = tk.Entry(root, width=30, borderwidth=5)
    entry.grid(row=0, column=0, columnspan=5)
    entry.configure(bg='white', fg='black')
    
    buttons = [
        "DEL","C", "%", "/",
        "1", "2" , "3" , "*",
        "4", "5" , "6" , "-",
        "7", "8" , "9" , "+",
        ".", "0" ,   "="
    ]
    
    colors = [ 'gray'  ,   'gray' ,  'gray'  , 'gray' ,
              'lightpink', 'lightpink', 'lightpink', 'gray',
              'lightpink', 'lightpink', 'lightpink', 'gray',
              'lightpink', 'lightpink', 'lightpink', 'gray',
              'gray', 'lightpink', 'orange']
    
    for i in range(len(buttons)):
        btn = tk.Button(root, text=buttons[i], padx=20, pady=10)    
    
        if buttons[i] == "=":
            btn.config(width=20)
            btn.grid(row=  5, column= 2 , columnspan= 2 )
        else: 
            btn.config(width= 5)
            btn.grid(row=i //4 + 1, column= i % 4 , sticky="ew")
        btn.configure(bg=colors[i])
        btn.bind("<Button-1>", on_click)
    
    menu = tk.Menu(root)
    root.config(menu=menu)
    
    operators_menu = tk.Menu(menu)
    menu.add_cascade(label="Other Operators", menu=operators_menu)
    operators_menu.add_command(label="Radical (√)", command=on_radical)
    operators_menu.add_command(label="Power (x^y)", command=on_power)
    operators_menu.add_command(label="(", command=paranthesis1)
    operators_menu.add_command(label=")", command=paranthesis2)

    root.mainloop()
except:
    print("Error!")