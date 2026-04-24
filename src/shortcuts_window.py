import tkinter as tk
from tkinter import ttk

def open_shortcuts_window():
    # Ορίζουμε τη μεταβλητή με όνομα "main_window" να είναι το παράθυρο Tk μας
    shortcuts_window = tk.Tk()

    # Ορίζουμε τον τίτλο του παραθύρου μας αντί για τον προεπιλεγμένο "Tk"
    shortcuts_window.title("Keyboard Shortcuts")

    # Αποθηκεύουμε σε μεταβλητές το πλάτος (window_width) και ύψος (window_height) που θα επιθυμούσαμε για το κύριο παράθυρό μας (main_window)
    window_width = 350
    window_height = 300

    # Αποθηκεύουμε το πλάτος και ύψος της κύριας οθόνης
    screen_width = shortcuts_window.winfo_screenwidth()
    screen_height = shortcuts_window.winfo_screenheight()

    # Υπολογίζουμε το κέντρο σε πλάτος και ύψος της οθόνης, ώστε να τοποθετήσουμε το κύριο παράθυρο (main_window) αλλά και άλλα τυχόν παράθυρα στο κέντρο της οθόνης
    # Έτσι δίνουμε μια πιο ομαλή εμπειρία στον χρήστη της εφαρμογής μας
    default_window_x_pos = (screen_width // 2) - (window_width // 2)
    default_window_y_pos = (screen_height // 2) - (window_height // 2) 

    # Όριζουμε εδώ πέρα το πλάτος και ύψος του παραθύρου αλλά και την τοποθεσία στην οθόνη όπου θα πρωτοεμφανιστεί
    # Ναι, για κάποιον λόγο τα ορίζουμε όλα αυτά με ένα f-string. Βλέπουμε πως και μία επαγγελματική βιβλιοθήκη μπορεί σε κάποια σημεία να είναι περίεργη
    shortcuts_window.geometry(f"{window_width}x{window_height}+{default_window_x_pos}+{default_window_y_pos}")

    # Το κάνουμε ώστε να μην μπορεί ο χρήστης να αλλάξει το πλάτος ή ύψος της εφαρμογής γιατί είναι μια απλή αριθμομηχανή
    shortcuts_window.resizable(False, False)

    title = ttk.Label(
        shortcuts_window,
        text="Keyboard Shortcuts",
        font=("Arial", 14, "bold")
    )
    title.pack(pady=10)

    shortcuts = [
        ("0–9", "Enter numbers"),
        ("+  -  *  /", "Operations"),
        ("Enter", "Calculate"),
        ("Backspace", "Delete last character"),
        ("C", "Clear display")
    ]

    for key, desc in shortcuts:
        ttk.Label(
            shortcuts_window,
            text=f"{key} - {desc}",
            font=("Arial", 11)
        ).pack(anchor="w", padx=20, pady=4)