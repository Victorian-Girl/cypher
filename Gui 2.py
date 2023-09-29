from tkinter import *
import tkinter
from tkinter import filedialog
from decoding_text import de_coding
from text_coding import coding
from code2 import code_2
from uncode2 import un_code2
import sys

sys.modules["subprocess"] = None


global selected


def decoding():
    uncode_window = tkinter.Toplevel(app)
    uncode_window.title("Décrytage de code")
    uncode_window.geometry("640x525+750+250")
    uncode_window.minsize(640, 525)
    uncode_window.config(background="#4065A4")
    label = tkinter.Label(uncode_window, text="Votre texte codé ici.", background="#4065A4", font=("Courrier", 20),
                          fg="white")
    lb = tkinter.Label(uncode_window, background="#4065A4")
    # create our scrollbar for the test box
    text_scroll = Scrollbar(lb)
    text_scroll.pack(side=RIGHT, fill=Y)
    # Horizontal Scrollbar
    hor_scroll = Scrollbar(lb, orient="horizontal")
    hor_scroll.pack(side=BOTTOM, fill=X)
    entry_text = tkinter.Text(lb, width=60, height=10, undo=True, wrap="none",
                              yscrollcommand=text_scroll.set, xscrollcommand=hor_scroll.set)
    text_scroll.config(command=entry_text.yview)
    hor_scroll.config(command=entry_text.xview)
    lb2 = tkinter.Label(uncode_window, background="#4065A4")
    # create our scrollbar for the test box
    text_scroll = Scrollbar(lb2)
    text_scroll.pack(side=RIGHT, fill=Y)
    # Horizontal Scrollbar
    hor_scroll = Scrollbar(lb2, orient="horizontal")
    hor_scroll.pack(side=BOTTOM, fill=X)
    output_text = tkinter.Text(lb2, width=60, height=10, undo=True, wrap="none",
                               yscrollcommand=text_scroll.set, xscrollcommand=hor_scroll.set)
    text_scroll.config(command=output_text.yview)
    hor_scroll.config(command=output_text.xview)

    def summit():
        # Open the file
        global selected
        uncode = de_coding(str(entry_text.get(1.0, END))).lower()
        entry_text.delete("1.0", END)
        output_text.insert(END, uncode)

    global selected
    selected = False

    def clear_text():
        global selected
        output_text.delete("1.0", END)

    # create new file function
    def new_file():
        # Delete previous text-
        entry_text.delete("1.0", END)
        global selected
        selected = False

    def open_text():
        global selected
        # Delete previous text-
        entry_text.delete("1.0", END)

        # Grab filename-
        text_file = filedialog.askopenfilename(initialdir="C:/", title="Open File", filetypes=(("All files", "*.*"),
                                               ("Text Files", "*.txt"), ("Python File", "*.py"), ("Word File", "*.doc"),
                                               ("Word File", "*.docx"), ("Html File", "*.html"),
                                               ("Libre Office File", "*.odt"),))
        # Check to see if there is a file name
        if text_file:
            # make filename global so we can access it later
            global selected
            selected = text_file

        # Open the file
        text_file = open(text_file, "r")
        stuff = text_file.read()
        # Add file to textbox
        entry_text.insert(END, stuff)
        # Close the opened file
        text_file.close()

    # cut text
    def cut_text(e):
        global selected
        # check to see if we used keyboard shortcuts
        if e:
            selected = entry_text.clipboard_get()
        else:
            if entry_text.selection_get():
                # grab selectext from text box
                selected = entry_text.selection_get()
                # delete selected text from text box
                entry_text.delete("sel.first", "sel.last")
                # Clear the clipboard then append
                entry_text.clipboard_clear()
                entry_text.clipboard_append(selected)

    # copy text
    def copy_text(e):
        global selected
        # check to see if we used keyboard shortcuts
        if e:
            selected = entry_text.clipboard_get()
        if entry_text.selection_get():
            # grab selectext from text box
            selected = entry_text.selection_get()
            # Clear the clipboard then append
            entry_text.clipboard_clear()
            entry_text.clipboard_append(selected)

    # paste text
    def paste_text(e):
        global selected
        # check to see if we used keyboard shortcuts
        if e:
            selected = entry_text.clipboard_get()
        else:
            if selected:
                position = entry_text.index(INSERT)
                entry_text.insert(position, selected)

    def save_as_file():
        text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="C:/", title="Enregistrer sous",
                                                 filetypes=(("All files", "*.*"),
                                                            ("Text Files", "*.txt"), ("Python File", "*.py"),
                                                            ("Word File", "*.doc"), ("Word File", "*.docx"),
                                                            ("Html File", "*.html"), ("Libre Office File", "*.odt"),))
        # Save the file
        text_file = open(text_file, "w")
        text_file.write(output_text.get(1.0, END))
        # CLose the file
        text_file.close()

    uncode_window_button = tkinter.Button(uncode_window, text="Décrypter", width=10, height=1, command=summit)
    uncode_window_button_clear = tkinter.Button(uncode_window, text="Effacer", width=10, height=1,
                                                command=clear_text)

    label.pack(pady=10)
    lb.pack(pady=5)
    entry_text.pack()
    uncode_window_button.pack(pady=5)
    lb2.pack(pady=5)
    output_text.pack()
    uncode_window_button_clear.pack(pady=5)

    secondmenu = tkinter.Menu(uncode_window)

    files_menu3 = tkinter.Menu(secondmenu, tearoff=0)
    files_menu3.add_command(label="Nouveau", command=new_file)
    files_menu3.add_command(label="Ouvrir", command=open_text)
    files_menu3.add_separator()
    files_menu3.add_command(label="Enregister sous", command=save_as_file)
    files_menu3.add_separator()
    files_menu3.add_command(label="Quitter", activebackground="red", command=uncode_window.destroy)

    edition_menu3 = tkinter.Menu(secondmenu, tearoff=0)
    edition_menu3.add_command(label="Copie", command=lambda: copy_text(False), accelerator="(Ctrl+c)")
    edition_menu3.add_command(label="Coller", command=lambda: paste_text(False), accelerator="(Ctrl+v)")
    edition_menu3.add_command(label="Couper", command=lambda: cut_text(False), accelerator="(Ctrl+x)")
    edition_menu3.add_separator()
    edition_menu3.add_command(label="Undo", command=entry_text.edit_undo, accelerator="(Ctrl+z)")
    edition_menu3.add_command(label="Redo", command=entry_text.edit_redo, accelerator="(Ctrl+y)")

    entry_text.bind("<Control-Key-x>", cut_text)
    entry_text.bind("<Control-Key-c>", copy_text)
    entry_text.bind("<Control-Key-v>", paste_text)

    secondmenu.add_cascade(label="Fichier", menu=files_menu3)
    secondmenu.add_cascade(label="Edition", menu=edition_menu3)

    uncode_window.config(menu=secondmenu)


def wrote_code():
    text_writting = tkinter.Toplevel(app)
    text_writting.title("Encryptage du texte")
    text_writting.geometry("640x525+650+350")
    text_writting.minsize(640, 525)
    text_writting.config(background="#4065A4")
    label = Label(text_writting, text="Votre texte ici.", background="#4065A4", font=("Courrier", 20), fg="white")
    lb = tkinter.Label(text_writting, background="#4065A4")
    # create our scrollbar for the test box
    text_scroll = Scrollbar(lb)
    text_scroll.pack(side=RIGHT, fill=Y)
    # Horizontal Scrollbar
    hor_scroll = Scrollbar(lb, orient="horizontal")
    hor_scroll.pack(side=BOTTOM, fill=X)
    entry_text1 = tkinter.Text(lb, width=60, height=10, undo=True, wrap="none",
                               yscrollcommand=text_scroll.set, xscrollcommand=hor_scroll.set)
    text_scroll.config(command=entry_text1.yview)
    hor_scroll.config(command=entry_text1.xview)
    lb2 = tkinter.Label(text_writting, background="#4065A4")
    # create our scrollbar for the test box
    text_scroll = Scrollbar(lb2)
    text_scroll.pack(side=RIGHT, fill=Y)
    # Horizontal Scrollbar
    hor_scroll = Scrollbar(lb2, orient="horizontal")
    hor_scroll.pack(side=BOTTOM, fill=X)
    output_text = tkinter.Text(lb2, width=60, height=10, undo=True, wrap="none",
                               yscrollcommand=text_scroll.set, xscrollcommand=hor_scroll.set)
    text_scroll.config(command=output_text.yview)
    hor_scroll.config(command=output_text.xview)

    def summit1():
        # Open the file
        global selected
        code = coding(str(entry_text1.get(1.0, END)))
        entry_text1.delete("1.0", END)
        output_text.insert(END, code)

    global selected
    selected = False

    def clear_text():
        global selected
        output_text.delete("1.0", END)

    # create new file function
    def new_file():
        # Delete previous text-
        entry_text1.delete("1.0", END)
        global selected
        selected = False

    def open_text():
        global selected
        # Delete previous text-
        entry_text1.delete("1.0", END)

        # Grab filename-
        text_file = filedialog.askopenfilename(initialdir="C:/", title="Open File", filetypes=(("All files", "*.*"),
                                               ("Text Files", "*.txt"), ("Python File", "*.py"), ("Word File", "*.doc"),
                                               ("Word File", "*.docx"), ("Html File", "*.html"),
                                               ("Libre Office File", "*.odt"),))
        # Check to see if there is a file name
        if text_file:
            # make filename global so we can access it later
            global selected
            selected = text_file

        # Open the file
        text_file = open(text_file, "r")
        stuff = text_file.read()
        # Add file to textbox
        entry_text1.insert(END, stuff)
        # Close the opened file
        text_file.close()

    # cut text
    def cut_text(e):
        global selected
        # check to see if we used keyboard shortcuts
        if e:
            selected = entry_text1.clipboard_get()
        else:
            if entry_text1.selection_get():
                # grab selectext from text box
                selected = entry_text1.selection_get()
                # delete selected text from text box
                entry_text1.delete("sel.first", "sel.last")
                # Clear the clipboard then append
                entry_text1.clipboard_clear()
                entry_text1.clipboard_append(selected)

    # copy text
    def copy_text(e):
        global selected
        # check to see if we used keyboard shortcuts
        if e:
            selected = entry_text1.clipboard_get()
        if entry_text1.selection_get():
            # grab selectext from text box
            selected = entry_text1.selection_get()
            # Clear the clipboard then append
            entry_text1.clipboard_clear()
            entry_text1.clipboard_append(selected)

    # paste text
    def paste_text(e):
        global selected
        # check to see if we used keyboard shortcuts
        if e:
            selected = entry_text1.clipboard_get()
        else:
            if selected:
                position = entry_text1.index(INSERT)
                entry_text1.insert(position, selected)

    def save_as_file():
        text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="C:/", title="Enregistrer sous",
                                                 filetypes=(("All files", "*.*"),
                                                            ("Text Files", "*.txt"), ("Python File", "*.py"),
                                                            ("Word File", "*.doc"), ("Word File", "*.docx"),
                                                            ("Html File", "*.html"), ("Libre Office File", "*.odt"),))
        # Save the file
        text_file = open(text_file, "w")
        text_file.write(output_text.get(1.0, END))
        # CLose the file
        text_file.close()

    text_writting_button = tkinter.Button(text_writting, text="Crypter", width=10, height=1, command=summit1)
    text_writting_button_clear = tkinter.Button(text_writting, text="Effacer", width=10, height=1,
                                                command=clear_text)

    label.pack(pady=10)
    lb.pack(pady=5)
    entry_text1.pack()
    text_writting_button.pack(pady=5)
    lb2.pack(pady=5)
    output_text.pack()
    text_writting_button_clear.pack(pady=5)

    thirddmenu = tkinter.Menu(text_writting)

    files_menu3 = tkinter.Menu(thirddmenu, tearoff=0)
    files_menu3.add_command(label="Nouveau", command=new_file)
    files_menu3.add_command(label="Ouvrir", command=open_text)
    files_menu3.add_separator()
    files_menu3.add_command(label="Enregister sous", command=save_as_file)
    files_menu3.add_separator()
    files_menu3.add_command(label="Quitter", activebackground="red", command=text_writting.destroy)

    edition_menu3 = tkinter.Menu(thirddmenu, tearoff=0)
    edition_menu3.add_command(label="Copie", command=lambda: copy_text(False), accelerator="(Ctrl+c)")
    edition_menu3.add_command(label="Coller", command=lambda: paste_text(False), accelerator="(Ctrl+v)")
    edition_menu3.add_command(label="Couper", command=lambda: cut_text(False), accelerator="(Ctrl+x)")
    edition_menu3.add_separator()
    edition_menu3.add_command(label="Undo", command=entry_text1.edit_undo, accelerator="(Ctrl+z)")
    edition_menu3.add_command(label="Redo", command=entry_text1.edit_redo, accelerator="(Ctrl+y)")

    entry_text1.bind("<Control-Key-x>", cut_text)
    entry_text1.bind("<Control-Key-c>", copy_text)
    entry_text1.bind("<Control-Key-v>", paste_text)

    thirddmenu.add_cascade(label="Fichier", menu=files_menu3)
    thirddmenu.add_cascade(label="Edition", menu=edition_menu3)

    text_writting.config(menu=thirddmenu)


def decoding2():
    uncode_window = tkinter.Toplevel(app)
    uncode_window.title("Décrytage de code")
    uncode_window.geometry("640x525+750+250")
    uncode_window.minsize(640, 525)
    uncode_window.config(background="#4065A4")
    label = tkinter.Label(uncode_window, text="Votre texte codé ici.", background="#4065A4", font=("Courrier", 20),
                          fg="white")
    lb = tkinter.Label(uncode_window, background="#4065A4")
    # create our scrollbar for the test box
    text_scroll = Scrollbar(lb)
    text_scroll.pack(side=RIGHT, fill=Y)
    # Horizontal Scrollbar
    hor_scroll = Scrollbar(lb, orient="horizontal")
    hor_scroll.pack(side=BOTTOM, fill=X)
    entry_text = tkinter.Text(lb, width=60, height=10, undo=True, wrap="none",
                              yscrollcommand=text_scroll.set, xscrollcommand=hor_scroll.set)
    text_scroll.config(command=entry_text.yview)
    hor_scroll.config(command=entry_text.xview)
    lb2 = tkinter.Label(uncode_window, background="#4065A4")
    # create our scrollbar for the test box
    text_scroll = Scrollbar(lb2)
    text_scroll.pack(side=RIGHT, fill=Y)
    # Horizontal Scrollbar
    hor_scroll = Scrollbar(lb2, orient="horizontal")
    hor_scroll.pack(side=BOTTOM, fill=X)
    output_text = tkinter.Text(lb2, width=60, height=10, undo=True, wrap="none",
                               yscrollcommand=text_scroll.set, xscrollcommand=hor_scroll.set)
    text_scroll.config(command=output_text.yview)
    hor_scroll.config(command=output_text.xview)

    def summit():
        # Open the file
        global selected
        uncode = un_code2(str(entry_text.get(1.0, END))).lower()
        entry_text.delete("1.0", END)
        output_text.insert(END, uncode)

    global selected
    selected = False

    def clear_text():
        global selected
        output_text.delete("1.0", END)

    # create new file function
    def new_file():
        # Delete previous text-
        entry_text.delete("1.0", END)
        global selected
        selected = False

    def open_text():
        global selected
        # Delete previous text-
        entry_text.delete("1.0", END)

        # Grab filename-
        text_file = filedialog.askopenfilename(initialdir="C:/", title="Open File", filetypes=(("All files", "*.*"),
                                               ("Text Files", "*.txt"), ("Python File", "*.py"), ("Word File", "*.doc"),
                                               ("Word File", "*.docx"), ("Html File", "*.html"),
                                               ("Libre Office File", "*.odt"),))
        # Check to see if there is a file name
        if text_file:
            # make filename global so we can access it later
            global selected
            selected = text_file

        # Open the file
        text_file = open(text_file, "r")
        stuff = text_file.read()
        # Add file to textbox
        entry_text.insert(END, stuff)
        # Close the opened file
        text_file.close()

    # cut text
    def cut_text(e):
        global selected
        # check to see if we used keyboard shortcuts
        if e:
            selected = entry_text.clipboard_get()
        else:
            if entry_text.selection_get():
                # grab selectext from text box
                selected = entry_text.selection_get()
                # delete selected text from text box
                entry_text.delete("sel.first", "sel.last")
                # Clear the clipboard then append
                entry_text.clipboard_clear()
                entry_text.clipboard_append(selected)

    # copy text
    def copy_text(e):
        global selected
        # check to see if we used keyboard shortcuts
        if e:
            selected = entry_text.clipboard_get()
        if entry_text.selection_get():
            # grab selectext from text box
            selected = entry_text.selection_get()
            # Clear the clipboard then append
            entry_text.clipboard_clear()
            entry_text.clipboard_append(selected)

    # paste text
    def paste_text(e):
        global selected
        # check to see if we used keyboard shortcuts
        if e:
            selected = entry_text.clipboard_get()
        else:
            if selected:
                position = entry_text.index(INSERT)
                entry_text.insert(position, selected)

    def save_as_file():
        text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="C:/", title="Enregistrer sous",
                                                 filetypes=(("All files", "*.*"),
                                                            ("Text Files", "*.txt"), ("Python File", "*.py"),
                                                            ("Word File", "*.doc"), ("Word File", "*.docx"),
                                                            ("Html File", "*.html"), ("Libre Office File", "*.odt"),))
        # Save the file
        text_file = open(text_file, "w")
        text_file.write(output_text.get(1.0, END))
        # CLose the file
        text_file.close()

    uncode_window_button = tkinter.Button(uncode_window, text="Décrypter", width=10, height=1, command=summit)
    uncode_window_button_clear = tkinter.Button(uncode_window, text="Effacer", width=10, height=1,
                                                command=clear_text)

    label.pack(pady=10)
    lb.pack(pady=5)
    entry_text.pack()
    uncode_window_button.pack(pady=5)
    lb2.pack(pady=5)
    output_text.pack()
    uncode_window_button_clear.pack(pady=5)

    secondmenu = tkinter.Menu(uncode_window)

    files_menu3 = tkinter.Menu(secondmenu, tearoff=0)
    files_menu3.add_command(label="Nouveau", command=new_file)
    files_menu3.add_command(label="Ouvrir", command=open_text)
    files_menu3.add_separator()
    files_menu3.add_command(label="Enregister sous", command=save_as_file)
    files_menu3.add_separator()
    files_menu3.add_command(label="Quitter", activebackground="red", command=uncode_window.destroy)

    edition_menu3 = tkinter.Menu(secondmenu, tearoff=0)
    edition_menu3.add_command(label="Copie", command=lambda: copy_text(False), accelerator="(Ctrl+c)")
    edition_menu3.add_command(label="Coller", command=lambda: paste_text(False), accelerator="(Ctrl+v)")
    edition_menu3.add_command(label="Couper", command=lambda: cut_text(False), accelerator="(Ctrl+x)")
    edition_menu3.add_separator()
    edition_menu3.add_command(label="Undo", command=entry_text.edit_undo, accelerator="(Ctrl+z)")
    edition_menu3.add_command(label="Redo", command=entry_text.edit_redo, accelerator="(Ctrl+y)")

    entry_text.bind("<Control-Key-x>", cut_text)
    entry_text.bind("<Control-Key-c>", copy_text)
    entry_text.bind("<Control-Key-v>", paste_text)

    secondmenu.add_cascade(label="Fichier", menu=files_menu3)
    secondmenu.add_cascade(label="Edition", menu=edition_menu3)

    uncode_window.config(menu=secondmenu)


def wrote_code2():
    text_writting = tkinter.Toplevel(app)
    text_writting.title("Encryptage du texte")
    text_writting.geometry("640x525+650+350")
    text_writting.minsize(640, 525)
    text_writting.config(background="#4065A4")
    label = Label(text_writting, text="Votre texte ici.", background="#4065A4", font=("Courrier", 20), fg="white")
    lb = tkinter.Label(text_writting, background="#4065A4")
    # create our scrollbar for the test box
    text_scroll = Scrollbar(lb)
    text_scroll.pack(side=RIGHT, fill=Y)
    # Horizontal Scrollbar
    hor_scroll = Scrollbar(lb, orient="horizontal")
    hor_scroll.pack(side=BOTTOM, fill=X)
    entry_text1 = tkinter.Text(lb, width=60, height=10, undo=True, wrap="none",
                               yscrollcommand=text_scroll.set, xscrollcommand=hor_scroll.set)
    text_scroll.config(command=entry_text1.yview)
    hor_scroll.config(command=entry_text1.xview)
    lb2 = tkinter.Label(text_writting, background="#4065A4")
    # create our scrollbar for the test box
    text_scroll = Scrollbar(lb2)
    text_scroll.pack(side=RIGHT, fill=Y)
    # Horizontal Scrollbar
    hor_scroll = Scrollbar(lb2, orient="horizontal")
    hor_scroll.pack(side=BOTTOM, fill=X)
    output_text = tkinter.Text(lb2, width=60, height=10, undo=True, wrap="none",
                               yscrollcommand=text_scroll.set, xscrollcommand=hor_scroll.set)
    text_scroll.config(command=output_text.yview)
    hor_scroll.config(command=output_text.xview)

    def summit1():
        # Open the file
        global selected
        code = code_2(str(entry_text1.get(1.0, END)))
        entry_text1.delete("1.0", END)
        output_text.insert(END, code)

    global selected
    selected = False

    def clear_text():
        global selected
        output_text.delete("1.0", END)

    # create new file function
    def new_file():
        # Delete previous text-
        entry_text1.delete("1.0", END)
        global selected
        selected = False

    def open_text():
        global selected
        # Delete previous text-
        entry_text1.delete("1.0", END)

        # Grab filename-
        text_file = filedialog.askopenfilename(initialdir="C:/", title="Open File", filetypes=(("All files", "*.*"),
                                               ("Text Files", "*.txt"), ("Python File", "*.py"), ("Word File", "*.doc"),
                                               ("Word File", "*.docx"), ("Html File", "*.html"),
                                               ("Libre Office File", "*.odt"),))
        # Check to see if there is a file name
        if text_file:
            # make filename global so we can access it later
            global selected
            selected = text_file

        # Open the file
        text_file = open(text_file, "r")
        stuff = text_file.read()
        # Add file to textbox
        entry_text1.insert(END, stuff)
        # Close the opened file
        text_file.close()

    # cut text
    def cut_text(e):
        global selected
        # check to see if we used keyboard shortcuts
        if e:
            selected = entry_text1.clipboard_get()
        else:
            if entry_text1.selection_get():
                # grab selectext from text box
                selected = entry_text1.selection_get()
                # delete selected text from text box
                entry_text1.delete("sel.first", "sel.last")
                # Clear the clipboard then append
                entry_text1.clipboard_clear()
                entry_text1.clipboard_append(selected)

    # copy text
    def copy_text(e):
        global selected
        # check to see if we used keyboard shortcuts
        if e:
            selected = entry_text1.clipboard_get()
        if entry_text1.selection_get():
            # grab selectext from text box
            selected = entry_text1.selection_get()
            # Clear the clipboard then append
            entry_text1.clipboard_clear()
            entry_text1.clipboard_append(selected)

    # paste text
    def paste_text(e):
        global selected
        # check to see if we used keyboard shortcuts
        if e:
            selected = entry_text1.clipboard_get()
        else:
            if selected:
                position = entry_text1.index(INSERT)
                entry_text1.insert(position, selected)

    def save_as_file():
        text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="C:/", title="Enregistrer sous",
                                                 filetypes=(("All files", "*.*"),
                                                            ("Text Files", "*.txt"), ("Python File", "*.py"),
                                                            ("Word File", "*.doc"), ("Word File", "*.docx"),
                                                            ("Html File", "*.html"), ("Libre Office File", "*.odt"),))
        # Save the file
        text_file = open(text_file, "w")
        text_file.write(output_text.get(1.0, END))
        # CLose the file
        text_file.close()

    text_writting_button = tkinter.Button(text_writting, text="Crypter", width=10, height=1, command=summit1)
    text_writting_button_clear = tkinter.Button(text_writting, text="Effacer", width=10, height=1,
                                                command=clear_text)

    label.pack(pady=10)
    lb.pack(pady=5)
    entry_text1.pack()
    text_writting_button.pack(pady=5)
    lb2.pack(pady=5)
    output_text.pack()
    text_writting_button_clear.pack(pady=5)

    thirddmenu = tkinter.Menu(text_writting)

    files_menu3 = tkinter.Menu(thirddmenu, tearoff=0)
    files_menu3.add_command(label="Nouveau", command=new_file)
    files_menu3.add_command(label="Ouvrir", command=open_text)
    files_menu3.add_separator()
    files_menu3.add_command(label="Enregister sous", command=save_as_file)
    files_menu3.add_separator()
    files_menu3.add_command(label="Quitter", activebackground="red", command=text_writting.destroy)

    edition_menu3 = tkinter.Menu(thirddmenu, tearoff=0)
    edition_menu3.add_command(label="Copie", command=lambda: copy_text(False), accelerator="(Ctrl+c)")
    edition_menu3.add_command(label="Coller", command=lambda: paste_text(False), accelerator="(Ctrl+v)")
    edition_menu3.add_command(label="Couper", command=lambda: cut_text(False), accelerator="(Ctrl+x)")
    edition_menu3.add_separator()
    edition_menu3.add_command(label="Undo", command=entry_text1.edit_undo, accelerator="(Ctrl+z)")
    edition_menu3.add_command(label="Redo", command=entry_text1.edit_redo, accelerator="(Ctrl+y)")

    entry_text1.bind("<Control-Key-x>", cut_text)
    entry_text1.bind("<Control-Key-c>", copy_text)
    entry_text1.bind("<Control-Key-v>", paste_text)

    thirddmenu.add_cascade(label="Fichier", menu=files_menu3)
    thirddmenu.add_cascade(label="Edition", menu=edition_menu3)

    text_writting.config(menu=thirddmenu)


def info_window():
    window_info = tkinter.Toplevel(app)
    window_info.title("Information")
    window_info.geometry("370x120+850+350")
    window_info.config(background="#4065A4")
    lb = tkinter.Label(window_info, text="\n Logitiel pour crypter et décripter du text.\n Utiliser le même encodeur "
                                         "pour crypter et décrypter.\n Aussi vous pouvez mélanger d'un encodeur a l'autres,"
                                         " \n Seulement se souvenir de l'ordre que vous le faite. \n Choissiez l'une des options pour débuter",
                       font=("Courrier", 11), bg="#4065A4", fg="white")
    lb.pack()


def about():
    about_window = tkinter.Toplevel(app)
    about_window.title("À propos")
    about_window.geometry("250x80+900+350")
    about_window.config(background="#4065A4")
    lb = tkinter.Label(about_window, text="\n Utilitaire de cryptage, décriptage\n Version 1.0.0.4"
                                          "\n Tout droit réserver 2021", font=("Courrier", 11),
                       bg="#4065A4", fg="white")
    lb.pack()


# creation de la fenetre = parametrage
app = tkinter.Tk()
app.geometry("640x300+700+250")
app.iconbitmap("proxy-image.ico")
app.minsize(640, 300)
app.title("Crypteur / décrypteur de texte")
app.config(background="#4065A4")
label_title = tkinter.Label(app, text="Bienvenue sur l'application!", font=("Courrier", 30), bg="#4065A4", fg="white")
label_title.pack(padx=0, pady=55)
label_subtitle = tkinter.Label(app, text="Amusez vous!", font=("Courrier", 25), bg="#4065A4", fg="white")
label_subtitle.pack()

# Widgets...
mainmenu = tkinter.Menu(app)

files_menu = tkinter.Menu(mainmenu, tearoff=0)
files_menu.add_command(label="Quitter", activebackground="red", command=app.quit)

options_menu = tkinter.Menu(mainmenu, tearoff=0)
submenu1 = Menu(options_menu, tearoff=0)
submenu1.add_command(label="Coder un texte", command=wrote_code)
submenu1.add_command(label="Lire un code", command=decoding)
options_menu.add_cascade(label="Césard", menu=submenu1)
options_menu.add_separator()
submenu2 = Menu(options_menu, tearoff=0)
submenu2.add_command(label="Coder un texte", command=wrote_code2)
submenu2.add_command(label="Lire un code", command=decoding2)
options_menu.add_cascade(label="Javanais", menu=submenu2)
help_menu = tkinter.Menu(mainmenu, tearoff=0)
help_menu.add_command(label="Info", command=info_window)
help_menu.add_command(label="À propos", command=about)

mainmenu.add_cascade(label="Fichier", menu=files_menu)
mainmenu.add_cascade(label="Options", menu=options_menu)
mainmenu.add_cascade(label="?", menu=help_menu)

# Boucle principal
app.config(menu=mainmenu)
app.mainloop()
