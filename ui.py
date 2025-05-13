import tkinter as tk
from tkinter import font
from data import get_random_passage
from logic import start_timer, stop_timer, calculate_wpm, calculate_accuracy

def create_ui(root):
    text_font = font.Font(family="Courier", size=12)

    current_passage = {"text": get_random_passage()}  # shared mutable object

    # Title
    title_label = tk.Label(root, text="Typing Speed Tester", font=("Helvetica", 16, "bold"))
    title_label.pack(pady=10)

    # Passage Display
    passage_display = tk.Text(root, height=5, width=60, font=text_font, wrap="word")
    passage_display.insert(tk.END, current_passage["text"])
    passage_display.config(state="disabled")
    passage_display.pack(pady=10)

    # Typing Input
    input_entry = tk.Entry(root, width=60, font=text_font)
    input_entry.pack(pady=10)

    # Timer Label
    timer_label = tk.Label(root, text="Time: 0s")
    timer_label.pack()

    # Results Label
    results_label = tk.Label(root, text="WPM: ___   Accuracy: ___%")
    results_label.pack(pady=10)

    # Timer state
    elapsed = {"seconds": 0}

    # Helper to load new passage
    def load_new_passage():
        new_text = get_random_passage()
        current_passage["text"] = new_text
        passage_display.config(state="normal")
        passage_display.delete("1.0", tk.END)
        passage_display.insert(tk.END, new_text)
        passage_display.config(state="disabled")

    def update_timer_display(seconds):
        elapsed["seconds"] = seconds
        timer_label.config(text=f"Time: {seconds}s")

    def start_test():
        input_entry.delete(0, tk.END)
        input_entry.config(state="normal")
        input_entry.focus()
        start_button.config(state="disabled")
        results_label.config(text="WPM: ___   Accuracy: ___%")
        timer_label.config(text="Time: 0s")
        elapsed["seconds"] = 0
        start_timer(root, update_timer_display)

    def end_test():
        stop_timer(root)
        typed = input_entry.get()
        wpm = calculate_wpm(typed, current_passage["text"], elapsed["seconds"])
        accuracy = calculate_accuracy(typed, current_passage["text"])
        results_label.config(text=f"WPM: {wpm}   Accuracy: {accuracy}%")
        start_button.config(state="normal")
        load_new_passage()

    def reset_test():
        stop_timer(root)
        input_entry.delete(0, tk.END)
        input_entry.config(state="normal")
        results_label.config(text="WPM: ___   Accuracy: ___%")
        timer_label.config(text="Time: 0s")
        start_button.config(state="normal")
        load_new_passage()

    # Buttons
    buttons_frame = tk.Frame(root)
    buttons_frame.pack(pady=5)

    start_button = tk.Button(buttons_frame, text="Start", command=start_test)
    start_button.pack(side="left", padx=10)

    done_button = tk.Button(buttons_frame, text="Done", command=end_test)
    done_button.pack(side="left", padx=10)

    reset_button = tk.Button(buttons_frame, text="Reset", command=reset_test)
    reset_button.pack(side="left", padx=10)
