import tkinter as tk
from tkinter import ttk
from ui.main_window import MainWindow

class StockSearchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stock Search Application")
        self.root.geometry("800x600")
        
        self.main_window = MainWindow(self.root)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = StockSearchApp(root)
    app.run()