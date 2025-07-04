import tkinter as tk

def length_cn_to_inches():
    try:
        inches = float(entry.get())
        
        centimeters  = inches * 2.54 # 1 inch is equal to 2.54
        
        result_lbl.config(text=f"{inches} inches is {centimeters:.2f} centimeters")
    except ValueError:
        result_lbl.config(text="please input valid number")
    

window = tk.Tk()
window.geometry("400x400")
window.title("Length converter app")
window.configure(bg="grey")

label = tk.Label(window, text="Enter length in inches",bg = "yellow",fg = "Red",font=("Times New Roman", 16, "bold") )
label.pack(pady=5)

entry = tk.Entry(window,font=("Times New Roman", 16, "bold"))
entry.pack(pady=5)

cn_button = tk.Button(window, text="convert",command = length_cn_to_inches,font=("Times New Roman", 16, "bold"),relief=tk.RIDGE)
cn_button.pack(pady=5)

result_lbl = tk.Label(window,text="",font=("Times New Roman", 16, "bold"))
result_lbl.pack(pady=5)

window.mainloop()