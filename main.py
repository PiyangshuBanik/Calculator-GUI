import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        
        self.current_input = tk.StringVar()
        
        self.create_ui()
        
    def create_ui(self):
        input_frame = tk.Frame(self.root)
        input_frame.pack(padx=1, pady=1)
        
        entry = tk.Entry(input_frame, textvariable=self.current_input, font=("Arial", 18), bd=10, insertwidth=4, width=20, justify="right")
        entry.grid(row=0, column=0)
        
        button_frame = tk.Frame(self.root)
        button_frame.pack(padx=1, pady=1)
        
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
        ]
        
        for (text, row, col) in buttons:
            button = tk.Button(button_frame, text=text, font=("Arial", 16), height=2, width=5, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=6, pady=6)
        
    def on_button_click(self, value):
        if value == "=":
            try:
                result = eval(self.current_input.get())
                self.current_input.set(result)
            except Exception as e:
                self.current_input.set("Error")
        else:
            current_text = self.current_input.get()
            new_text = current_text + value
            self.current_input.set(new_text)
        
def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

