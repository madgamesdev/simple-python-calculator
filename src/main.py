# Εισαγωγή βιβλιοθήκων που θα χρειαστούμε
import tkinter as tk # Απλή αλλά και αξιόπιστη βιβλιοθήκη για GUI
from tkinter import ttk
from tkinter import messagebox
import re

# Εισαγωγή του κώδικα απ' το σενάριο python με όνομα "shortcuts_window". Είναι στον ίδιο φάκελο με αυτό το σενάριο
import shortcuts_window

# Ορίζουμε τη μεταβλητή με όνομα "main_window" να είναι το παράθυρο Tk μας
main_window = tk.Tk()

# Ορίζουμε τον τίτλο του παραθύρου μας αντί για τον προεπιλεγμένο "Tk"
main_window.title("Simple Python Calculator")

# Αποθηκεύουμε σε μεταβλητές το πλάτος (window_width) και ύψος (window_height) που θα επιθυμούσαμε για το κύριο παράθυρό μας (main_window)
window_width = 400
window_height = 500

# Αποθηκεύουμε το πλάτος και ύψος της κύριας οθόνης
screen_width = main_window.winfo_screenwidth()
screen_height = main_window.winfo_screenheight()

# Υπολογίζουμε το κέντρο σε πλάτος και ύψος της οθόνης, ώστε να τοποθετήσουμε το κύριο παράθυρο (main_window) αλλά και άλλα τυχόν παράθυρα στο κέντρο της οθόνης
# Έτσι δίνουμε μια πιο ομαλή εμπειρία στον χρήστη της εφαρμογής μας
default_window_x_pos = (screen_width // 2) - (window_width // 2)
default_window_y_pos = (screen_height // 2) - (window_height // 2) 

# Όριζουμε εδώ πέρα το πλάτος και ύψος του παραθύρου αλλά και την τοποθεσία στην οθόνη όπου θα πρωτοεμφανιστεί
# Ναι, για κάποιον λόγο τα ορίζουμε όλα αυτά με ένα f-string. Βλέπουμε πως και μία επαγγελματική βιβλιοθήκη μπορεί σε κάποια σημεία να είναι περίεργη
main_window.geometry(f"{window_width}x{window_height}+{default_window_x_pos}+{default_window_y_pos}")

# Το κάνουμε ώστε να μην μπορεί ο χρήστης να αλλάξει το πλάτος ή ύψος της εφαρμογής γιατί είναι μια απλή αριθμομηχανή
main_window.resizable(False, False)

# Η διαδικασία με το DPI Awareness είναι μέσα σε ένα try block γιατί σε άλλες πλατφόρμες όπως τα Linux ή τα MacOS δεν το έχουν αυτό.
try:
    # Φορτώνουμε τη βιβλιοθήκη windll που με λίγα λόγια μας αφήνει να επικοινωνήσουμε με τα Windows
    from ctypes import windll 
    # Ενεργοποιούμε το DPI Awareness για να μην αφήσουμε τα Windows να μεγενθύνουν την εφαρμογή και να φανεί θωλή σε μεγάλες οθόνες.
    windll.shcore.SetProcessDpiAwareness(1)
except:
    # Δεν τρέχει το πρόγραμμα σε Windows; Ας το αφήσουμε αυτό!
    pass

# -------------------------------
# Το μυαλό της εφαρμογής
# -------------------------------

global current_num_decimal
global default_zero

def add_to_display(char):
    global default_zero

    # Παίρνουμε το τρέχον κείμενο από την οθόνη
    current = calc_display.get()

    # Επιτρέπουμε αλλαγές στο πεδίο
    calc_display.config(state="normal")

    # Άμα γράφει "Error" το πεδίο, καθάρισέ το πριν γράψεις κάτι άλλο
    if current == "Error":
        current = ""
        calc_display.delete(0, tk.END)
    # Άμα η οθόνη είναι άδεια ή έχει το default 0
    elif current == "" or current == "0":
        # Αν θέλουμε να βάλουμε αριθμό, αντικαθιστούμε το 0 με αυτόν
        if char.isdigit():
            calc_display.delete(0, tk.END)
            calc_display.insert(tk.END, char)
            default_zero = False
        # Αν πατηθεί τελεία, βάζουμε "0."
        elif char == ".":
            calc_display.delete(0, tk.END)
            calc_display.insert(tk.END, "0.")
            default_zero = False
    # Αν ο χαρακτήρας που θέλουμε να βάλουμε είναι τελεία
    elif char == ".":
        # Σπάμε την πράξη σε κομμάτια βάση τους τελεστές
        last_number = re.split(r"[+\-*/]", current)[-1]

        # Αν υπάρχει ήδη τελεία σε αυτόν τον αριθμό, δε βάζουμε άλλη
        if "." not in last_number:
            calc_display.insert(tk.END, char)
    # Κουμπί ίσον
    elif char == "=":
        calculate(current)
    # Κανονοική εισαγωγή του χαρακτήρα
    else:
        calc_display.insert(tk.END, char)
        default_zero = False

    # Κάνουμε read-only το πεδίο
    calc_display.config(state="readonly")

# Function για τον υπολογισμό μιας πράξης 
def calculate(calculation_to_do):
    try:
        # Το eval θα υπολογίσει την πράξη στη μεταβλητή με όνομα "calculation_to_do"
        # Έχει βάλει το function "eval" μέσα στο function με όνομα "str" που σημαίνει string,
        # έτσι θα μετατρέψουμε το αποτέλεσμα της πράξης σε string
        result = (str(eval(calculation_to_do)))

        # Εκκαθάριση του πεδίου που προβάλλει την πράξη και το αποτέλεσμά της πριν προσθέσουμε το αποτέλεσμα
        calc_display.delete(0, tk.END)

        # Προσθέτουμε το αποτέλεσμα στο πεδίο
        calc_display.insert(tk.END, result)

    # Άμα κάτι πάει στραβά (π.χ. κάποιος διαιρέσει κάτι με το 0, που το αποτέλεσμα είναι απροσδιόριστο),
    # τότε το πεδίο κώδικα από κάτω θα το καλύψει
    except Exception: 
        calc_display.delete(0, tk.END)
        calc_display.insert(tk.END, "Error") # Τυπώνει "Error" στο πεδίο

# Κώδικας για το κουμπί C. Άμα χρησιμοποιήσουμε αυτό το function μέσα άλλα function όπως το calculate τα χαλάει,
# επειδή κάνει το πεδίο read-only πριν προσθέσουμε νέο περιεχόμενο μέσα του
def clear_display():
    global current_num_decimal
    global default_zero

    calc_display.config(state="normal")

    calc_display.delete(0, tk.END)
    calc_display.insert(tk.END, "0")
    current_num_decimal = False
    default_zero = True

    calc_display.config(state="readonly")

    
# -------------------------------
# Εδώ θα το κάνουμε ώστε να μπορούμε να γράφουμε απ' το πληκτρολόγιο
# -------------------------------
def on_key_press(event):
    key = event.char
    keysym = event.keysym

    if key.isdigit(): # Αν είναι ψηφίο
        add_to_display(key)
    elif keysym == "Return": # Enter
        add_to_display("=")
    elif key.lower() in ["c", "ψ"]: # C
        clear_display()
    elif keysym in ["plus", "KP_Add"]: # +
        add_to_display("+")
    elif keysym in ["minus", "KP_Subtract"]: # -
        add_to_display("-")
    elif keysym in ["asterisk", "KP_Multiply"]: # *
        add_to_display("*")
    elif keysym in ["slash", "KP_Divide"]: # /
        add_to_display("/")
    elif keysym == "BackSpace": # Backspace
        calc_display.config(state="normal")

        new_display_content = calc_display.get()[:-1]

        if (default_zero):
            # Δεν έχει γράψει ο χρήστης τίποτα στην ουσία, οπότε δεν κάνουμε τίποτα
            calc_display.config(state="readonly")
        elif (len(new_display_content) == 1):
            # Αντικατάσταση του περιεχομένου της οθόνης με default 0
            clear_display()
            calc_display.config(state="readonly")
        else: 
            # Εκκαθάρηση της οθόνης
            calc_display.delete(0, tk.END)
            # Και εμφάνιση του περιεχομένου αλλά χωρίς τον τελευταίο χαρακτήρα,
            # γιατί πατήσαμε backspace
            calc_display.insert(0, new_display_content)
            calc_display.config(state="readonly")

# Βάζουμε το παράθυρο να ελέγχει για πατημένα πλήκτρα. Όταν εντοπίσει πως πατήθηκε ένα, τότε τρέχει το on_key_press() function από πάνω
main_window.bind("<Key>", on_key_press)

# -------------------------------
# Ήρθε η ώρα για το GUI!
# -------------------------------

# Πάνω-πάνω μπάρα

# Εδώ φτιάχνουμε την πάνω-πάνω μπάρα με τις επιλογές
menu_bar = tk.Menu(main_window)

# Προσθέτουμε την μπάρα στο παράθυρο ορίζοντας στην ως το μενού του κυρίου παραθύρου
main_window.config(menu=menu_bar)

# Δημιουργούμε και προσθέτουμε τη Help επιλογή στην μπάρα
help_menu = tk.Menu(menu_bar, 
                    tearoff=0, 
                    font=("Arial", 11))
menu_bar.add_cascade(label="Help", menu=help_menu)

help_menu.add_command(
    label="Shortcuts",
    command=lambda: shortcuts_window.open_shortcuts_window()
)

help_menu.add_command(
    label="About",
    command=lambda: tk.messagebox.showinfo(
        "Python Calculator",
        "A beginner-friendly app for the new Python developers to experiment with freely. Make sure to fork this project and enrich it with your own ideas!"
    )
)
# -------------------------------
# Εδώ μπορούμε να ξεκινήσουμε να φτιάχνουμε το GUI της αριθμομηχανής
# -------------------------------

# Φτιάχνουμε το πεδίο πάνω όπου θα προβάλλονται οι αριθμοί που πληκτρολογούνται και το αποτέλεσμα
calc_display = ttk.Entry(main_window, 
                         font=("Arial", 34), 
                         justify="right", 
                         state="readonly")

calc_display.pack(fill="x", padx=10, ipady=16)

# Φτιάχνουμε το "button_frame" το οποίο θα κρατάει τα κουμπιά της αριθμομηχανής
button_frame = tk.Frame(main_window)
button_frame.pack(expand=True, 
                  fill="both", 
                  padx=10, 
                  pady=10)

# Μια λίστα με τη σειρά των κουμπιών και το περιεχόμενό τους
calc_button_template = [
    ["7", "8", "9", "+"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "*"],
    ["=", "0", ".", "/"],
    ["C"]
]


# Ρυθμίζουμε την εμφάνιση των κουμπιών της αριθμομηχανής μας
calc_button_style = ttk.Style()
calc_button_style.configure("CalcButton.TButton", font=("Arial", 20, "bold"))

# Προσθέτουμε τα κουμπιά της αριθμομηχανής στο "button_frame"
# Δύσκολο να εξηγήσω πως δουλεύει. Όπως και να το κάνετε, μια χαρά είναι, αρκεί να δουλεύει
for r, row in enumerate(calc_button_template):
    for c, char in enumerate(row):
        if char == "C":
            button = ttk.Button(button_frame, 
                                text=char, 
                                style="CalcButton.TButton",
                                command=clear_display)
        else:
            button = ttk.Button(button_frame, 
                                text=char, 
                                style="CalcButton.TButton",
                                command=lambda ch=char: add_to_display(ch))
        button.grid(row=r, column=c, sticky="nsew")

# Κάνουμε τα κουμπιά να μη βγαίνουν έξω από το button_frame. Δύσκολο να εξηγηθεί
for i in range(5):
    button_frame.columnconfigure(i, weight=1)

for i in range(5):
    button_frame.rowconfigure(i, weight=1)

# Βάζουμε ένα αρχικό 0 στην οθόνη
clear_display()

# -------------------------------
# Ήρθε η ώρα να δώσουμε ζωή στην εφαρμογή μας
# Το mainloop() ενός παραθύρου Tk κρατάει το παράθυρο ανοιχτό και περιμένει ενέργειες του χρήστη
# -------------------------------
main_window.mainloop()

# -------------------------------
# Πειραματιστείτε ΕΛΕΥΘΕΡΑ με αυτήν την εφαρμογή, μελετήστε την ή και εμπλουτίστε την!
# -------------------------------