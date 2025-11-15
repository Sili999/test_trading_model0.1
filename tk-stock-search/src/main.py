import tkinter as tk
from app import App

def main():
    root = tk.Tk()
    root.title("Stock Search Application")
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()