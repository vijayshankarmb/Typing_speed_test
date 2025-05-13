import time

_timer_id = None
_start_time = None

def start_timer(root, callback):
    global _start_time, _timer_id
    _start_time = time.time()

    def update():
        elapsed = time.time() - _start_time
        callback(int(elapsed))
        global _timer_id
        _timer_id = root.after(1000, update)

    update()

def stop_timer(root):
    global _timer_id
    if _timer_id:
        root.after_cancel(_timer_id)
        _timer_id = None

def calculate_wpm(typed_text, reference_text, elapsed_seconds):
    words = typed_text.strip().split()
    correct_words = 0
    ref_words = reference_text.strip().split()

    for i in range(min(len(words), len(ref_words))):
        if words[i] == ref_words[i]:
            correct_words += 1

    minutes = elapsed_seconds / 60 if elapsed_seconds > 0 else 1
    wpm = correct_words / minutes
    return round(wpm, 2)

def calculate_accuracy(typed_text, reference_text):
    total_chars = len(reference_text)
    correct_chars = sum(1 for i, c in enumerate(typed_text) if i < total_chars and c == reference_text[i])
    accuracy = (correct_chars / total_chars) * 100 if total_chars > 0 else 0
    return round(accuracy, 2)
