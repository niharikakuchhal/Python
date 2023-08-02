import tkinter as tk
from tkinter import font

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.geometry("400x500")
        master.configure(bg='#333333')

        # Create the entry widget to display the current value
        entry_font = font.Font(size=30, weight='bold')
        self.entry = tk.Entry(master, width=18, font=entry_font, justify='right', borderwidth=5, bg='#444444', fg='white')
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Create the buttons for the calculator
        button_list = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '.', '0', '=', '+',
            'C'
        ]
        button_font = font.Font(size=20, weight='bold')
        self.buttons = []
        for i in range(len(button_list)):
            if button_list[i] == 'C':
                self.buttons.append(tk.Button(master, text=button_list[i], width=4, height=2, font=button_font, bg='#ff6666', fg='white', bd=0, command=lambda x=button_list[i]: self.click(x)))
            else:
                self.buttons.append(tk.Button(master, text=button_list[i], width=4, height=2, font=button_font, bg='#666666', fg='white', bd=0, command=lambda x=button_list[i]: self.click(x)))
            self.buttons[i].grid(row=i // 4 + 1, column=i % 4, padx=5, pady=5, sticky="nsew")
            self.buttons[i].bind('<Enter>', self.on_enter)
            self.buttons[i].bind('<Leave>', self.on_leave)

    def click(self, key):
        # Handle the button clicks
        if key == '=':
            # Calculate the result
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, 'Error')
        elif key == 'C':
            # Clear the entry widget
            self.entry.delete(0, tk.END)
        else:
            # Add the key to the end of the current entry
            self.entry.insert(tk.END, key)

    def on_enter(self, event):
        # Change the button color on hover
        event.widget.config(bg='#999999')

    def on_leave(self, event):
        # Change the button color back to normal
        event.widget.config(bg='#666666')

# Create the main window and run the application
root = tk.Tk()
app = Calculator(root)
root.mainloop()
