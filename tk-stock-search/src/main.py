import tkinter as tk
from app import StockSearchApp

def main():
    root = tk.Tk()
    app = StockSearchApp(root)
    app.run()

if __name__ == "__main__":
    main()