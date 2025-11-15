import tkinter as tk
from tkinter import ttk

class SearchBar(tk.Frame):
    def __init__(self, master=None, search_callback=None):
        super().__init__(master)
        self.master = master
        self.search_callback = search_callback
        self.create_widgets()

    def create_widgets(self):
        self.label = ttk.Label(self, text="Enter Stock Ticker:")
        self.label.pack(side=tk.LEFT, padx=(10, 5), pady=10)

        self.entry = ttk.Entry(self)
        self.entry.pack(side=tk.LEFT, padx=(0, 5), pady=10)

        self.search_button = ttk.Button(self, text="Search", command=self.perform_search)
        self.search_button.pack(side=tk.LEFT, padx=(0, 10), pady=10)

    def perform_search(self):
        ticker = self.entry.get().strip()
        if ticker and self.search_callback:
            self.search_callback(ticker)

    def clear(self):
        self.entry.delete(0, tk.END)