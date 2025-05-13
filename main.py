import tkinter as tk
from ui import create_ui

def main():
    root = tk.Tk()
    root.title("Typing Speed Tester")
    create_ui(root)
    root.mainloop()

if __name__ == "__main__":
    main()
